    
class Solution(object):
    def groupAnagrams(self, strs):
        d={}
        for i in strs:
            a="".join(sorted(i))
            if a in d:
                d[a].append(i)
            else:
                d[a]=[i]
        return d.values()

 