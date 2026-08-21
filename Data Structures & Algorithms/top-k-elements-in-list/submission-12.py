class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = defaultdict(int)
        result = []

        for num in nums:
            myDict[num] += 1

        sortedList = sorted(myDict.items(), reverse = True, key = lambda pair: pair[1])
        for i in range(k):
            result.append(sortedList[i][0])
        return result
        