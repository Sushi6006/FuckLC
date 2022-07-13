# faster than 99.38%, wow

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        isomap = {}  # map of chars

        for i in range(len(s)):
            if s[i] in isomap:
                if t[i] != isomap[s[i]]:
                    return False
            elif t[i] in isomap.values():
                # this elif branch is unnecessary, but a small optimisation
                return False
            else:
                isomap[s[i]] = t[i]

        return True


if __name__ == "__main__":
    solution = Solution()
    print(solution.isIsomorphic("egg", "add"))
    print(solution.isIsomorphic("foo", "bar"))
    print(solution.isIsomorphic("paper", "title"))
    print(solution.isIsomorphic("e", "a"))
    print(solution.isIsomorphic("eae", "aaa"))
    print(solution.isIsomorphic("aaa", "eae"))
