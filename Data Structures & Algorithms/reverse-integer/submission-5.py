class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        x = abs(x)
        out = 0
        while x > 0:
            out *= 10
            out += x % 10
            x = int(x/10)
        
        if negative:
            out *= -1

        return out if abs(out) <= 0x7FFFFFFF else 0