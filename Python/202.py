class Solution:
    def isHappy(self, n: int) -> bool:
        appeared = set()
        while n != 1:
            n = int(sum(list(map(lambda x: int(x) ** 2, list(str(n))))))
            if n in appeared:
                return False
            else:
                appeared.add(n)
        return True