"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

"""
Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

class Solution:
    def isValid(self, s: str) -> bool:
        sStack = []
        sMapping = {")":"(", "}":"{", "]":"["}

        for character in s: 
            if character in sMapping:
                if len(sStack) == 0 or sStack.pop() != sMapping[character]:
                    return False
            else:
                sStack.append(character)

        return len(sStack) == 0

"""
Time complexity = O(n)
Space complexity = O(n)
"""