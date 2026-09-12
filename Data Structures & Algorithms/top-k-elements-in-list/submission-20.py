class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = defaultdict(int)
        n = len(nums)
        bucket = [[] for _ in range(len(nums) + 1)]
        result = []
        
        for num in nums:
            myDict[num] += 1
        
        for val,freq in myDict.items():
            bucket[freq].append(val)
        
        for freq in range(len(bucket)-1,-1,-1):
            for num in bucket[freq]:
                result.append(num)
                if len(result) == k:
                    return result
        return result