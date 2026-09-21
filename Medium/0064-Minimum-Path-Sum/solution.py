class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j == 0: continue

                if i == 0:
                    grid[i][j] += grid[i][j-1]
                elif j == 0:
                    grid[i][j] += grid[i-1][j]
                else:
                    shorterPath = min(grid[i-1][j], grid[i][j-1])
                    grid[i][j] += shorterPath
                
        return grid[-1][-1]

"""
Time complexity = O(m * n)
Space complexity = O(1)
"""