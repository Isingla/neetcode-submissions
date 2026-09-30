class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap = defaultdict(int)

        for ch in t:
            tMap[ch] += 1

        windowMap = defaultdict(int)
        need = len(tMap.keys())
        have = 0
        bestLen = float('inf')
        windowStart = 0
        l = 0
        for r in range(len(s)):
            windowMap[s[r]] += 1

            if windowMap[s[r]] == tMap[s[r]]:
                have += 1
            
            while have == need:
                windowLen = r - l + 1

                if windowLen < bestLen:
                    bestLen = windowLen
                    windowStart = l
                windowMap[s[l]] -= 1
                if tMap[s[l]] > windowMap[s[l]]:
                    have -= 1

                l += 1

        if bestLen == float('inf'):
            return ""
        return s[windowStart : windowStart + bestLen]

