class Solution(object):
    def numberOfSteps(self, num):
        # odd and even 
        # when even div by 2
        # when odd sub by 1
        step = 0
        while num != 0:
            if num%2==0 :
                num = num/2
            else:
                num=num-1
            step = step+1
        return step

        