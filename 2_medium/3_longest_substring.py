class Solution:
    '''
    This solution is wrong when we in case e.g. "dvdf" remove letter from substring when we go to second d instead of counting again from v
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        subset = ''
        max_length = 0
        for i, ss in enumerate(s):
            if ss not in subset:
                subset += ss
            else:
                max_length = max(max_length, len(subset))
                subset = ss
        #final check of max length in case string s is unique
        max_length = max(max_length, len(subset))
        return max_length

class Solution:
    '''
    Works!
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        len_s = len(s)
        if len_s == 0:
            return 0

        subset = ''
        max_length = 0
        temp_length = 0
        
        i=0
        j=0

        while True:

            if i+j < len_s and s[i+j] not in subset:
                subset += s[i+j]
                j+=1
                temp_length+=1
            else:
                max_length = max(max_length, temp_length)

                
                if i+1 == len_s or i+j == len_s:
                    break
                else:
                    i+=1
                    j=1
                    subset = s[i]
                    temp_length = 1
    
        return max_length

# PERFORMANCE
# Runtime 351 ms (Beats 7.79% of users with Python)
# Memory 16.70 MB (Beats 63.13% of users with Python)

# Better solution is with sliding window instead of looking on integers only
class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        
        len_s = len(s)

        subset = set()
        max_length = 0
        
        left=0

        for right in range(len_s):
            if s[right] not in subset:
                subset.add(s[right])
                max_length = max(max_length, right-left+1)
            else:
                while s[right] in subset:
                    subset.remove(s[left])
                    left+=1
                subset.add(s[right])
    
        return max_length
    

if __name__ == '__main__':
    
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3
    assert Solution().lengthOfLongestSubstring("") == 0
    assert Solution().lengthOfLongestSubstring(" ") == 1
    assert Solution().lengthOfLongestSubstring("au") == 2
    assert Solution().lengthOfLongestSubstring("dvdf") == 3



