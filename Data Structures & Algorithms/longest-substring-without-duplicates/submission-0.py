class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        inString = set()
        l = 0

        for r in range(len(s)):
            while s[r] in inString:
                inString.remove(s[l])
                l += 1
            inString.add(s[r])
            window_len = r - l + 1
            if window_len > best:
                best = window_len
        return best