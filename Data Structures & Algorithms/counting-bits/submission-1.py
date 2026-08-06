class Solution:
    #0  0000
    #1  0001
    #2  0010
    #3  0011
    #4  0100
    #5  0101
    #6  0110
    #7  0111
    #8  1000
    #9  1001
    #10 1010
    #11 1011
    #12 1100
    #13 1101
    #14 1110
    #15 1111

    #When you right shift a number by 1 you are changing the number of 1s bits at most by 1, since you are only removing one bit
    #As this is a smaller number than our current we have already computed the number of 1s bits so we can simply reuse our answer
    #To take into account the removed bit we can simply isolate the last bit by masking it then adding it to our answer

    def countBits(self, n: int) -> List[int]:
        bits = [0] * (n+1) #init array size
        for i in range(n+1):
            bits[i] = bits[i>>1] + (i & 1)

        return bits