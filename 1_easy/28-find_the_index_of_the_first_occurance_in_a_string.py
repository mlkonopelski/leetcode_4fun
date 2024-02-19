class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    
# PERFORMANCE
# Runtime 38 ms (Beats 43.71% of users with Python)
# Memory 16.44 MB (Beats 92.17% of users with Python)

# FASTER SOLUTION
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n_len = len(needle)
        h_len = len(haystack[:-n_len]) + 1
        for h_ix in range(h_len):
            if haystack[h_ix: h_ix+n_len] == needle:
                return h_ix
        else:
            return -1

# PERFORMANCE
# Runtime 36 ms (Beats 54.93% of users with Python)
# Memory 16.55 MB (Beats Beats 70.74% of users with Python)

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except:
            return -1

# PERFORMANCE
# Runtime 33 ms (Beats 75.25%% of users with Python)
# Memory 16.48 MB (Beats Beats 95.33% of users with Python)

if __name__ == '__main__':
    assert Solution().strStr(haystack = "a", needle = "a") == 0
    assert Solution().strStr(haystack = "sadbutsad", needle = "sad") == 0
    assert Solution().strStr(haystack = "butsad", needle = "sad") == 3
    assert Solution().strStr(haystack = "leetcode", needle = "leeto") == -1
   
    
    