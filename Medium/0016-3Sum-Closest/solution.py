"""
Given an integer array nums of length n and an integer target, find three integers at distinct indices in nums such that the sum is closest to target.
Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Example 1:
Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""

"""
Constraints:
3 <= nums.length <= 500
-1000 <= nums[i] <= 1000
-104 <= target <= 104
"""

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]
        minDifference = abs(target - closest)

        for i in range(0, len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]: continue
            
            curMin = nums[i] + nums[i+1] + nums[i+2]
            if curMin > target:
                curDifference = abs(target - curMin)
                if curDifference < minDifference:
                    closest = curMin
                    minDifference =  curDifference
                    break

            curMax = nums[i] + nums[len(nums)-1] + nums[len(nums)-2]
            if curMax < target:
                curDifference = abs(target - curMax)
                if curDifference < minDifference:
                    closest = curMax
                    minDifference =  curDifference
                    continue
            
            left, right = i + 1, len(nums) - 1
            while left < right:
                curSum = nums[i] + nums[left] + nums[right]
                curDifference = abs(target - curSum)

                if curSum == target: return curSum

                if curDifference < minDifference:
                    closest = curSum
                    minDifference = curDifference

                if curSum < target: left += 1
                else: right -= 1

        return closest

"""
Time complexity = O(n ^ 2)
Space complexity = O(1)
"""