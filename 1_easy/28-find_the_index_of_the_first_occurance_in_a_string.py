class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    
# PERFORMANCE
# Runtime 38 ms (Beats 43.71% of users with Python)
# Memory 16.44 MB (Beats 92.17% of users with Python)

# FASTER SOLUTION
# class Solution:
#     def strStr(self, haystack: str, needle: str) -> int:
#         i = 0
#         while i < len(needle):
#             for j in range(len(haystack)):
#                 if haystack[i] != needle[j]:
#                     i = 0
#                     break
#                 else:
#                     i+=1
#                     if i == len(needle):
#                         return j
#             return -1
        

            

        return haystack.find(needle)

if __name__ == '__main__':
    assert Solution().strStr(haystack = "sadbutsad", needle = "sad") == 0
    assert Solution().strStr(haystack = "butsad", needle = "sad") == 3
    assert Solution().strStr(haystack = "leetcode", needle = "leeto") == -1
    
    