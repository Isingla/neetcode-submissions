class Solution:
    def trap(self, height: List[int]) -> int:
        maximum = 0
        ltr = []
        rtl = []
        result = 0
        for i in range(len(height)):
            ltr.append(maximum)
            if height[i] > maximum:
                maximum = height[i]

        maximum = 0

        for i in range(len(height)-1,-1,-1):
            rtl.append(maximum)
            if height[i] > maximum:
                maximum = height[i]
        rtl.reverse()

        for i in range(len(height)):
            if min(ltr[i],rtl[i]) - height[i] > 0:
                result += min(ltr[i],rtl[i]) - height[i]
        return result