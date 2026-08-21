class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            l = str(len(word))
            l += "#"
            encoded += (l + word)
        return encoded

    def decode(self, s: str) -> List[str]:
        i = 0
        decoded = []
        while i < len(s):
            l = ""
            word = ""
            while s[i] != "#":
                l += (s[i])
                i += 1
            l = int(l)
        
            for j in range(l):
                word += s[i+j+1]
            decoded.append(word)
            i += l + 1
        return decoded

