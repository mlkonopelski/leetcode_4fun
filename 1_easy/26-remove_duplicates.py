from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        last_unique = 0
        potential = 1
        k = 1

        while potential < len(nums):
            if nums[potential] != nums[last_unique]:
                nums[last_unique + 1] = nums[potential]
                k += 1
                last_unique += 1
            potential += 1

        return k

# PERFORMANCE
# Runtime 75 ms (Beats 62.48% of users with Python)
# Memory 17.97 MB (Beats Beats 58.42% of users with Python)


if __name__ == '__main__':
    assert Solution().removeDuplicates([1,1,2]) == 2
    assert Solution().removeDuplicates([0,0,1,1,1,2,2,3,3,4]) == 5
