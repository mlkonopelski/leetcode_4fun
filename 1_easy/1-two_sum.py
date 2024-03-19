""" DESCRIPTION
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]


# PERFORMANCE
# Runtime 2150 ms (Beats 41.05% of users with Python)
# Memory 12.48 MB (Beats 94.09% of users with Python)

# PERFECT SOLUTION
# class Solution(object):
    # def twoSum(self, nums, target):
    #     """
    #     :type nums: List[int]
    #     :type target: int
    #     :rtype: List[int]
    #     """
    #     tried = {}
    #     for i, num in enumerate(nums):
    #         j = target - num
    #         if j in tried:
    #             return [i, tried[j]]
    #         tried[num] = i
    #     return []


class Solution(object):
    def twoSum(self, nums, target):
        nums.sort()
        i = 0
        j = len(nums) - 1
        
        while i < j:
            if nums[i] + nums[j] == target:
                return [i, j]
            elif nums[i] + nums[j] > target:
                j -= 1
            else:
                i += 1


if __name__ == '__main__':

    assert Solution().twoSum([2,7,11,15], 9) == [0,1]
    assert Solution().twoSum([3,2,4], 6) == [0,1]