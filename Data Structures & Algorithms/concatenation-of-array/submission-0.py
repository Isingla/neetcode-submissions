class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)*2
        for i in range(len(nums)*2):
            if i >= len(nums):
                ans[i] = nums[i - len(nums)]
            else:
                ans[i] = nums[i]
        return ans
