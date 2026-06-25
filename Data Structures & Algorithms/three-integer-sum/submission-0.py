class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []

        for i in range(len(nums)):
            complement = -nums[i]
            left = i + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] > complement:
                    right -= 1
                elif nums[left] + nums[right] < complement:
                    left += 1
                else:
                    temp = sorted([nums[i], nums[left], nums[right]])
                    if temp not in res:
                        res.append(temp)
                    left += 1
                    right -= 1
        return res