class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # one pass

        rows = [set() for _ in range(9)] # 9 rows
        cols = [set() for _ in range(9)] # 9 cols
        boxes = [set() for _ in range(9)] # 9 boxes

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == ".":
                    continue
                
                box = (r//3) * 3 + (c//3) # boxes 0 -> 8

                if (val in rows[r]) or (val in cols[c]) or (val in boxes[box]):
                    return False
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box].add(val)
        return True
