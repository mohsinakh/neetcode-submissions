class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                if board[row][col]==".":
                    continue

                if board[row][col] in rows[row]:
                    return False
                
                if board[row][col] in cols[col]:
                    return False

                box = (row//3) * 3 + col//3

                if board[row][col] in boxs[box]:
                    return False

                rows[row].add(board[row][col])
                cols[col].add(board[row][col])
                boxs[box].add(board[row][col])
        return True