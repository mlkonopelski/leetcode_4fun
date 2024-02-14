class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        for i in range(len(x) // 2):
            if x[i] != x[-i-1]:
                return False
        return True

# PERFORMANCE
# Runtime 48 ms (Beats 83.65% of users with Python)
# Memory 16.47 MB (Beats 91.67% of users with Python)

# FAST SOLUTION
# class Solution:
#     def isPalindrome(self, x: int) -> bool:
#         if x < 0:
#             return False

#         x = str(x)
#         if x == x[::-1]:
#             return True
#         else:
#             return False    
