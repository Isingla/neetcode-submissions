class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        count = 1
        longest = 1
        nums = sorted(nums)

        if len(nums) == 0:
            return 0
        last = nums[0]

        for i in range(1, len(nums)):
            if last + 1 == nums[i]:
                count += 1
                last = nums[i]
                if count > longest:
                    longest = count
            elif last == nums[i]:
                continue
            else:
                count = 1
                last = nums[i]
        return longest
