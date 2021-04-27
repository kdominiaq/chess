import pygame
from Params import Params


class ImageDatabase(Params):
    def __init__(self):
        super().__init__()

        # Chess Board
        self._chess_board = pygame.image.load('chess_png/chessboard.png')
        self._chess_board = pygame.transform.scale(self._chess_board, (self.width_chess_board, self.height_chess_board))

        # Black pieces
        self._b_piece = pygame.image.load('chess_png/bP.png')
        self._b_piece = pygame.transform.scale(self._b_piece, (self.width_field, self.height_field))
        self._b_rook = pygame.image.load('chess_png/bR.png')
        self._b_rook = pygame.transform.scale(self._b_rook, (self.width_field, self.height_field))
        self._b_knight = pygame.image.load('chess_png/bN.png')
        self._b_knight = pygame.transform.scale(self._b_knight, (self.width_field, self.height_field))
        self._b_queen = pygame.image.load('chess_png/bQ.png')
        self._b_queen = pygame.transform.scale(self._b_queen, (self.width_field, self.height_field))
        self._b_bishop = pygame.image.load('chess_png/bB.png')
        self._b_bishop = pygame.transform.scale(self._b_bishop, (self.width_field, self.height_field))
        self._b_king = pygame.image.load('chess_png/bK.png')
        self._b_king = pygame.transform.scale(self._b_king, (self.width_field, self.height_field))

        # White pieces
        self._w_piece = pygame.image.load('chess_png/wP.png')
        self._w_piece = pygame.transform.scale(self._w_piece, (self.width_field, self.height_field))
        self._w_rook = pygame.image.load('chess_png/wR.png')
        self._w_rook = pygame.transform.scale(self._w_rook, (self.width_field, self.height_field))
        self._w_knight = pygame.image.load('chess_png/wN.png')
        self._w_knight = pygame.transform.scale(self._w_knight, (self.width_field, self.height_field))
        self._w_queen = pygame.image.load('chess_png/wQ.png')
        self._w_queen = pygame.transform.scale(self._w_queen, (self.width_field, self.height_field))
        self._w_bishop = pygame.image.load('chess_png/wB.png')
        self._w_bishop = pygame.transform.scale(self._w_bishop, (self.width_field, self.height_field))
        self._w_king = pygame.image.load('chess_png/wK.png')
        self._w_king = pygame.transform.scale(self._w_king, (self.width_field, self.height_field))
