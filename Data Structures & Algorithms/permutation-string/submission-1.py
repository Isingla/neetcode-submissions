class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)
        s1_count = defaultdict(int)
        s2_count = defaultdict(int)

        if s1_len > s2_len:
            return False
        
        for letter in s1:
            s1_count[letter] += 1
        
        for i in range(s1_len):
            s2_count[s2[i]] += 1
        
        for i in range(1, s2_len - s1_len + 1):
            if s2_count == s1_count:
                return True
            s2_count[s2[i-1]] -= 1
            if s2_count[s2[i-1]] == 0:
                s2_count.pop(s2[i-1])
            s2_count[s2[i + s1_len - 1]] += 1
            
        return s2_count == s1_count