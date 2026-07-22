class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = defaultdict(list)
        for word in strs:
            myArray = [0] * 26
            for char in word:
                myArray[ord(char) - ord('a')] += 1
            key = tuple(myArray)
            myDict[key].append(word)
        return list(myDict.values())
        