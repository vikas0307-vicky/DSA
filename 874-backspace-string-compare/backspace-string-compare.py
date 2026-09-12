class Solution(object):
    def check(self, str):
        st=[]
        for i in str:
            if i != '#':
                st.append(i)
            elif st:
                st.pop()
        return "".join(st)

    def backspaceCompare(self, s, t):
        return self.check(s) == self.check(t)

