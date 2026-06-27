class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        hashMap = {}
        for _ in nums:
            hashMap[_] = _
        
        for _ in range(0, len(nums) + 1):
            if _ not in hashMap:
                return _