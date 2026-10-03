# class Solution(object):
#     def isBalanced(self, num):
#         even_sum = 0
#         odd_sum = 0
#         leg= len(num)
#         for i in range(leg):
#             if i % 2 == 0:
#                 even_sum = even_sum + int(num[i])
#             else:
#                 odd_sum = odd_sum + int(num[i])
#         return even_sum == odd_sum
class Solution(object):
    def isBalanced(self, num):
        e, o = 0, 0
        for i in range(len(num)):
            if i % 2 == 0:
                e += int(num[i])
            else:
                o += int(num[i])
        return e == o