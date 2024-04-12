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


if __name__ == '__main__':
    assert Solution().longestPalindrome("babad") == 'bab'
    assert Solution().longestPalindrome("cbbd") == 'bb'
    assert Solution().longestPalindrome("ac") == 'a'
    assert Solution().longestPalindrome("a") == 'a'
    assert Solution().longestPalindrome("bb") == 'bb'
