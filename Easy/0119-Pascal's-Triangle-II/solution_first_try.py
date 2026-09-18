class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        prevRow = []

        for i in range(rowIndex + 1):
            curRow = [1] * (i + 1)
            for j in range(1, i):
                curRow[j] = prevRow[j-1] + prevRow[j]
            prevRow = curRow
        
        return prevRow

"""
Time complexity = O(n ^ 2)
Space complexity = O(n)
"""