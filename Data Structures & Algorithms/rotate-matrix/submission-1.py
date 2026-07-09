class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Transpose, then reverse array
        for r in range(len(matrix)):
            for c in range(0,r+1):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        for r in matrix:
            r.reverse()