class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        bag = 1
        product = 1

        # left to right pass
        for i in range(len(nums)):
            result.append(product)
            product *= nums[i]

        # right to left
        for i in range(len(nums)-1,-1,-1):
            result[i] *= bag
            bag *= nums[i]


        return result