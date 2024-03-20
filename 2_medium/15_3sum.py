from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []

        nums = sorted(nums)

        max_ix = len(nums)

        ix_1 = 0
        ix_2 = 1
        ix_3 = 2

        while True:
            print(ix_1, ix_2, ix_3)
            s = [nums[ix_1], nums[ix_2], nums[ix_3]]
            if sum(s) == 0:
                if s not in result:
                    result.append(s)
            if ix_3 < max_ix - 1:
                ix_3 += 1
            elif ix_2 < max_ix - 2:
                ix_2 += 1
                ix_3 = ix_2 + 1
            elif ix_1 < max_ix - 3:
                ix_1 += 1
                ix_2 = ix_1 + 1
                ix_3 = ix_2 + 1
            else:
                break
    
        return result

# Three pointer approach
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        nums = sorted(nums)
        nums_len = len(nums)

        fix_id = 0
        left_id = 1
        right_id = nums_len -1
        
        while fix_id <= nums_len - 3:
            while left_id < right_id:
                s = [nums[fix_id], nums[left_id], nums[right_id]]
                if sum(s) == 0:
                    if s not in result:
                        result.append(s)
                    left_id += 1
                elif sum(s) > 0:
                    right_id -= 1
                else:
                    left_id += 1
            fix_id += 1
            left_id = fix_id + 1
            right_id = nums_len -1

        return result


# BEST USER SOLUTION
# https://leetcode.com/problems/3sum/solutions/725950/python-5-easy-steps-beats-97-4-annotated/
from itertools import combinations

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = set()

        # 1. Split nums into three lists: negative numbers, positive numbers, and zeros
        n, p, z = [], [], []
        for num in nums:
            if num == 0:
                z.append(num)
            elif num > 0:
                p.append(num)
            else:
                n.append(num)
        
        # 2. Create sets for p and n for O(1) lookup
        N, P = set(n), set(p)

        # 4. If there is 0 search for opposite numbers:
        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num, 0, num))
            # 3. If there are 3 zeros add to reults
            if len(z) >= 3:
                res.add((0, 0, 0))
        
        # 5. for all pairs in negative side check if there is solution in positive side
        for s in [n, p]:
            for x, y in combinations(s, 2):
                target = -1 * (x+y)
                if target in P:
                    res.add(tuple(sorted([x, y, target])))

        return [list(r) for r in res]


if __name__ == '__main__':
    
    assert Solution().threeSum([-1,0,1,2,-1,-4]) == [[-1, 0, 1], [-1, -1, 2]]
    assert Solution().threeSum([0,1,1]) == []
    assert Solution().threeSum([0,0,0]) == [[0,0,0]]
