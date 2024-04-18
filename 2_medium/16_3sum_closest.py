from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        
        nums_len = len(nums)
        best_match = 10**5
        best_result = None

        for i in range(0, nums_len-2):
            for j in range(i+1, nums_len-1):
                for k in range(j+1, nums_len):
                    r = nums[i] + nums[j] + nums[k]
                    match = abs(target - r)
                    if match < best_match:
                        best_match = match
                        best_result = r
                    elif match == target:
                        return match

        return best_result

# Correct but to slow
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        len_n = len(nums)
        if len_n == 3:
            return sum(nums)
        nums.sort()
        old_diff = abs(target - (nums[0]+nums[1]+nums[2]))
        new_diff = abs(target - (nums[1]+nums[2]+nums[3]))
        if old_diff < new_diff:
            return nums[0]+nums[1]+nums[2]

        i = 1
        while new_diff < old_diff and i < len_n-2:
            i+=1
            old_diff = new_diff
            new_diff = abs(target - (nums[i]+nums[i+1]+nums[i+2]))
        
        j = 1
        k = 1
        while i-j > 0 and i+k < len_n:
            left = nums[i-j]+nums[i]+nums[i+1]
            right = nums[i]+nums[i+1]+nums[i+1+k]
            if abs(target-left) < old_diff:
                old_diff = abs(target-left)
                j -= 1
            elif  abs(target-right) < old_diff:
                k += 1
            else:
                if j >= k:
                    k+=1
                else:
                    j+=1

        return nums[i-j]+nums[i]+nums[i+k]

# USER SOLUTION
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        n=len(nums)
        nums.sort()
        diff=20001
        val=0
        for i in range(n):
            a=i+1
            b=n-1
            while(a<b):
                cc=nums[i]+nums[a]+nums[b]
                kk=abs(cc-target)
                if(kk<diff):
                    diff=kk
                    val=cc
                if(cc==target):
                    return target
                elif(cc<target):
                    a+=1
                else:
                    b-=1
            
        return val

if __name__ == '__main__':

    assert Solution().threeSumClosest([-1,2,1,-4], 1) == 2
    assert Solution().threeSumClosest([0,0,0],  1) == 0
    assert Solution().threeSumClosest([1,1,1,0], -100) == 2
    assert Solution().threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2) == -2
