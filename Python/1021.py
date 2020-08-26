class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        num = 0
        i = 0
        res = list(S)
        while i <= len(res) - 1:
            if res[i] == '(':
                if num == 0:
                    res.pop(i)
                    i -= 1
                num += 1
            else:
                num -= 1
                if num == 0:
                    res.pop(i)
                    i -= 1
            i += 1
        
        return "".join(res)