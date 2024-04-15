class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        x = str(x)
        while x and x[-1] == "0":
            x = x[:-1]

        if x[0] == '-':
            inv = int('-' + x[1:][::-1])
        else:
            inv = int(x[::-1])
        
        if inv < -2147483648 or inv > 2147483647:
            return 0
        else:
            return inv
        
# PERFORMANCE
# Runtime 40 ms (Beats 32.49% of users with Python)
# Memory 16.57 MB (Beats 68.89% of users with Python)

    
if __name__ == '__main__':
    
    Solution().reverse(123) == 321
    Solution().reverse(-123) == -321
    Solution().reverse(120) == 21
    Solution().reverse(0) == 0
    Solution().reverse(1534236469) == 0

