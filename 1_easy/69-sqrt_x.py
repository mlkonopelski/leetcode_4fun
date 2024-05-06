class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0
        while i*i <= x:
            i += 1
        return i-1

# PERFORMANCE
# Runtime 993 ms (Beats 17.79% of users with Python)
# Memory 16.48 MB (Beats 89.56% of users with Python)

# BEST USER SOLUTION
class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x
        while left <= right:
            mid = (left + right) // 2
            if mid * mid < x:
                left = mid + 1
            elif mid * mid > x:
                right = mid -1
            else:
                return mid
            
        return right

