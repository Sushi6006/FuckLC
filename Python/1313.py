# 06/17/2020 21:22

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(0, len(nums), 2):
            for j in range(nums[i]):
                res.append(nums[i + 1])
        return res