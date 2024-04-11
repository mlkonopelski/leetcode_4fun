from typing import List


class Solution:
    """
    Good Solution but max exceeds time
    """
    def maxArea(self, height: List[int]) -> int:
        h_len = len(height)
        max_total = 0
        for i in range(0, h_len-1):
            for j in range(i+1, h_len):
                total = min(height[i], height[j]) * (j-i)
                max_total = max(total, max_total)
        return max_total


class Solution:
    """
    This solution is smarter because it finds biggest square based on assumptions that distance is important
    """
    def maxArea(self, height: List[int]) -> int:
        h_len = len(height)
        left = 0
        right = h_len - 1
        max_area = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


# PERFORMANCE
# Runtime 532 ms (Beats 39.65% of users with Python)
# Memory 29.63 MB (Beats 42.04% of users with Python)

if __name__ == '__main__':
    assert Solution().maxArea([1,8,6,2,5,4,8,3,7]) == 49
    assert Solution().maxArea([1,1]) == 1