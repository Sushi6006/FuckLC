# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:
# SELF-DEFINED IN THIS CODE

class Solution:

    def __init__(self, bad):
        self.bad = bad

    # ANSWER STARTS HERE
    def firstBadVersion(self, n: int) -> int:

        def isBadVersion(bad):
            return bad >= self.bad

        first, last = 1, n
        
        while last - first > 1:
            mid = (first + last) // 2
            if isBadVersion(mid):
                last = mid
            else:
                first = mid
        
        return first if isBadVersion(first) else last


if __name__ == "__main__":
    print(Solution(4).firstBadVersion(5))
    print(Solution(1).firstBadVersion(1))
    print(Solution(2).firstBadVersion(3))
