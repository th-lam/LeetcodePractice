"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2
"""

"""
Constraints:
1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while right >= left:
            median = (left + right) // 2

            if nums[median] < target:
                left = median + 1
            elif nums[median] > target:
                right = median - 1
            else:
                return median
        
        return left

"""
Time complexity = O(log n)
Space complexity = O(1)
"""