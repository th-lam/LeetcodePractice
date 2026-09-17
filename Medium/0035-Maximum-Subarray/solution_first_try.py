class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxRes = nums[0]
        curRes = 0
        
        for i in range(len(nums)):
            if nums[i] >= 0:
                if curRes < 0:
                    curRes = nums[i]
                else:
                    curRes += nums[i]
                
            else:
                if curRes + nums[i] < 0:
                    curRes = nums[i]
                else:
                    curRes += nums[i]

            maxRes = max(curRes, maxRes)
        return maxRes

"""
Time complexity = O(n)
Space complexity = O(1)
"""