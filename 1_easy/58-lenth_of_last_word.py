class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(' ')
        while True:
            s_ = s.pop()
            if s_.isalpha() and s_ != '':
                return s_

# PERFORMANCE
# Runtime 24 ms (Beats 97.82% of users with Python)
# Memory 16.44 MB (Beats 98.63% of users with Python)


class Solution:
    '''This breaks on last example'''
    def lengthOfLastWord(self, s: str) -> int:
        
        is_string = False
        i = -1
        
        while True:
            if s[-i] == ' ' and is_string:
                break
            elif s[-i] == ' ' and not is_string:
                i -= 1
            else:
                is_string = True
                i -= 1

        return len(s[i:-1].rstrip())

if __name__ == '__main__':
    
    Solution().lengthOfLastWord('Hello World') == 5
    Solution().lengthOfLastWord('   fly me   to   the moon  ') == 4
    Solution().lengthOfLastWord('luffy is still joyboy') == 6
    Solution().lengthOfLastWord('test') == 4
    