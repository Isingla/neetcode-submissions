class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            if s[i] == " ":
                count = 0
            else:
                count += 1
                result = count
            if i == len(s)-1 and count == 0:
                return result
        return count