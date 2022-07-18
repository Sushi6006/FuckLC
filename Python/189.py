# LEETCODE QUESTION 189 METHOD NO.3 UNFINISHED

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        ##### METHOD ONE: NOT IN PLACE #####
        """
        nums = nums[len(nums) - k:] + nums[:len(nums) - k]
        """

        ##### METHOD ONE MODIFIED: PASSED #####
        # O(n) extra space, O(n) time, faster than 98.4%
        """
        k = k % len(nums)
        for i, num in enumerate(nums[len(nums) - k:] + nums[:len(nums) - k]):
            nums[i] = num
        """

        ##### METHOD TWO: O(kn) - TIME LIMIT EXCEEDED #####
        """
        for _ in range(k):
            # replace
            num = nums[-1]
            for j in range(len(nums) - 1, 0, -1):
                nums[j] = nums[j - 1]
            nums[0] = num
        """

        ##### METHOD THREE: IN PLACE O(n) #####
        ### i rewrote this method more than 8 times already
        ### ill come back to it
        length = len(nums)  # this method uses len too often
        k = k % length
        if k == 0:
            return
        temp = nums[k % length]
        for i in range(length):
            nums[(i + k) % length] = nums[i]
        nums[i - 1] = temp
        

        


if __name__ == "__main__":
    solution = Solution()

    nums = [1, 2, 3, 4, 5, 6, 7]
    solution.rotate(nums, 3)
    print(nums)

    nums = [-1, -100, 3, 99]
    solution.rotate(nums, 2)
    print(nums)

    nums = [0]
    solution.rotate(nums, 100)
    print(nums)

    nums = [1, 2, 3, 4, 5]
    solution.rotate(nums, 3)
    print(nums)
