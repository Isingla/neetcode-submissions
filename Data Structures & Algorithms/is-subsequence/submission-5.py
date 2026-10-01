class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(t) < len(s):
            return False
        if len(s) == 0:
            return True
        
        sPointer = 0
        for i in range(len(t)):
            if sPointer >= len(s):
                return True
            if t[i] == s[sPointer]:
                sPointer += 1
        
        return sPointer >= len(s)
            