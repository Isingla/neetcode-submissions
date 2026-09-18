class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp = {}
        l = 0
        best = 0

        for r in range(len(s)):
            if s[r] in mp:
                l = max(mp[s[r]]+ 1, l)
            
            mp[s[r]] = r
            window_len = r - l + 1
            if window_len > best:
                best = window_len
        
        return best