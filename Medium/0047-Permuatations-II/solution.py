"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

Example 1:
Input: nums = [1,1,2]
Output: [[1,1,2], [1,2,1], [2,1,1]]
"""

"""
Constraints:
1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        path = []
        used = [False] * len(nums)
        
        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                
                used[i] = True
                path.append(nums[i])

                backtrack()
                
                path.pop()
                used[i] = False
        
        backtrack()
        return res

"""
Time complexity = O(n! × n)
Space complexity = O(n)
"""