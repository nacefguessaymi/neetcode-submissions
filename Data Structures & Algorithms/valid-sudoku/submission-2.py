class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_t = [list(i) for i in zip(*board)]
        board_b = [[board[r][c] for r in range(br, br + 3) for c in range(bc, bc + 3)] for br in range(0, 9, 3) for bc in range(0, 9, 3)]
        for i, row in enumerate(board):
            list_row = sorted([j for j in row if j != "."])
            set_row = set(list_row)
            list_col = sorted([j for j in board_t[i] if j !="."])
            set_col = set(list_col)
            if sorted(list(set_row)) != list_row:
                return False
            if sorted(list(set_col)) != list_col:
                return False
        for b in board_b:
            list_b = sorted([j for j in b if j !="."])
            set_b = set(list_b)
            if sorted(list(set_b)) != list_b:
                return False
        return True