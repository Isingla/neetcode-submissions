class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        colDict = defaultdict(set)
        cubeDict = defaultdict(set)

        for r in range(len(board)):
            filteredRow = set()
            for c in range(len(board[r])):
                if board[r][c] != ".":
                    if (
                        board[r][c] in filteredRow
                        or board[r][c] in colDict[c]
                        or board[r][c] in cubeDict[r//3, c // 3]
                    ):
                        return False
                    else:
                        filteredRow.add(board[r][c])
                        colDict[c].add(board[r][c])
                        cubeDict[r // 3, c // 3].add(board[r][c])

        return True
