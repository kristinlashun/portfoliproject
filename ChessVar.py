# Author: Kristin Towns
# GitHub username: kristinlashun
# Date: 3/14/2024
# Description: This file contains the implementation of a class named ChessVar for playing an abstract board game
# that is a variant of chess, incorporating unique pieces like the Falcon and the Hunter. The class manages the game state,
# enforces the rules of movement and capture for all pieces, and introduces special rules for entering the Falcon and Hunter pieces
# into the game. The game ends when a player's king is captured, determining the winner.

class ChessPiece:
    def __init__(self, piece_type, color):
        self.piece_type = piece_type  # 'P', 'R', 'N', 'B', 'Q', 'K', 'F', 'H'
        self.color = color  # 'W' or 'B'

class ChessVar:
    def __init__(self):
        self.board = self.setup_board()
        self.turn = 'W'  # White starts
        self.game_state = 'UNFINISHED'
        self.lost_pieces = {'W': [], 'B': []}  # Track lost pieces to determine fairy piece eligibility
    
    def setup_board(self):
        # Initialize and return the initial board setup as a 2D list
        pass
    
    def make_move(self, from_sq, to_sq):
        # Check if the move is valid and execute it
        return False  # Placeholder
    
    def enter_fairy_piece(self, piece_type, position):
        # Check if a fairy piece can be entered and execute it
        return False  # Placeholder
    
    def get_game_state(self):
        return self.game_state