class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_arr = [0] * 26
        s2_arr = [0] * 26

        for i in range(len(s1)):
            s1_arr[ord(s1[i]) - ord('a')] += 1
            s2_arr[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1_arr[i] == s2_arr[i]:
                matches += 1
        
        for i in range(1,len(s2) - len(s1) + 1):
            if matches == 26:
                return True

            leaving_letter = ord(s2[i-1]) - ord('a')
            s2_arr[leaving_letter] -= 1
            if s1_arr[leaving_letter] == s2_arr[leaving_letter]:
                matches += 1
            elif s1_arr[leaving_letter] - 1 == s2_arr[leaving_letter]:
                matches -= 1

            entering_letter = ord(s2[i + len(s1) - 1]) - ord('a')
            s2_arr[entering_letter] += 1
            if s1_arr[entering_letter] == s2_arr[entering_letter]:
                matches += 1
            elif s1_arr[entering_letter] + 1 == s2_arr[entering_letter]:
                matches -= 1

        return matches == 26
            