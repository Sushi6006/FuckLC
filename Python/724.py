class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        left_sum = 0
        right_sum = sum(nums[1:])
        for i in range(len(nums) - 1):
            if left_sum == right_sum:
                return i
            else:
                left_sum += nums[i]
                right_sum -= nums[i + 1]
        if left_sum == 0:
            return len(nums) - 1
        return -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.pivotIndex([1, 7, 3, 6, 5, 6]))
    print(solution.pivotIndex([1, 2, 3]))
    print(solution.pivotIndex([2, 1, -1]))
    print(solution.pivotIndex([-1, -1, 0, 1, 1, 0]))
    print(solution.pivotIndex([-1, -1, -1, 1, 1, 1]))
