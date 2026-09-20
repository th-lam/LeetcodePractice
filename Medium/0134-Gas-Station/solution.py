class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        totalSum = 0
        curSum = 0
        curIdx = 0

        for i in range(len(gas)):
            totalSum += (gas[i] - cost[i])
            curSum += (gas[i] - cost[i])
            if curSum < 0:
                curSum = 0
                curIdx = i + 1
            
        if totalSum < 0: return -1
        return curIdx

"""
Time complexity = O(n)
Space complexity = O(1)
"""