class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip().rstrip()
        int_ = s[0]
        i = 1
        while i <= len(s[1:]):
            if not s[i].isdigit():
                break
            else:
                i += 1
        int_ = int(int_ + s[1:i])
        int_ = max(-2**31, int_)
        int_ = min(int_, 2**31 -1)
        return int_


class Solution:
    def myAtoi(self, s: str) -> int:

        i = 0
        start_int = None
        end_int = len(s)
        while i < end_int:
            if s[i].isdigit() and start_int is None:
                start_int = i
            elif not s[i].isdigit() and start_int is not None:
                end_int = i
                break
            i += 1
        
        neg = ''
        try:
            if s[start_int-1] == '-':
                neg = '-'
        except:
            ...
        int_ = int(neg + s[start_int:end_int])

        int_ = max(-2**31, int_)
        int_ = min(int_, 2**31 -1)

        return int_


if __name__ == '__main__':

    assert Solution().myAtoi('42') == 42
    assert Solution().myAtoi('   -42') == -42
    assert Solution().myAtoi('4193 with words') == 4193
    assert Solution().myAtoi('words and 987') == 987
