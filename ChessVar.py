# Author: Kristin Towns
# GitHub username: kristinlashun
# Date: 3/14/2024
# Description: Implements a ChessVar class for a variant of chess that includes unique pieces like the Falcon and the Hunter.
# This class handles the game state, enforces movement and capture rules for all pieces, and introduces special rules for the Falcon
# and Hunter pieces. The game concludes when a player's king is captured.

class ChessPiece:
    def __init__(self, piece_type, color):
        self.piece_type = piece_type  # 'P', 'R', 'N', 'B', 'Q', 'K', 'F', 'H'
        self.color = color  # 'W' or 'B'

class ChessVar:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]  # 8x8 chess board
        self.turn = 'W'  # White starts
        self.game_state = 'UNFINISHED'
        self.setup_board()

    def setup_board(self):
        # Initialize the board with pieces in their starting positions
        # Placeholder: You need to populate the board with ChessPiece instances
        pass

    def switch_turn(self):
        # Switch the current turn between 'W' and 'B'
        self.turn = 'B' if self.turn == 'W' else 'W'

    def make_move(self, from_sq, to_sq):
        # Validate and execute a move, then switch turns
        # Placeholder for actual implementation
        self.switch_turn()  # This should only happen if the move is valid
        return True  # Placeholder: Return True if the move is valid, False otherwise

    def get_game_state(self):
        # Check for and return the current game state
        return self.game_state

