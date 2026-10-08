class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pDict = {'}':'{', ']':'[', ')':'('}
        for p in s:
            if p == '(':
                stack.append(p)
            elif p == '{':
                stack.append(p)
            elif p == '[':
                stack.append(p)
            else:
                if stack:
                    op = stack.pop()
                    if op == pDict[p]:
                        continue
                    else:
                        return False
                else:
                    return False
        if stack:
            return False
        return True