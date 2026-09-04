class Solution:
    def maxArea(self, heights: List[int]) -> int:
        result = 0
        l,r = 0 , len(heights)-1
        while l < r:
            if heights[l] < heights[r]:
                area = heights[l] * (r-l)
                if area > result:
                    result = area
                l += 1
            else:
                area = heights[r] * (r-l)
                if area > result:
                    result = area
                r -= 1
        return result