class Solution(object):
    def mergeAlternately(self, str1, str2):
        result= ""
        for i in range(max(len(str1),len(str2))):
            if i < len(str1):
                result = result +str1[i]

            if i < len(str2):
                result = result +str2[i]

        return result
    

