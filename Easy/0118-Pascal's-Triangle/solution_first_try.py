class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        res = []
        for _ in range(1, numRows + 1):
            res.append([0] * _)

        for i in range(len(res)):
            for j in range(len(res[i])):
                if j == 0 or j == len(res[i]) - 1:
                    res[i][j] = 1 
                else:
                    res[i][j] = res[i-1][j-1] + res[i-1][j]

        return res

"""
Time complexity = O(n ^ 2)
Space complexity = O(n ^ 2)
"""