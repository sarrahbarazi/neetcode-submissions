class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len (matrix[0])

        topRow, botRow = 0, ROWS - 1
        while topRow <= botRow:
            row = (topRow+botRow)//2
            if target > matrix[row][-1]:
                topRow = row +1
            elif target < matrix[row][0]:
                botRow = row - 1
            else:
                break
        if not (topRow <= botRow):
            return False
        row = (topRow+botRow)//2
        l, r = 0, COLS-1
        while l<=r:
            m = (l+r)//2
            if target >matrix[row][m]:
                l = m+1
            elif target < matrix[row][m]:
                r = m - 1
            else:
                return True
        return False




