class Solution:
    #input: 32 bit unsigned integer
    #output: 32 bit unsigned integer with the bits in reverse order compared to the input
    #0001
    #1000

    #0111
    #1110

    #0111 & 0001 = 0001
    #0111 & 1000 = 0000
    #0111 &= 1111
    #

    #0001101
    #1011000
    def reverseBits(self, n: int) -> int:
        for i in range(16):
            rightBit = n & (1 << i)
            leftBit = n & (1 << (31-i))
            n = (n | 1 << i) if leftBit else (n & ~(1 << i))
            n = (n | 1 << (31-i)) if rightBit else (n & ~(1 << (31-i)))

        return n