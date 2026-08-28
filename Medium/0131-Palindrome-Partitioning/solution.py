"""
131. Palindrome Partitioning
Given a string s, partition s such that every substring of the partition is a palindrome. 
Return all possible palindrome partitioning of s.

Example 1:
Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]
"""

"""
Constraints:
1 <= s.length <= 16
s contains only lowercase English letters.
"""

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        path = []

        def isPalindrome(substring):
            left = 0 
            right = len(substring) -1

            while left < right:
                if substring[left] != substring[right]: 
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start):
            if start == len(s):
                res.append(path[:])
                return

            for end in range(start, len(s)):
                substring = s[start: end+1]

                if isPalindrome(substring):
                    path.append(substring)
                else:
                    continue

                backtrack(start+len(substring))

                path.pop()

        backtrack(0)
        return res

"""
Time complexity = O(n × 2^n)
Space complexity = O(n)
"""