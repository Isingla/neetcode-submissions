class Solution:
    def minWindow(self, s: str, t: str) -> str:
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)
        best_len = float('inf')
        l = 0
        window_start = 0

        for ch in t:
            t_dict[ch] += 1
        
        need = len(t_dict.keys())
        have = 0
        
        for r in range(len(s)):
            s_dict[s[r]] += 1

            if s_dict[s[r]] == t_dict[s[r]]:
                have += 1
            
            while have == need:
                window_len = r-l+1
                if window_len < best_len:
                    best_len = window_len
                    window_start = l
                s_dict[s[l]] -= 1

                if t_dict[s[l]] > s_dict[s[l]]:
                    have -= 1
                l += 1
        if best_len == float('inf'):
            return ""
        return s[window_start : window_start + best_len]
                
                
                