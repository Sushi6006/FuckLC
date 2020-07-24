# 07/23/2020 18:03

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return list(str(int("".join(list(map(str, digits)))) + 1))
        