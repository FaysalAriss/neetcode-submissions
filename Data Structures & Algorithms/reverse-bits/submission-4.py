class Solution:
    #input: 32 bit unsigned integer
    #output: 32 bit unsigned integer with the bits in reverse order compared to the input
    #0001
    #1000

    #0111
    #1110

    #0001101
    #1011000
    def reverseBits(self, n: int) -> int:
        return int(f"{bin(n)[2:][::-1]:032}", 2)