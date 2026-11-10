class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float('inf')

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] > nums[-1]:
                l = mid + 1
            elif nums[mid] <= nums[-1]:
                res = min(res, nums[mid])
                r = mid - 1
        return res  