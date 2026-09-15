class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        bag = 1
        product = 1

        for num in nums:
            result.append(product)
            product *= num
        
        for i in range(len(nums)-1,-1,-1):
            result[i] *= bag
            bag *= nums[i]
        
        return result