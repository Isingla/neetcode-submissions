class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        w = i = 0

        while i < n:
            j = i
            while j < n and chars[j] == chars[i]:
                j += 1
            count = j-i
            chars[w] = chars[i]
            w += 1
            if count > 1:
                for d in str(count):
                    chars[w] = d
                    w += 1
            i = j
        return w