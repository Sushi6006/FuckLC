# 06/17/2020 21:03

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")