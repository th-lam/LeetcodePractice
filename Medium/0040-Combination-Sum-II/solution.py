"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: [[1,1,6], [1,2,5], [1,7], [2,6]]
"""

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        path = []

        def backtrack(start, total):
            if total > target:
                return
            elif total == target:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                path.append(candidates[i])

                backtrack(i + 1, total + candidates[i])

                path.pop()

        backtrack(0, 0)
        return res

"""
Time complexity = O(2 ^ n)
Space complexity = O(n)

N = number of candidates
T = value of target
M = value of the minimum candidate
"""