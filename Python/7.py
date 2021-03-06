class Solution:
    def reverse(self, x: int) -> int:
        ans = -int(str(abs(x))[::-1]) if x < 0 else int(str(abs(x))[::-1])
        return ans if (ans in range(- (2 ** 31), 2 ** 31 - 1) and x in range(- (2 ** 31), 2 ** 31 - 1)) else 0