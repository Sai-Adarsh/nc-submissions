class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for _ in range(n + 1):
            res.append(bin(_).count("1"))
        return res