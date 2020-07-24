# 06/17/2020 21:09

class Solution:
    def numberOfSteps (self, num: int) -> int:
        step = 0
        while num != 0:
            num = num // 2 if num % 2 == 0 else num - 1
            step += 1
        
        return step