from typing import List
from itertools import combinations

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        This solutiion is wrong because it gives all possible combinations
        """
        comb = []
        letters = ''

        LETTERS = {
            1: '',
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
            }

        len_d = len(digits)
        if len_d == 0:
            return []
        if len_d == 1:
            return list(LETTERS[int(digits)])

        for d in digits:
            letters += LETTERS[int(d)]

        for a, b in combinations(letters, len_d):
            comb.append(f'{a}{b}')

        return sorted(comb)


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        digits = list(digits)
        l_digits = len(digits)

        LETTERS = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
            }
        
        try:
            letters_1 = list(LETTERS[int(digits[0])])
        except:
            letters_1 = []
        try:
            letters_2 = list(LETTERS[int(digits[1])])
        except:
            letters_2 = []
        try:
            letters_3 = list(LETTERS[int(digits[2])])
        except:
            letters_3 = []
        try:
            letters_4 = list(LETTERS[int(digits[3])])
        except:
            letters_4 = []

        result = []

        for l_1 in letters_1:
            if l_digits == 1:
                result.append(l_1)
                continue
            for l_2 in letters_2:
                if l_digits == 2:
                    result.append(l_1+l_2)
                    continue
                for l_3 in letters_3:
                    if l_digits == 3:
                        result.append(l_1+l_2+l_3)
                        continue
                    for l_4 in letters_4:
                        result.append(l_1+l_2+l_3+l_4)

        return result
    

# PERFORMANCE
# Runtime 26 ms (Beats 96.67% of users with Python)
# Memory 16.56 (Beats 41% of users with Python)
    

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        digits = list(digits)
        l_digits = len(digits)

        LETTERS = {
            2: 'abc',
            3: 'def',
            4: 'ghi',
            5: 'jkl',
            6: 'mno',
            7: 'pqrs',
            8: 'tuv',
            9: 'wxyz'
            }
        
        try:
            letters_1 = list(LETTERS[int(digits[0])])
        except:
            letters_1 = []
        try:
            letters_2 = list(LETTERS[int(digits[1])])
        except:
            letters_2 = []
        try:
            letters_3 = list(LETTERS[int(digits[2])])
        except:
            letters_3 = []
        try:
            letters_4 = list(LETTERS[int(digits[3])])
        except:
            letters_4 = []

        result = []

        if l_digits == 1:
            for l_1 in letters_1:
                result.append(l_1)
        
        elif l_digits == 2:
            for l_1 in letters_1:
                for l_2 in letters_2:
                    result.append(l_1+l_2)

        elif l_digits == 3:
            for l_1 in letters_1:
                for l_2 in letters_2:
                    for l_3 in letters_3:
                        result.append(l_1+l_2+l_3)
        elif l_digits == 4:
            for l_1 in letters_1:
                for l_2 in letters_2:
                    for l_3 in letters_3:
                        for l_4 in letters_4:
                            result.append(l_1+l_2+l_3+l_4)
        else:
            raise Exception('Out of bounds')

        return result

# PERFORMANCE
# Runtime 29 ms (Beats 90.45% of users with Python)
# Memory 16.82MB (Beats 9.98% of users with Python)


# BEST USER SOLUTION
# NOTES: USe recursive function that starts from first digits and goes to next
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:


        LETTERS = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
            }
        
        result = []

        def backtrack(i, curr_str):
            if len(curr_str) == len(digits):
                result.append(curr_str)
                return 
            for c in LETTERS[digits[i]]:
                backtrack(i+1, curr_str+c)

        if digits:
            backtrack(0, '')

        return result

if __name__ == '__main__':

    print(Solution().letterCombinations("23"))
    print(Solution().letterCombinations("2"))
    print(Solution().letterCombinations(""))
