class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: list[list[int]]) -> int:
        if obstacleGrid[0][0] == 1: return 0
        obstacleGrid[0][0] = 1

        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if i == 0 and j == 0: continue

                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                    continue

                if i == 0:
                    obstacleGrid[i][j] = obstacleGrid[i][j-1]
                elif j == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j]
                else:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]

        return obstacleGrid[-1][-1]

"""
Time complexity = O(m * n)
Space complexity = O(1)
"""