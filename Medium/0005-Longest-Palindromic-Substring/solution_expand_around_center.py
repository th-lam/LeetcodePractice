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
        maxLen = 1
        maxStart = 0

        def expandFromCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                    left -= 1
                    right += 1
            return right - left - 1, left + 1  # curLen = (right-1) - (left+1) + 1

        for center in range(len(s)):
            curLen, curStart = expandFromCenter(center, center) # odd
            if curLen > maxLen:
                maxLen = curLen
                maxStart = curStart

            curLen, curStart = expandFromCenter(center, center+1) # even
            if curLen > maxLen:
                maxLen = curLen
                maxStart = curStart

        return s[maxStart:maxStart + maxLen]

    """
Time complexity = O(n ^ 2)
Space complexity = O(1)
"""