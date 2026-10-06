class Solution(object):
    def haveConflict(self, event1, event2):
        s1 = event1[0]
        e1 = event1[1]

        s2=event2[0]
        e2=event2[1]

        if e1<s2:
            return False
        
        if e2<s1:
            return False

        return True
        