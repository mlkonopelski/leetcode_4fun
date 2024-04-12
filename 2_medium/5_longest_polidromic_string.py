class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        
        max_len = 1
        max_s = s[0]

        left = 0
        right = s_len - 1

        for left in range(s_len-1):
            for right in range(left+1, s_len+1):
                s_sub = s[left:right]
                if s_sub == s_sub[::-1] and len(s_sub) > max_len:
                    max_len = len(s_sub)
                    max_s = s_sub

        return max_s

# PERFORMANCE
# Runtime 7978 ms (Beats 9.00% of users with Python)
# Memory 16.65 MB (Beats 50.48% of users with Python)

class Solution:
    def longestPalindrome(self, s: str) -> str:
        s_len = len(s)
        
        max_len = 1
        max_s = s[0]

        left = 0
        right = 2

        while left < s_len-1:
            s_sub = s[left:right]
            if s_sub == s_sub[::-1]:
                if len(s_sub) > max_len:
                    max_len = len(s_sub)
                    max_s = s_sub
                
                if right < s_len:
                    right += 1
                else:
                    break
            else: 
                if right < s_len:
                    right += 1
                elif left < s_len - 1:
                    left += 1
                    right = left + 2
                else:
                    break

        return max_s

# PERFORMANCE
# Runtime 4313 ms (Beats 19.88% of users with Python)
# Memory 16.71 MB (Beats 29.30% of users with Python)


# USER SOLUTION I LIKE
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
                    return s

        def expand_from_center(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        max_str = s[0]

        for i in range(len(s) - 1):
            odd = expand_from_center(i, i)
            even = expand_from_center(i, i + 1)

            if len(odd) > len(max_str):
                max_str = odd
            if len(even) > len(max_str):
                max_str = even

        return max_str






if __name__ == '__main__':
    assert Solution().longestPalindrome("babad") in ['bab', 'aba']
    assert Solution().longestPalindrome("cbbd") == 'bb'
    assert Solution().longestPalindrome("ac") == 'a'
    assert Solution().longestPalindrome("a") == 'a'
    assert Solution().longestPalindrome("bb") == 'bb'
