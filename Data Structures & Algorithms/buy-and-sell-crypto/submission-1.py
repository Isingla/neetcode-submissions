class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        for b in range(len(prices)):
            for s in range(b+1,len(prices)):
                if prices[s] - prices[b] > best:
                    best = prices[s] - prices[b]
        return best