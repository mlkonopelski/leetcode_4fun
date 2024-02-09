class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) != len(set(nums)):
            return True
        else:
            return False
        

# PERFORMANCE
# Runtime 423 ms (Beats 83.04% of users with Python)
# Memory 27.57 MB (Beats 60.03% of users with Python)


# PERFECT SOLUTION
# class Solution(object):
    # def containsDuplicate(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: bool
    #     """
    #     unique = set()
    #     for n in nums:
    #         if n in unique:
    #             return True
    #         else:
    #             unique.add(n)
    #     return False
