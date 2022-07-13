class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        # first_birth = 2051
        # last_death = 1949

        # for li in logs:
        #     if li[0] < first_birth:
        #         first_birth = li[0]
        #     if li[1] > last_death:
        #         last_death = li[1]

        # birth_years = [0 for _ in range(last_death - first_birth)]
        # for li in logs:
        #     for i in range(li[0] - first_birth, li[1] - first_birth):
        #         birth_years[i] += 1

        # return birth_years.index(max(birth_years)) + first_birth

        max_population = max_year = curr_population = 1
        logs.sort(key=lambda x: (x[0], x[1]))
        year = logs[0][0]
        for li in logs:
            print(f'year: {year};  curr_population: {curr_population}')
            if li[1] <= year:
                curr_population -= 1
            elif li[0] >= year:
                curr_population += 1
            if curr_population > max_population:
                max_population = curr_population
                max_year = year
            year = li[0] if li[0] < li[1] else li[1]

        return max_year


if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumPopulation([[1993, 1999], [2000, 2010]]))
    print(solution.maximumPopulation(
        [[1960, 1971], [1950, 1961], [1970, 1981]]))
    print(solution.maximumPopulation([[2033, 2034], [2039, 2047], [1998, 2042], [
          2047, 2048], [2025, 2029], [2005, 2044], [1990, 1992], [1952, 1956], [1984, 2014]]))

    
    
    
    
    

    
    
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
        length = len(nums)  # this method uses len too often
        k = k % length
        if k == 0:
            return
        if k < length / 2:
            new_end = nums[k]
            for i in range(k):
                nums[k + i] = nums[i]
                nums[i] = nums[k + i + 1]
            nums[-1] = new_end
        elif k > length / 2:
            pass
        else:
            for i in range(k):
                nums[i], nums[k + i] = nums[k + i], nums[i]

        


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
