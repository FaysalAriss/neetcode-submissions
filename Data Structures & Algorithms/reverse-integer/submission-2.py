class Solution:
    def reverse(self, x: int) -> int:
        string = str(x) if x >= 0 else str(x)[1:]
        temp = string[::-1]
        if int(temp) > 0x7FFFFFFF:
            return 0
        if x < 0:
            return int("-"+temp)
        else:
            return int(temp)