from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        try:
            while nums[i] < target:
                i += 1
        except:
            ...
        return i
    
# PERFORMANCE
# Runtime 56 ms (Beats 15.09% of users with Python)
# Memory 17.45 MB (Beats 16.81% of users with Python)

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        oon = True
        for i, n in enumerate(nums):
            if n >= target:
                oon = False
                break
        return i+ 1 if oon else i
    
# PERFORMANCE
# Runtime 52 ms (Beats 39.11% of users with Python)
# Memory 17.28 MB (Beats 85.03% of users with Python)

# Binary Search

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        while nums:
            mid_ix = len(nums)//2
            mid = nums[mid_ix]
            if target == mid:
                break
            elif target > mid:
                mid_ix += 1
                nums = nums[mid_ix:-1]
                # if not nums:
                #     mid_ix +=1
                #     break
            elif target < mid:
                nums = nums[0: mid_ix]
        return mid_ix

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) -1
        while left <= right:
            mid_ix = left + (right - left) // 2
            if target == nums[mid_ix]:
                return mid_ix
            elif target > nums[mid_ix]:
                left = mid_ix + 1
            elif target < nums[mid_ix]:
                right = mid_ix - 1
        return left
    
# PERFORMANCE
# Runtime 47 ms (Beats 74.86% of users with Python)
# Memory 17.22 MB (Beats 85.03% of users with Python)

if __name__ == '__main__':
    
    assert Solution().searchInsert([1,3,5,6], 5) == 2
    assert Solution().searchInsert([1,3,5,6], 2) == 1
    assert Solution().searchInsert([1,3,5,6], 7) == 4
    assert Solution().searchInsert([1,3,5,6], 0) == 0
    assert Solution().searchInsert([1,3], 1) == 1
