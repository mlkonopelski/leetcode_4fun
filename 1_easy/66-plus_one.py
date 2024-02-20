from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        # result = []
        # for i, d in enumerate(digits[::-1]):
        #     if d == 9:
        #         result += [0]
        #         digits += []
        #     else:
        #         return digits[:len_d - i - 1] + [d + 1] + result
        
        digits = int(''.join([str(d) for d in digits]))
        digits += 1
        return [int(i) for i in str(digits)]

# PERFORMANCE
# Runtime 35 ms (Beats 73.39% of users with Python)
# Memory 16.46 MB (Beats Beats 91.70% of users with Python)


if __name__ == '__main__':
    Solution().plusOne([1,2,3]) == [1,2,4]
    Solution().plusOne([4,3,2,2]) == [4,3,2,3]
    Solution().plusOne([9]) == [1, 0]
    Solution().plusOne([2, 9, 9]) == [3, 0, 0]
    