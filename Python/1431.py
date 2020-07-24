# 06/17/2020 19:49

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        return [count + extraCandies >= max(candies) for count in candies]