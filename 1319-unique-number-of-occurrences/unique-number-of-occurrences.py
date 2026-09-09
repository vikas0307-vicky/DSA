class Solution(object):
    def uniqueOccurrences(self, arr):
        dic = {}
        for i in arr:
            if i in dic:
                dic[i] = dic[i]+1
            else:
                dic[i] = 1

        if len(set(dic.values())) != len(set(arr)):
            return False
        return True



        # for i in range(len(arr)):
        #     if arr.count(i) != arr.count(i):
        #         return True
        #     else:
        #         return False


        