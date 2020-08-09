class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in indices:            
                indices[num].append(i)
            else:
                indices[num] = [i]
        for i in range(len(nums)):
            num = nums[i]
            if (num2 := target - nums[i]) in indices:
                if len(indices[num2]) > 1:
                    return [i, indices[num2][-1]]
                elif indices[num2][0] != i:
                    return [i, indices[num2][0]]