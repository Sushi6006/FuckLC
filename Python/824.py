class Solution:
    def toGoatLatin(self, S: str) -> str:
        res = ""
        for i, word in enumerate(S.split()):
            if len(word) <= 1 or word[0].lower() in "aeiou":
                res += word
            else:
                res += word[1:] + word[0]
            
            res += "ma" + (i + 1) * "a" + " "
        
        return res[:-1]