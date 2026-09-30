class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = defaultdict(int)
        tDict = defaultdict(int)
        for ch in s:
            sDict[ch] += 1
        for ch in t:
            tDict[ch] += 1
        return sDict == tDict