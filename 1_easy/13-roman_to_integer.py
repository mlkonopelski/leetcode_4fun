class Solution:
    def romanToInt(self, s: str) -> int:
        ROMAN = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}
        SPECIAL = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900   
        }
        
        # problem: performance not good enough
        integers = []

        for roman, integer in SPECIAL.items():
            if roman in s:
                integers.append(integer)
                s = s.replace(roman, '')
    
        for roman, integer in ROMAN.items():
            if roman in s:
                integers.extend([integer] * s.count(roman))
        
        return sum(integers)

# PERFORMANCE
# Runtime 53 ms (Beats 32.96% of users with Python)
# Memory 16.79 MB (Beats 51.96% of users with Python)
        

class Solution:
    def romanToInt(self, s: str) -> int:
        ROMAN = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}
        SPECIAL = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900   
        }

        for roman, integer in SPECIAL.items():
            s = s.replace(roman, f'{integer}-')

        for roman, integer in ROMAN.items():
            s = s.replace(roman, f'{integer}-')

        return sum([int(i) for i in s.split('-')[:-1]])

# PERFORMANCE
# Runtime 49 ms (Beats 51.90% of users with Python)
# Memory 16.52 MB (Beats 79.49% of users with Python)  

import re
class Solution:
    def romanToInt(self, s: str) -> int:
        ROMAN = {
            'I': '1-',
            'V': '5-',
            'X': '10-',
            'L': '50-',
            'C': '100-',
            'D': '500-',
            'M': '1000-'}
        SPECIAL = {
            'IV': '4-',
            'IX': '9-',
            'XL': '40-',
            'XC': '90-',
            'CD': '400-',
            'CM': '900-'   
        }
        
        s = re.sub(r"([A-Z]{2})",lambda m : SPECIAL.get(m.group(1),m.group(1)),s) # TODO: re.sub not working
        s = re.sub(r"([A-Z])",lambda m : ROMAN.get(m.group(1),m.group(1)),s)
        
        return sum([int(i) for i in s.split('-')[:-1]])

class Solution:
    def romanToInt(self, s: str) -> int:
        ROMAN = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}
        SPECIAL = {
            'IV': 4,
            'IX': 9,
            'XL': 40,
            'XC': 90,
            'CD': 400,
            'CM': 900   
        }
        integers = []
        while s:
            try:
                r = SPECIAL[s[-2:]]
                integers.append(r)
                s = s[:-2]
            except:
                r = ROMAN[s[-1]]
                integers.append(r)
                s = s[:-1]

        return sum(integers)

# PERFORMANCE
# Runtime 38 ms (Beats 93.58% of users with Python)
# Memory 16.64 MB (Beats 57.99% of users with Python) 

# PERFECT SOLUTION
class Solution:
    def romanToInt(self, s: str) -> int:
        ROMAN = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000}

        ans = 0

        for i in range(len(s)):
            if i < len(s) - 1 and ROMAN[s[i]] < ROMAN[s[i+1]]:
                ans -= ROMAN[s[i]]
            else:
                ans += ROMAN[s[i]]

        return ans

if __name__ == '__main__':
    
    assert Solution().romanToInt('III') == 3
    assert Solution().romanToInt('LVIII') == 58
    assert Solution().romanToInt('MCMXCIV') == 1994
