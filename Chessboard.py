class ChessBoard:

    def __init__(self, N):
        self.N = N

    def create_board(self):
        global board
        # board = [[0] * self.N] * self.N
        board = []
        for i in range(self.N):
            row = []
            for j in range(self.N):
                row.append(0)
            board.append(row)
        return board

    def place_queen(self, row, col):
        board[row][col] = 1

    def remove_queen(self, ind, col):
        board[ind][col] = 0

    def is_safe(self, row, col):
        checked = ""

        for i in range(len(board)):
            # check row
            if board[row][i] != 1:
                checked = True
            else:
                checked = False
                break

            # check col
            if board[i][col] != 1:
                checked = True
            else:
                checked = False
                break

            # check right down diag
            if col + i < len(board) - 2 and row + i < len(board) - 2:
                if board[row + i][col + i] != 1:
                    checked = True
                else:
                    checked = False
                    break

            # check left up diag
            if board[row - i][col - i] != 1 or row - i < 0 or col - i < 0:
                checked = True
            else:
                checked = False
                break

            # check left down diag
            if row + i < len(board) - 2:
                if (board[row + i][col - i] != 1 or col - i < 0):
                    checked = True
                else:
                    checked = False
                    break

            # check right up diag
            if col + i < len(board) - 2:
                if (board[row - i][col + i] != 1 or row - i < 0):
                    checked = True
                else:
                    checked = False
                    break
        return checked

    def play(self, col):
        if col >= self.N:
            return True
        # Consider this column and try placing
        # this queen in all rows one by one
        for i in range(self.N):
            if self.is_safe(i, col):
                # Place this queen in board[i][col]
                board[i][col] = 1

                # recur to place rest of the queens
                if self.play(col + 1) == True:
                    return True

                # If placing queen in board[i][col
                # doesn't lead to a solution, then
                # queen from board[i][col]
                board[i][col] = 0

        # if the queen can not be placed in any row in
        # this column col  then return false
        return False

    def __str__(self):
        res = ""
        for row in board:
            res += str(row) + "\n"
        return res