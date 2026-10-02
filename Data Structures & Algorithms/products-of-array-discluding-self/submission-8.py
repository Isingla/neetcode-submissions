class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        product = 1
        for num in nums:
            result.append(product)
            product *= num
        
        product = 1
        
        for i in range(len(nums)-1,-1,-1):
            result[i] *= product
            product *= nums[i]
        
        return result
        