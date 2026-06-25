class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = collections.Counter(nums)

        hashArr = [[i, j] for i, j in hashMap.items()]
        hashArr.sort(key = lambda x: x[1])

        res = []
        for _ in range(k):
            res.append(hashArr.pop()[0])
        return res