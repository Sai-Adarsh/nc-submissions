class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = defaultdict(list)
        for each in strs:
            hashMap["".join(sorted(each))].append(each)
        return [hashMap[i] for i in hashMap]