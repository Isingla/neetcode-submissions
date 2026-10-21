class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_arr = [0]*26
        s2_arr = [0]*26
        matches = 0

        if len(s1) > len(s2):
            return False

        for i in range(len(s1)):
            s1_arr[ord(s1[i]) - ord('a')] += 1
            s2_arr[ord(s2[i]) - ord('a')] += 1

        for i in range(26):
            if s1_arr[i] == s2_arr[i]:
                matches += 1
        
        for i in range(1, len(s2) - len(s1) + 1):
            if matches == 26:
                return True
            leaving = ord(s2[i-1]) - ord('a')
            s2_arr[leaving] -= 1
            if s2_arr[leaving] == s1_arr[leaving]:
                matches += 1
            elif s2_arr[leaving] == s1_arr[leaving] - 1:
                matches -= 1
            
            entering = ord(s2[i + len(s1) - 1]) - ord('a')
            s2_arr[entering] += 1
            if s2_arr[entering] == s1_arr[entering]:
                matches += 1
            elif s2_arr[entering] == s1_arr[entering] + 1:
                matches -= 1

        return matches == 26