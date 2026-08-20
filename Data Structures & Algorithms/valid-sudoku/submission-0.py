class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        #checking rows for dupes
        for r in range(len(board)):
            filtered = []
            for c in range(len(board[r])):
                if board[r][c] != ".":
                    filtered.append(board[r][c])
            if len(filtered) != len(set(filtered)):
                return False
            
        #checking cols for dupes
        for r in range(len(board)):
            filtered = []
            for c in range(len(board[r])):
                if board[c][r] != ".":
                    filtered.append(board[c][r])
            if len(filtered) != len(set(filtered)):
                return False
        
        #checking 3x3 mini squares
        for rOuter in range(0,len(board),3):
            for cOuter in range(0,len(board),3):
                filtered = []
                for rInner in range(rOuter,rOuter+3):
                    for cInner in range(cOuter,cOuter+3):
                        if board[rInner][cInner] != ".":
                            filtered.append(board[rInner][cInner])
                if len(filtered) != len(set(filtered)):
                    return False
            
        return True
