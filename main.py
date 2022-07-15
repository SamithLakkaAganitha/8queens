from Chessboard import ChessBoard

chess = ChessBoard(8)
board = chess.create_board()
new_board = chess.play(0)
print(chess.__str__())