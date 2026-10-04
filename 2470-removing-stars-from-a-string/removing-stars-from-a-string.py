class Solution(object):
    def removeStars(self, s):
        stack = []
        for i in s:
            if i == "*":
                stack.pop()
            else:
                stack += i

        return "".join(stack)
        