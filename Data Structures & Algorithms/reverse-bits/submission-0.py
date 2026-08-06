class Solution:
    #input: 32 bit unsigned integer
    #output: 32 bit unsigned integer with the bits in reverse order compared to the input
    def reverseBits(self, n: int) -> int:
        return int(f"{bin(n)[2:]:>032}"[::-1], 2)