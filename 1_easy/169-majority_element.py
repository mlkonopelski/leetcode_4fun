from collections import Counter
from typing import List 

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return Counter(nums).most_common(1)[0][0]
    
# PERFORMANCE
# Runtime 168 ms (Beats 10.95% of users with Python)
# Memory 17.92 MB (Beats Beats 83.55% of users with Python)

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = [nums[0], 1]
        # majority[] = 1
        for num in nums[1:]:
            if majority[0] == num:
                majority[1] += 1
            else:
                if majority[1] == 1:
                    majority[0] = num
                else:
                    majority[1] -= 1
        return majority[0]

# PERFORMANCE
# Runtime 178 ms (Beats 8.72% of users with Python)
# Memory 17.93 MB (Beats Beats 83.55% of users with Python)



class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums = sorted(nums)
        return nums[len(nums) // 2]


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for n in nums:
            try:
                count[n] += 1
            except:
                count[n] = 1
        return max(count, key=count.get)
    

if __name__ == '__main__':
    
    assert Solution().majorityElement([3,2,3]) == 3
    assert Solution().majorityElement([2,2,1,1,1,2,2]) == 2
    