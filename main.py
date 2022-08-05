from chessboard import ChessBoard
import logging

chess = ChessBoard(8)
new_board = chess.play(0)
logging.info(chess)
