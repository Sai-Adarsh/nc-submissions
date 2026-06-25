class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indicesMap = defaultdict(list)

        for i in range(len(nums)):
            indicesMap[nums[i]].append(i)

        nums.sort()

        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] + nums[right] > target:
                right -= 1
            elif nums[left] + nums[right] < target:
                left += 1
            else:
                return sorted([indicesMap[nums[left]].pop(0), indicesMap[nums[right]].pop(0)])
        return