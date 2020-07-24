# 06/17/2020 21:12

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        total = 0
        for c in J:
            total += S.count(c)
        return total