# THIS IS O(N)

class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:

        # find mid (first non-negative number)
        mid = -1
        for i in range(len(nums)):
            if nums[i] >= 0:
                mid = i
                break
        
        # special conditions
        if not mid:  # if mid is the first digit
            return [num ** 2 for num in nums]
        elif nums[-1] <= 0:  # if every number negative
            return [num ** 2 for num in nums[::-1]]

        # add to new list with two pointers
        squares = []
        left, right = mid - 1, mid
        while left >= 0 and right < len(nums):
            if abs(nums[left]) > abs(nums[right]):
                squares.append(nums[right] ** 2)
                right += 1
            else:
                squares.append(nums[left] ** 2)
                left -= 1
        
        # add the rest of the lists
        if len(nums) - right >= 1:
            squares += [num ** 2 for num in nums[right:len(nums)]]
        elif left >= 0:
            squares += [num ** 2 for num in nums[0:left + 1][::-1]]

        return squares


if __name__ == "__main__":
    solution = Solution()
    print(solution.sortedSquares([-4,-1,0,3,10]))
    print(solution.sortedSquares([-4,-1,0,3,10]))
    print(solution.sortedSquares([0]))
    print(solution.sortedSquares([0, 0, 0]))
    print(solution.sortedSquares([0, 10, 100]))
    print(solution.sortedSquares([-10, 0, 10, 100]))
    print(solution.sortedSquares([-1000, -100, -10, 0, 10, 100]))
    print(solution.sortedSquares([-2, -1, -1, 0, 1, 1, 2]))
    print(solution.sortedSquares([-3, -2, -1]))
    print(solution.sortedSquares([-3, -2, -1, 0]))
    print(solution.sortedSquares([-3, 0, 2]))

