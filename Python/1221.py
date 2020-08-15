class Solution:
    def balancedStringSplit(self, s: str) -> int:
        r, l = 0, 0
        count = 0
        for c in s:
            if c == 'R':
                r += 1
            elif c == 'L':
                l += 1
            
            if r == l and r != 0:
                count += 1
                r, l = 0, 0
        
        return count