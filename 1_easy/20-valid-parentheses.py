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
    
    
if __name__ == '__main__':
    
    assert Solution().isValid('()') == True
    assert Solution().isValid('()[]{}') == True
    assert Solution().isValid('(]') == False