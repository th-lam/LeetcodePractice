"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
"""

"""
Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        path = []

        def backtrack(start):
            res.append(path[:])

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue

                path.append(nums[i])

                backtrack(i + 1)

                path.pop()

        backtrack(0)
        return res

"""
Time complexity = O(n × 2^n)
Space complexity = O(n)
"""