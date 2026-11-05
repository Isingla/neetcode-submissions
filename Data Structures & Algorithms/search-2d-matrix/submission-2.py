class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1
        row = -1
        while t <= b:
            mid = t + (b - t) // 2
            if matrix[mid][0] > target:
                b = mid - 1
            elif matrix[mid][0] < target and matrix[mid][-1] < target:
                t = mid + 1
            else:
                row = mid
                break
        if row == -1:
            return False
        while l <= r:
            mid = l + (r - l) // 2
            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True
        return False