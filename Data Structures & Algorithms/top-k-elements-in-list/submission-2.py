class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        myDict = defaultdict(int)
        n = len(nums)
        bucket = []
        for _ in range(len(nums) + 1):  
            bucket.append([])
        result = []
        
        for num in nums:
            myDict[num] += 1

        for key,val in myDict.items():
            bucket[val].append(key)
        
        for slot in bucket[::-1]:
            for num in slot:
                result.append(num)
                if len(result) == k:
                    return result
        return result