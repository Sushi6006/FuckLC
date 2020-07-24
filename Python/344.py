# 06/22/2020 01:42

class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def rev(counter, s):
            # base
            if counter >= (len(s) // 2):
                return
            
            s[counter], s[-(counter + 1)] = s[-(counter + 1)], s[counter]
            counter += 1
            rev(counter, s)
        
        rev(0, s)
        