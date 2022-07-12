class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        # find
        while right - left > 1:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                right = mid
            else:
                left = mid
        
        if nums[left] == target:
            return left
        elif nums[right] == target:
            return right

        # insert
        if nums[left] < target < nums[right]:
            return right
        elif nums[left] > target:
            return left
        else:
            return right + 1

        
if __name__ == "__main__":
    solution = Solution()
    print(solution.searchInsert([1, 3, 5, 6], 5))  # 2
    print(solution.searchInsert([1, 3, 5, 6], 2))  # 1
    print(solution.searchInsert([1, 3, 5, 6], 7))  # 4
    print(solution.searchInsert([1, 3, 5, 6], 0))  # 0
