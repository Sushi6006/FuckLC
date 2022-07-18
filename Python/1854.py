class Solution:
    def maximumPopulation(self, logs: list[list[int]]) -> int:
        
        ### SOLUTION #1: USING LIST INDEXING AS DICTIONARY
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


        ### SOLUTION #2: LOOP THROUGH LOGS, MAY WORK BUT NOT YET
        # max_population = curr_population = max_year = curr_year = 0
        # logs.sort(key=lambda x: (x[0], x[1]))
        # for log in logs:

        #     print()

        #     if log[0] > curr_year:
        #         curr_population += 1
        #         curr_year = log[0]
        #     if log[1] <= curr_year:
        #         curr_population -= 1

        #     if curr_population > max_population:
        #         max_year = curr_year
        #         max_population = curr_population


        ### SOLUTION #3: THIS IS A REWORK FROM A SOLUTION FROM DISCUSSION BOARD
        flat_logs = []  # list with years and population change
        for log in logs:
            flat_logs.append((log[0], 1))
            flat_logs.append((log[1], -1))
        flat_logs.sort()

        max_year = max_population = curr_population = 0
        for log in flat_logs:
            curr_population += log[1]
            if curr_population > max_population:
                max_population = curr_population
                max_year = log[0]
        
        return max_year


if __name__ == "__main__":
    solution = Solution()
    print(solution.maximumPopulation([[1993, 1999], [2000, 2010]]))
    print(solution.maximumPopulation(
        [[1960, 1971], [1950, 1961], [1970, 1981]]))
    print(solution.maximumPopulation([[2033, 2034], [2039, 2047], [1998, 2042], [
          2047, 2048], [2025, 2029], [2005, 2044], [1990, 1992], [1952, 1956], [1984, 2014]]))
