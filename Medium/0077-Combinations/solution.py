"""
Given two integers n and k,
return all possible combinations of k numbers chosen from the range [1, n].
You may return the answer in any order.
 
Example 1:
Input: n = 4, k = 2
Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
Explanation: There are 4 choose 2 = 6 total combinations.
Note that combinations are unordered,
i.e., [1,2] and [2,1] are considered to be the same combination.
"""

"""
Constraints:
1 <= n <= 20
1 <= k <= n
"""
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start: int):
            if len(path) == k:
                res.append(path[:])
                return

            for i in range(start, n + 1):
                if len(path) + (n - i + 1) < k:
                    break
                
                path.append(i)
                
                backtrack(i + 1)
                
                path.pop()

        backtrack(1)
        return res

"""
Time complexity = O(k × C(n, k))
Space complexity = O(k)
"""