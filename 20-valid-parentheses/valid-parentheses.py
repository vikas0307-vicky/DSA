class Solution(object):
    def isValid(self, s):
        stack =[]
        mp ={
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for i in s:
            if i in mp:
                if not stack or stack[-1] != mp[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)

        return len(stack) == 0