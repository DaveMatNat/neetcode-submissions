class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ## A board is a 2D array
        # Check if row have dupes; row by row
        for row in range(9):
            seen = set()
            for col in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                if num in seen:
                    return False
                seen.add(num)
        # Check if cols have dupes
        for col in range(9):
            seen = set()
            for row in range(9):
                num = board[row][col]
                if num == ".":
                    continue
                if num in seen:
                    return False
                seen.add(num)

        # Check if any 3x3 sub boxes have dupes
        for row_box in range(0,9,3):
            for col_box in range(0,9,3):
                seen = set()
                for row in range(row_box, row_box+3):
                    for col in range(col_box, col_box+3):
                        num = board[row][col]
                        if num == ".":
                            continue
                        if num in seen:
                            return False
                        seen.add(num)

        return True
