"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.

Example 1:
Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
"""

"""
Constraints:
1 <= nums.length <= 200
-109 <= nums[i] <= 109
-109 <= target <= 109
"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        for i in range(0, len(nums)-3):

            if i > 0 and nums[i] == nums[i-1]: continue
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target: break

            for j in range(i+1, len(nums)-2):

                if j > i + 1 and nums[j] == nums[j-1]: continue
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target: break
                if nums[i] + nums[j] + nums[-2] + nums[-1] < target: continue
                
                left, right = j + 1, len(nums) - 1
                while left < right:
                    if nums[i] + nums[j] + nums[left] + nums[right] > target:
                        right -= 1
                    elif nums[i] + nums[j] + nums[left] + nums[right] < target:
                        left += 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        right -= 1
                        while left < right and nums[right] == nums[right+1]: right -= 1
                        
                        left += 1
                        while left < right and nums[left] == nums[left-1]: left += 1

        return res

"""
Time complexity = O(n ^ 3)
Space complexity = O(1)
"""