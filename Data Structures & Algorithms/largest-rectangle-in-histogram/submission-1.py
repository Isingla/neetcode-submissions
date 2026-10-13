class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        right_walls = [0] * len(heights)
        left_walls = []
        best = 0
        for i in range(len(heights)-1,-1,-1):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                right_walls[i] = stack[-1]
            else:
                right_walls[i] = len(heights)
            stack.append(i)
        
        stack = []
        for i in range(len(heights)):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            if stack:
                left_walls.append(stack[-1])
            else:
                left_walls.append(-1)
            stack.append(i)
        
        for i in range(len(heights)):
            rect = heights[i] * (right_walls[i] - left_walls[i] - 1)
            best = max(rect, best)
        return best