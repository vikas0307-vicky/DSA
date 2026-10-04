class Solution:
    def isValid(self, s):
        # stack = []
        # pairs = {')': '(', ']': '[', '}': '{'}

        # for i in s:
        #     if i in pairs:
        #         if not stack or stack.pop() != pairs[i]:
        #             return False
        #     else:
        #         stack.append(i)

        # return not stack

        stack = []
        mp = {")":"(", "}":"{","]":"["}
        for i in s:
            if i in mp:
                if not stack or stack.pop() != mp[i]:
                    return False
            else:
                stack.append(i)
        return not stack