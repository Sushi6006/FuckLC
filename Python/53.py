# 07/24/2020 13:07

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr = max_sum = nums[0]
        for i in nums[1:]:
            curr = i if i > curr + i else curr + i
            max_sum = curr if curr > max_sum else max_sum
        
        return max_sum
            
