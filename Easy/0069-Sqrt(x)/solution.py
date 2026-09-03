"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.

Example 1:
Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., 
and since we round it down to the nearest integer, 2 is returned.
"""

"""
Constraints:
0 <= x <= 231 - 1
"""

class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x

        while right >= left:
            median = (right + left) // 2
            
            if median * median > x:
                right = median - 1
            elif median * median < x:
                left = median + 1
            else:
                return median
        
        return right

"""
Time complexity = O(log n)
Space complexity = O(1)
"""