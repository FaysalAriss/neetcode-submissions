class Solution:
    def getSum(self, a: int, b: int) -> int:
        carry = 0
        total = 0
        i = 0
        for i in range(11): #given constraint, max number of bits is 10, and 1 extra for the carry
            bitA = (a >> i) & 1
            bitB = (b >> i) & 1
            nextBit = bitA ^ bitB ^ carry
            carry = (bitA and bitB) or (carry and bitA ^ bitB)
            total = (total | 1 << i) if nextBit else (total & ~(1 << i))

        #if negative result
        if((a < 0 and abs(a) > b) or (b < 0 and abs(b) > a)):
            total |= (-1 << 11)

        return total