import pygame
from Board import Board
from Pieces import Pieces


class Screen(Board, Pieces):

    """
    set caption also stores variables for initialize window (wth and hgt)
    :return: none
    """
    def __init__(self, width, height):
        super().__init__(width,height)
        # set caption
        pygame.display.set_caption("Chess")

        # set icon
        icon = pygame.image.load('chess_png/icon.png')
        pygame.display.set_icon(icon)

        # initial screen
        self._width = width
        self._height = height
        self.screen = pygame.display.set_mode((self._width, self._height))

        # initial board
        self._chess_board = pygame.image.load('chess_png/chessboard.png')
        self._chess_board = pygame.transform.scale(self._chess_board, (self._width, self._height))

    @staticmethod
    def on():
        """
        initialize pygame
        :return: none
        """
        pygame.init()

    @staticmethod
    def update():
        """
        screen update
        :return: none
        """
        pygame.display.flip()

    @staticmethod
    def quit():
        """
        screen quit
        :return: none
        """
        pygame.display.quit()

    def display_board(self):
        """
        set board
        :return: none
        """
        self.screen.blit(self._chess_board, (0, 0))

    def init_pieces_on_board(self):
        """
        display all pieces for start the game
        :return: none
        """
        self.screen.blit(self.w_piece, self.get_xy_from_chess_notation('a2'))
        self.screen.blit(self.w_piece, self.get_xy_from_chess_notation('b2'))
        self.screen.blit(self.w_piece, self.get_xy_from_chess_notation('c2'))
        self.screen.blit(self.w_piece, self.get_xy_from_chess_notation('d2'))
        self.screen.blit(self.w_piece, self.get_xy_from_chess_notation('e2'))
        self.screen.blit(self.w_piece, self.get_xy_from_chess_notation('f2'))
        self.screen.blit(self.w_piece, self.get_xy_from_chess_notation('g2'))
        self.screen.blit(self.w_piece, self.get_xy_from_chess_notation('h2'))
        self.screen.blit(self.w_tower, self.get_xy_from_chess_notation('a1'))
        self.screen.blit(self.w_tower, self.get_xy_from_chess_notation('h1'))
        self.screen.blit(self.w_horse, self.get_xy_from_chess_notation('b1'))
        self.screen.blit(self.w_horse, self.get_xy_from_chess_notation('g1'))
        self.screen.blit(self.w_bishop, self.get_xy_from_chess_notation('c1'))
        self.screen.blit(self.w_bishop, self.get_xy_from_chess_notation('f1'))
        self.screen.blit(self.w_king, self.get_xy_from_chess_notation('e1'))
        self.screen.blit(self.w_queen, self.get_xy_from_chess_notation('d1'))

        self.screen.blit(self.b_piece, self.get_xy_from_chess_notation('a7'))
        self.screen.blit(self.b_piece, self.get_xy_from_chess_notation('b7'))
        self.screen.blit(self.b_piece, self.get_xy_from_chess_notation('c7'))
        self.screen.blit(self.b_piece, self.get_xy_from_chess_notation('d7'))
        self.screen.blit(self.b_piece, self.get_xy_from_chess_notation('e7'))
        self.screen.blit(self.b_piece, self.get_xy_from_chess_notation('f7'))
        self.screen.blit(self.b_piece, self.get_xy_from_chess_notation('g7'))
        self.screen.blit(self.b_piece, self.get_xy_from_chess_notation('h7'))
        self.screen.blit(self.b_tower, self.get_xy_from_chess_notation('a8'))
        self.screen.blit(self.b_tower, self.get_xy_from_chess_notation('h8'))
        self.screen.blit(self.b_horse, self.get_xy_from_chess_notation('b8'))
        self.screen.blit(self.b_horse, self.get_xy_from_chess_notation('g8'))
        self.screen.blit(self.b_bishop, self.get_xy_from_chess_notation('c8'))
        self.screen.blit(self.b_bishop, self.get_xy_from_chess_notation('f8'))
        self.screen.blit(self.b_king, self.get_xy_from_chess_notation('e8'))
        self.screen.blit(self.b_queen, self.get_xy_from_chess_notation('d8'))





