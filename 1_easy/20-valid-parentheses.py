class Solution:
    def isValid(self, s: str) -> bool:
        
        valid = True

        while valid and s:
            s_ = s.replace(r'[]', '').replace('()', '').replace('{}','')
            if len(s_) == len(s):
                valid = False
                break
            else:
                s = s_
        
        return True if valid else False
    

class Solution:
    def isValid(self, s: str) -> bool:
        
        previous = ''
        invalid = ['(]', '(}', '{)', '{]', '[)', '[}']
        valid = ['()', '[]', '{}']
        
        for i, ch in enumerate(s):
            if previous and previous[-1] + ch in invalid:
                return False
            elif previous and previous[-1] + ch in valid:
                previous = previous[:-1]
            else:
                previous += ch
        
        return False if previous else True

# PERFORMANCE
# Runtime 35 ms (Beats 64.65% of users with Python)
# Memory 16.83 MB (Beats 50.45% of users with Python)

    
if __name__ == '__main__':
    
    assert Solution().isValid('()') == True
    assert Solution().isValid('()[]{}') == True
    assert Solution().isValid('(]') == False
    assert Solution().isValid('([][()])') == True