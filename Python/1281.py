# 06/17/2020 21:29

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = list(map(int, list(str(n))))
        tot = 1
        for i in n:
            tot *= i
        return tot - sum(n)
        