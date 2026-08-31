class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            if nums[i] > 0:
                break

            target = 0 - nums[i]

            left = i + 1
            right = len(nums) - 1

            while right > left:
                    
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])

                    left += 1
                    while left < right and nums[left] == nums[left-1]: left += 1

                    right -= 1
                    while right > left and nums[right] == nums[right+1]: right -= 1
                    
        return res