class Solution:
    def covers(self, tMap: dict, windowMap: dict) -> bool:
        for ch,count in tMap.items():
            if windowMap[ch] < count:
                return False
        return True
    def minWindow(self, s: str, t: str) -> str:
        tMap = defaultdict(int)
        windowMap = defaultdict(int)
        bestLen = float('inf')
        windowStart = 0
        l = 0

        for ch in t:
            tMap[ch] += 1
        
        for r in range(len(s)):
            windowMap[s[r]] += 1
            while self.covers(tMap, windowMap):
                windowLen = r - l + 1
                if windowLen < bestLen:
                    bestLen = windowLen
                    windowStart = l
                windowMap[s[l]] -= 1
                l += 1

        if bestLen == float('inf'):
            return ""
        return s[windowStart : windowStart + bestLen]