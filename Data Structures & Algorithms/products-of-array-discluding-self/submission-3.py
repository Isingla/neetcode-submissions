class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        leftRight = []
        rightLeft = []
        product = 1

        # left to right pass
        for i in range(len(nums)):
            leftRight.append(product)
            product *= nums[i]

        product = 1

        # right to left
        for i in range(len(nums)-1,-1,-1):
            rightLeft.append(product)
            product *= nums[i]

        rightLeft.reverse()

        for i in range(len(nums)):
            result.append(leftRight[i] * rightLeft[i])

        return result