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

    #When the number becomes a power of 2 the number of 1's is just 1
    #To get to the next power of two the sequence of everything before it repeats on the right of that new 1
    #As in for 4 to get to 8 it will go through the sequence of 0-3 for the bits to the right of the 3rd
    #So if you ignore the 3rd bit 4-7 looks like 0-3, meaning 4-7 as the same amount of 1s as 0-3 except +1
    #For 8 to get to 15 it needs to double so needs to through everything before it so 0-7, repeating the same pattern, again just with +1 1s
    #So to get the number of bits in 9 we can take the closest power of 2 which is 8, get the number of 1's in 9-8 and add 1 to it
    #We can keep track of this closest power of 2 (the offset) when we reach a new power of 2

    def countBits(self, n: int) -> List[int]:
        bits = [0] * (n+1) #init array size
        offset = 1 #minimum offset 2^0 = 1
        for i in range(1, n+1):
            if offset * 2 == i: #check if we're at a new power of 2
                offset *= 2
            bits[i] = bits[i-offset] + 1
            

        return bits