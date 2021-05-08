"""
Module inherits values of width/height field and board also image folder path. It is responsibly for load image to
pygame.image and transform of pieces by variables from Params.

Code using this module has to handle following exceptions:
FileNotFoundError: Invalid name of image or call to non-existing image. Exit code 1.
"""

import pygame
import os
from Params import Params


class ImageDatabase(Params):
    def __init__(self):
        super().__init__()

        try:
            # Chess Board
            self._chess_board = pygame.image.load(os.path.join(self.image_folder, 'chessboard.png'))

            # Black pieces
            self._b_piece = pygame.image.load(os.path.join(self.image_folder, 'bP.png'))
            self._b_rook = pygame.image.load(os.path.join(self.image_folder, 'bR.png'))
            self._b_knight = pygame.image.load(os.path.join(self.image_folder, 'bN.png'))
            self._b_queen = pygame.image.load(os.path.join(self.image_folder, 'bQ.png'))
            self._b_bishop = pygame.image.load(os.path.join(self.image_folder, 'bB.png'))
            self._b_king = pygame.image.load(os.path.join(self.image_folder, 'bK.png'))

            # White pieces
            self._w_piece = pygame.image.load(os.path.join(self.image_folder, 'wP.png'))
            self._w_rook = pygame.image.load(os.path.join(self.image_folder, 'wR.png'))
            self._w_knight = pygame.image.load(os.path.join(self.image_folder, 'wN.png'))
            self._w_queen = pygame.image.load(os.path.join(self.image_folder, 'wQ.png'))
            self._w_bishop = pygame.image.load(os.path.join(self.image_folder, 'wB.png'))
            self._w_king = pygame.image.load(os.path.join(self.image_folder, 'wK.png'))
        except FileNotFoundError as exc:
            print(f"Invalid name of image or call to non-existing image:  {exc}")
            exit(1)

        # Chess Board transform
        self._chess_board = pygame.transform.scale(self._chess_board, (self.width_chess_board, self.height_chess_board))

        # Black pieces transform
        self._b_piece = pygame.transform.scale(self._b_piece, (self.width_field, self.height_field))
        self._b_rook = pygame.transform.scale(self._b_rook, (self.width_field, self.height_field))
        self._b_knight = pygame.transform.scale(self._b_knight, (self.width_field, self.height_field))
        self._b_queen = pygame.transform.scale(self._b_queen, (self.width_field, self.height_field))
        self._b_bishop = pygame.transform.scale(self._b_bishop, (self.width_field, self.height_field))
        self._b_king = pygame.transform.scale(self._b_king, (self.width_field, self.height_field))

        # White pieces transform
        self._w_piece = pygame.transform.scale(self._w_piece, (self.width_field, self.height_field))
        self._w_rook = pygame.transform.scale(self._w_rook, (self.width_field, self.height_field))
        self._w_knight = pygame.transform.scale(self._w_knight, (self.width_field, self.height_field))
        self._w_queen = pygame.transform.scale(self._w_queen, (self.width_field, self.height_field))
        self._w_bishop = pygame.transform.scale(self._w_bishop, (self.width_field, self.height_field))
        self._w_king = pygame.transform.scale(self._w_king, (self.width_field, self.height_field))


