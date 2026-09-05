"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Example 1:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
"""

"""
Constraints:
1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000
"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s): return s

        rows = [""] * numRows
        row = 0
        moveDown = False

        for character in s:
            rows[row] += character

            if row == 0 or row == numRows-1:
                moveDown = not moveDown
            
            row += 1 if moveDown else - 1
        
        return "".join(rows)

"""
Time complexity = O(n)
Space complexity = O(n)
"""