class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        seen = set()
        l = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            seen.add(s[r])
            window_len = r - l + 1
            
            if window_len > best:
                best = window_len
        return best