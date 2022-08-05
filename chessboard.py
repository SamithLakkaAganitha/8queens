import logging

class ChessBoard:

    # Constructor
    def __init__(self, N):
        # Construction argument
        self.N = N
        # Creation of board
        self.board = [[0] * self.N for i in range(self.N)]

    # Place queen method
    def place_queen(self, row, col):
        self.board[row][col] = 1

    #Remove queen method
    def remove_queen(self, ind, col):
        self.board[ind][col] = 0

    #Check if queen is safe method
    def is_safe(self, row, col):
        for i in range(col):
            # print('I',i)
            # print('row',row)
            # print('col',col)
            if self.board[row][i] == 1:
                logging.error('ErrorRow')
                return False
 
            if row - i >= 0:
                # upleft
                if self.board[row - (i + 1)][col - (i + 1)] == 1:
                    logging.error('ErrorUp')
                    return False

            if row + i < self.N:
                # downleft
                if self.board[row + i][col - i] == 1:
                    logging.error('ErrorDown')
                    return False

        return True

    #Places queen when its safe or removes queen when its not safe method
    def play(self, col):

        if col >= self.N:
            return True

        for i in range(self.N):
            # print('ROW',i)
            # print('COL',col)

            if self.is_safe(i, col):
                # print('SAFE')
                self.place_queen(i, col)

                if self.play(col + 1) == True:
                    return True

                self.remove_queen(i, col)

        return False

    # String representation of board
    def __str__(self):
        res = ""
        for row in self.board:
            res += str(row) + "\n"
        return res
