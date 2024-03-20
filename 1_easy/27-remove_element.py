from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        k = 0
        position = 0

        for n in nums:
            if n != val:
                nums[position] = n
                position +=1
                k+=1

        print(nums)
        return k

# PERFORMANCE
# Runtime 33 ms (Beats 81.49% of users with Python)
# Memory 16.56MB (Beats Beats 49.60% of users with Python)


if __name__ == '__main__':

    assert Solution().removeElement([3,2,2,3], 3) == 2
    assert Solution().removeElement([0,1,2,2,3,0,4,2], 2) == 5