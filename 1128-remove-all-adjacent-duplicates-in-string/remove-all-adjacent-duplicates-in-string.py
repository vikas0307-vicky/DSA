class Solution(object):
    def removeDuplicates(self, s):

        # stack = []
        # for i in s:
        #     if stack and i == stack[-1]:
        #         stack.pop()
        #     else:
        #         stack.append(i)

        # return "".join(stack)


        st =[]
        for i in s:
            if st and i == st[-1]:
                st.pop()
            else:
                st.append(i)
        return "".join(st)


        