class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, (len(matrix) * len(matrix[0]) - 1)
        col_len, row_len = len(matrix), len(matrix[0])
        while l <= r:
            mid = l + (r - l) // 2
            row = mid // row_len
            col = mid % row_len
            if target > matrix[row][col]:
                l = mid + 1
            elif target < matrix[row][col]:
                r = mid - 1
            else:
                return True
        return False