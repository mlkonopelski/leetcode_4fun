
class Solution:
    def isPalindrome(self, s: str) -> bool:

        string = ''
        for l in s:
            if l.isalnum():
                string += l.lower()

        middle_ix = int(len(string)/2)
        if string[:middle_ix] == string[-middle_ix:][::-1] or len(string) == 1:
            return True
        else:
            return False

# PERFORMANCE
# Runtime 45 ms (Beats 56.19% of users with Python)
# Memory 17.15 MB (Beats 47.56% of users with Python)


class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = list(s)
        while len(s) > 1:
            if not s[0].isalnum():
                s.pop(0)
                continue
            if not s[-1].isalnum():
                s.pop()
                continue
            l_start, l_end = s.pop(0), s.pop()
            if not l_start.lower() == l_end.lower():
                return False
        return True

# PERFORMANCE
# Runtime 430 ms (Beats 5.01% of users with Python)
# Memory 17.63 MB (Beats 33.13% of users with Python)


class Solution:

    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l+=1
                continue
            if not s[r].isalnum():
                r-=1
                continue
            if not s[l].lower() == s[r].lower():
                return False
            else:
                l+=1
                r-=1
        return True

# PERFORMANCE
# Runtime 45 ms (Beats 56.19% of users with Python)
# Memory 17.06 MB (Beats 63.22% of users with Python)


if __name__ == '__main__':

    assert Solution().isPalindrome("A man, a plan, a canal: Panama") == True # "amanaplanacanalpanama" is a palindrome.
    assert Solution().isPalindrome("race a car") == False
    assert Solution().isPalindrome(" ") == True
    assert Solution().isPalindrome("a") == True
    assert Solution().isPalindrome("0P") == False
