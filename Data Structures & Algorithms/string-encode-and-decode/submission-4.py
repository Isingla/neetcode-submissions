class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_words = []
        for word in strs:
            l = str(len(word))
            l+= "#"
            part = l + word
            encoded_words.append(part)
        encoded = "".join(encoded_words)
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
            
            word = s[i+1: i+l+1]
            decoded.append(word)
            i += l+1
        return decoded
