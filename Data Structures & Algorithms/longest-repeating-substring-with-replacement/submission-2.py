class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        best = 1
        l = 0
        freqM = defaultdict(int)
        n = len(s)

        for r in range(n):
            freqM[s[r]] += 1
            while (r-l+1) - max(freqM.values()) > k:
                freqM[s[l]] -= 1
                l += 1
            best = max(r-l+1, best)
        return best