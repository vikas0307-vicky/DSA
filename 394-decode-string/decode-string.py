class Solution(object):
    def decodeString(self, s):
        stack = []
        num = 0
        curr =""

        for i in s:
            if i.isdigit():
                num = num * 10 +int(i)

            elif i =="[":
                stack.append((curr,num))
                curr = ""
                num = 0

            elif i == "]":
                prev,count = stack.pop()
                curr = prev + curr * count

            else:
                curr += i
            
        return curr

        