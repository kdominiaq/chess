import pygame


class Pieces:

    def __init__(self, width_board=100, height_board=100):

        self._width_piece = int(width_board * 1.0 / 8)
        self._height_piece = int(height_board * 1.0 / 8)

        self.b_piece = pygame.image.load('chess_png/bP.png')
        self.b_piece = pygame.transform.scale(self.b_piece, (self._width_piece, self._height_piece))
        self.b_tower = pygame.image.load('chess_png/bR.png')
        self.b_tower = pygame.transform.scale(self.b_tower, (self._width_piece, self._height_piece))
        self.b_horse = pygame.image.load('chess_png/bN.png')
        self.b_horse = pygame.transform.scale(self.b_horse, (self._width_piece, self._height_piece))
        self.b_queen = pygame.image.load('chess_png/bQ.png')
        self.b_queen = pygame.transform.scale(self.b_queen, (self._width_piece, self._height_piece))
        self.b_bishop = pygame.image.load('chess_png/bB.png')
        self.b_bishop = pygame.transform.scale(self.b_bishop, (self._width_piece, self._height_piece))
        self.b_king = pygame.image.load('chess_png/bK.png')
        self.b_king = pygame.transform.scale(self.b_king, (self._width_piece, self._height_piece))

        self.w_piece = pygame.image.load('chess_png/wP.png')
        self.w_piece = pygame.transform.scale(self.w_piece, (self._width_piece, self._height_piece))
        self.w_tower = pygame.image.load('chess_png/wR.png')
        self.w_tower = pygame.transform.scale(self.w_tower, (self._width_piece, self._height_piece))
        self.w_horse = pygame.image.load('chess_png/wN.png')
        self.w_horse = pygame.transform.scale(self.w_horse, (self._width_piece, self._height_piece))
        self.w_queen = pygame.image.load('chess_png/wQ.png')
        self.w_queen = pygame.transform.scale(self.w_queen, (self._width_piece, self._height_piece))
        self.w_bishop = pygame.image.load('chess_png/wB.png')
        self.w_bishop = pygame.transform.scale(self.w_bishop, (self._width_piece, self._height_piece))
        self.w_king = pygame.image.load('chess_png/wK.png')
        self.w_king = pygame.transform.scale(self.w_king, (self._width_piece, self._height_piece))

