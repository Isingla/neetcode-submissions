class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 1
        l = 0
        freqM = defaultdict(int)
        n = len(s)
        top_count = 0

        for r in range(n):
            freqM[s[r]] += 1
            top_count = max(top_count, freqM[s[r]])
            while (r-l+1) - top_count > k:
                freqM[s[l]] -= 1
                l += 1

            best = max(best, r-l+1)
        return best
            