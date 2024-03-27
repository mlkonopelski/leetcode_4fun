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
        
        comb = []
        letters = ''

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

        len_d = len(digits)
        
        for d in digits:


    


if __name__ == '__main__':

    print(Solution().letterCombinations("23"))
    print(Solution().letterCombinations("2"))
    print(Solution().letterCombinations(""))
