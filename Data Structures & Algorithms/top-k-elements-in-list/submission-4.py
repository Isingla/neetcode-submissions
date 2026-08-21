class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = defaultdict(int)

        result = []

        for num in nums:
            myDict[num] += 1
        
        for i in range(k):
            greatestVal = -1
            greatestKey = 0
            for key,val in myDict.items():
                if val > greatestVal:
                    greatestVal = val
                    greatestKey = key
            result.append(greatestKey)
            del myDict[greatestKey]
        
        return result
