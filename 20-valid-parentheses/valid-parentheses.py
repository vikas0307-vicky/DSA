class Solution:
    def isValid(self, s):

        # stack = []
        # mp = {")":"(", "}":"{","]":"["}
        # for i in s:
        #     if i in mp:
        #         if not stack or stack.pop() != mp[i]:
        #             return False
        #     else:
        #         stack.append(i)
        # return not stack

        mp={")":"(","}":"{","]":"["}
        stack=[]
        for i in s:
            if i in mp:
                if not stack or stack.pop() != mp[i]:
                    return False
            else:
                stack.append(i)
        return not stack