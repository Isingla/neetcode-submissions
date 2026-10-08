class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pDict = {'}': '{', ']': '[', ')': '('}
        for p in s:
            if p not in pDict:
                stack.append(p)
            elif not stack or stack.pop() != pDict[p]:
                return False
        return not stack