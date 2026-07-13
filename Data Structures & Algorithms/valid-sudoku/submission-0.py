class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ## A board is a 2D array
        valid_nums = [str(i) for i in range(1,10)]
        # Check if row have dupes; row by row
        for row in range(9):
            seen = set()
            for col in range(9):
                num = board[row][col]
                if (num in seen):
                    return False
                elif num == ".":
                    continue
                else:
                    seen.add(num)
        # Check if cols have dupes
        for col in range(9):
            seen = set()
            for row in range(9):
                num = board[row][col]
                if (num in seen):
                    return False
                elif num == ".":
                    continue
                else:
                    seen.add(num)

        # Check if any 3x3 sub boxes have dupes
        for row_box in range(0,6,3):
            for col_box in range(0,6,3):
                print(row_box,col_box)
                seen = set()
                for row in range(row_box, row_box+3):
                    for col in range(col_box, col_box+3):
                        num = board[row][col]
                        if (num in seen):
                            return False
                        elif num == ".":
                            continue
                        else:
                            seen.add(num)

        return True





