"""
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,3]
Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""

"""
Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
All the numbers of nums are unique.
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start):
            res.append(path[:])
            
            for i in range(start, len(nums)):
                path.append(nums[i])

                backtrack(i+1)

                path.pop()
        
        backtrack(0)

        return res

"""
Time complexity = O(n × 2^n)
Space complexity = O(n)
"""