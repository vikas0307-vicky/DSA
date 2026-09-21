class Solution(object):
    def isValid(self, s):
        stack =[]
        # n = len(s)
        # if n%2==0:
        #     return False

        # st = []

        # for i in list(s):
        #     if i == "(" or i =="{" or i =="[":
        #         st.append(i)
        #     else:
        #         if len(st) == 0:
        #             return False
        #         top = st.pop()
        #         if i == ")" and top != "(":
        #             return False
        #         elif i == "}" and top != "{":
        #             return False
        #         elif i == "]" and top != "[":
        #             return False

        # return len(st) == 0
 

        mp ={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for i in s:
            if i in mp:
                if not  stack or stack[-1] != mp[i]:
                    return False
                stack.pop()
            else:
                stack.append(i)

        if len(stack) == 0:
            return True
        return False