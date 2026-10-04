class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        myDict = defaultdict(int)
        myDict[0] = 1
        res = 0
        s = 0

        for i in range(len(nums)):
            s += nums[i]
            res += myDict[s - k]
            myDict[s] += 1
        return res