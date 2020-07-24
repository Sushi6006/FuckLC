# 06/17/2020 19:32

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        tot = 0
        for i in range(len(nums)):
            tot += nums[i]
            nums[i] = tot
        
        return nums