class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = defaultdict(int)

        for num in nums:
            myDict[num] += 1
        
        sortedDict = sorted(myDict, key=myDict.get, reverse = True)
        return sortedDict[:k]

        