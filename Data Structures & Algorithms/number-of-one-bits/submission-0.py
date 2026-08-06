class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        for bit in bin(n)[2:]:
            if int(bit) == 1:
                total += 1

        return total