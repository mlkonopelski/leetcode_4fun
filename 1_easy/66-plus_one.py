from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        digits = int(''.join([str(d) for d in digits]))
        digits += 1
        return [int(i) for i in str(digits)]

# PERFORMANCE
# Runtime 35 ms (Beats 73.39% of users with Python)
# Memory 16.46 MB (Beats Beats 91.70% of users with Python)


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = []
        decimal = 1
        for i, d in enumerate(digits[::-1]):
            if d + decimal > 9:
                result += [0]
            else:
                return digits[: - i - 1] + [d + 1] + result
        return digits[: - i - 1] + [1] + result

# PERFORMANCE
# Runtime 35 ms (Beats 73.32% of users with Python)
# Memory 16.42 MB (Beats Beats 91.41% of users with Python)

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] == 9:
            carry = 1
            i = len(digits) - 1
            while carry and i >= 0:
                if digits[i] != 9:
                    digits[i]+=1
                    break
                else:
                    digits[i] = 0
            if carry: digits.insert(0, 1)
            return digits
                    
                
        else:
            digits[-1] += 1
            return digits
                    


if __name__ == '__main__':
    assert Solution().plusOne([1,2,3]) == [1,2,4]
    assert Solution().plusOne([4, 9, 8, 9]) == [4,9, 9, 0]
    assert Solution().plusOne([9]) == [1, 0]
    assert Solution().plusOne([1, 2, 9, 9]) == [1, 3, 0, 0]
    assert Solution().plusOne([9, 9, 9, 9]) == [1, 0, 0, 0, 0]
    