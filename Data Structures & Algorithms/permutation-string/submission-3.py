class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_dict = defaultdict(int)
        s2_dict = defaultdict(int)
        l = 0

        for ch in s1:
            s1_dict[ch] += 1
        
        for r in range(len(s2)):
            s2_dict[s2[r]] += 1

            while l <= r and r - l + 1 == len(s1):
                if s1_dict == s2_dict:
                    return True
                s2_dict[s2[l]] -= 1
                if s2_dict[s2[l]] == 0:
                    s2_dict.pop(s2[l])
                l+= 1
        return False