class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        print
        if bits[-1] == 1:
            return False
        while len(bits) > 1:
            if bits[0] == 1:
                bits.pop(0)
            bits.pop(0)
        return len(bits) == 1        
        