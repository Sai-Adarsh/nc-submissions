class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        s = [i for i in s]
        isNeg = False
        if s[0] == "-":
            isNeg = True
            s[:] = s[1:]
        s[:] = s[::-1]
        if isNeg:
            s[:] = ["-"] + s[:]
        s = "".join(s)
        s = int(s)
        if s < -2 ** 31 or s > (2 ** 31) - 1:
            return 0
        return s