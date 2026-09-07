class Solution:
    def trap(self, height: List[int]) -> int:
        result = 0
        left = 0
        right = len(height)-1
        rMax = 0
        lMax = 0
        while left <= right:
            if lMax < rMax:
                if height[left] > lMax:
                    lMax = height[left]
                else:
                    result += lMax - height[left]
                left += 1
            
            else:
                if height[right] > rMax:
                    rMax = height[right]
                else:
                    result += rMax - height[right]
                right -= 1
        return result