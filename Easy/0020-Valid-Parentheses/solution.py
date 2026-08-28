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