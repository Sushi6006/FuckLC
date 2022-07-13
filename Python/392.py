class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pos = 0  # current position/index in t
        for c in s:
            while pos < len(t) and t[pos] != c:
                pos += 1
            else:
                pos += 1
                if pos > len(t):
                    return False
        
        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isSubsequence("abc", "ahbgdc"))
    print(solution.isSubsequence("axc", "ahbgdc"))
    print(solution.isSubsequence("ace", "abcde"))
    print(solution.isSubsequence("aec", "abcde"))
    print(solution.isSubsequence("a", "a"))
    print(solution.isSubsequence("a", "aaaaa"))
