from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        i = 1
        break_ = False
        max_letters = max([len(s) for s in strs])
        while i <= max_letters:
            j = 0
            while j < len(strs) -1:
                first, second = strs[j][:i], strs[j+1][:i]
                if first != second:
                    break_ = True
                j+= 1
            if break_:
                break
            i+= 1

        return '' if i == 1 else strs[0][:i-1]
    
if __name__ == '__main__':
    assert Solution().longestCommonPrefix(strs = ["flower","flow","flight"]) == "fl"
    assert Solution().longestCommonPrefix(strs = ["dog","racecar","car"]) == ""
    assert Solution().longestCommonPrefix(strs = [""]) == ""
    assert Solution().longestCommonPrefix(strs = ["flower","flower","flower","flower"]) == "flower"
