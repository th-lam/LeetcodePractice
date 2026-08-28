"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
"""

"""
Constraints:
1 <= n <= 8
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(path, openCount, closeCount):
            if len(path) == 2 * n:
                res.append(path)
                return
            
            if openCount < n:
                backtrack(path + "(", openCount+1, closeCount)

            if closeCount < openCount:
                backtrack(path + ")", openCount, closeCount+1)

        backtrack("(", 1, 0)
        return res

"""
Time complexity = O(4^n / √n)
Space complexity = O(n)
"""