class Solution:
    def search(self, nums: list[int], target: int) -> int:
      
        left, right = 0, len(nums) - 1

        if nums[left] == target:
            return target
        if nums[right] == target:
            return target

        while right - left > 1:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid
            else:
                left = mid

        return -1


if __name__ == "__main__":
    solution = Solution()
    print(solution.search([-1, 0, 3, 5, 9, 12], 9))
    print(solution.search([-1, 0, 3, 5, 9, 12], 2))
    print(solution.search([5], 5))
