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