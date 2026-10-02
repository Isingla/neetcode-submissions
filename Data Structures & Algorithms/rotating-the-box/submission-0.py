class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        rows = len(boxGrid)
        cols = len(boxGrid[0])
        result = [["."] * rows for _ in range(cols)]

        for r in range(len(boxGrid)):
            empty = len(boxGrid[0]) - 1
            for c in range(len(boxGrid[0])-1,-1,-1):
                if boxGrid[r][c] == "*":
                    empty = c - 1
                elif boxGrid[r][c] == "#":
                    boxGrid[r][c] = "."
                    boxGrid[r][empty] = "#"
                    empty -= 1

        for r in range(len(boxGrid)):
            for c in range(len(boxGrid[0])):
                result[c][rows - r - 1] = boxGrid[r][c]
        return result