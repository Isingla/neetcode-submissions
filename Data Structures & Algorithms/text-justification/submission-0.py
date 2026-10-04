class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        i = 0
        while i < len(words):
            line_len = 0
            line = []
            word_count = 0
            letter_count = 0
            while i < len(words) and line_len <= maxWidth:
                if word_count > 0:
                    space = 1
                else:
                    space = 0
                if line_len + len(words[i]) + space <= maxWidth:
                    line_len += space
                    line_len += len(words[i])
                    word_count += 1
                    line.append(words[i])
                    i += 1
                else:
                    break

            for word in line:
                for letter in word:
                    letter_count += 1
            
            total_spaces = maxWidth - letter_count
            gap_count = len(line) - 1
            if i == len(words) or gap_count == 0:
                s = " ".join(line)
                s += (maxWidth - len(s)) * " "
            else:
                base = total_spaces // gap_count
                extra = total_spaces % gap_count
                s = ""

                for g in range(gap_count):
                    s += line[g]
                    if g < extra:
                        s += " " * (base + 1)
                    else:
                        s += " " * base 
                s += line[-1]
            res.append(s)
        return res