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





if __name__ == '__main__':
    
    assert Solution().threeSum([-1,0,1,2,-1,-4]) == [[-1, -1, 2], [-1, 0, 1]]
    assert Solution().threeSum([0,1,1]) == []
    assert Solution().threeSum([0,0,0]) == [[0,0,0]]
