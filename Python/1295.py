# i wrote this left to right in one go bitch
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return list(map(lambda x: len(str(x)) % 2 == 0, nums)).count(True)