"""
Given a string s, return the longest palindromic substring in s.

Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
"""

"""
Constraints:
1 <= s.length <= 1000
s consist of only digits and English letters.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        t = "^#" + '#'.join(s) + "#$"
        radius = [0] * len(t)
        pCenter = pRight = 0

        for center in range(1, len(t)-1):
            if center < pRight:
                mirror = 2 * pCenter - center
                radius[center] = min(pRight - center, radius[mirror])

            while t[center + radius[center] + 1] == t[center - radius[center] - 1]:
                radius[center] += 1
        
            if center + radius[center] > pRight:
                pCenter, pRight = center, center + radius[center]

        maxLen, maxCenter = max((value, index) for index, value in enumerate(radius))
        start = (maxCenter - maxLen) // 2
        return s[start: start + maxLen]

"""
Time complexity = O(n)
Space complexity = O(n)
"""