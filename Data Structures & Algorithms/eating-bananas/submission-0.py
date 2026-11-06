class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        best = 0
        l, r = max(1, sum(piles) // h), max(piles)

        while l <= r:
            mid = l + (r - l) // 2
            total = 0

            for pile in piles:
                total += pile // mid
                if pile % mid > 0:
                    total += 1

            if total <= h:
                r = mid - 1
                best = mid
            else:
                l = mid + 1
        return best