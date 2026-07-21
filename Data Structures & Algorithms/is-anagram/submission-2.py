class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        myDict = {}
        for char in s:
            if char in myDict:
                myDict[char]+=1
            else:
                myDict[char]=1
        for char in t:
            if char in myDict:
                myDict[char]-=1
            else:
                return False
        
        for value in myDict.values():
            if value != 0:
                return False
        return True