from ChessObject import *


class Screen(ChessBoard, BlackPiece):
    """
    set caption also stores variables for initialize window (wth and hgt)
    :return: none
    """

    def __init__(self, width, height):

        ChessObject.__init__(self)
        # set caption
        pygame.display.set_caption("Chess")

        # set icon
        icon = pygame.image.load('chess_png/icon.png')
        pygame.display.set_icon(icon)

        # initial screen
        self._width = width
        self._height = height
        self.screen = pygame.display.set_mode((self._width, self._height))


        a = BlackPiece('a1')

        # initial sprite group
        self.all_sprite = pygame.sprite.Group()
        self.all_sprite.add(a)
        self.all_sprite.draw(self.screen)

    @staticmethod
    def on():
        """
        initialize pygame
        :return: none
        """
        pygame.init()

    def update(self):
        """
        screen update
        :return: none
        """
        self.all_sprite.update()
        pygame.display.flip()

    def init_board_with_pieces(self):
        """
        add board and all pieces to  all_sprite (sprite.Gruop()) for start a game
        for example: black bishop on 'c8' and 'f8'
        :return: none
        """

    @staticmethod
    def quit():
        """
        screen quit
        :return: none
        """
        pygame.display.quit()

    def init_pieces_on_board(self):
        """
        display all pieces for start the game
        :return: none
        """

        """
        self.screen.blit(self._w_piece, self.get_xy_from_chess_notation('b2'))
        self.screen.blit(self._w_piece, self.get_xy_from_chess_notation('c2'))
        self.screen.blit(self._w_piece, self.get_xy_from_chess_notation('d2'))
        self.screen.blit(self._w_piece, self.get_xy_from_chess_notation('e2'))
        self.screen.blit(self._w_piece, self.get_xy_from_chess_notation('f2'))
        self.screen.blit(self._w_piece, self.get_xy_from_chess_notation('g2'))
        self.screen.blit(self._w_piece, self.get_xy_from_chess_notation('h2'))
        self.screen.blit(self._w_tower, self.get_xy_from_chess_notation('a1'))
        self.screen.blit(self._w_tower, self.get_xy_from_chess_notation('h1'))
        self.screen.blit(self._w_horse, self.get_xy_from_chess_notation('b1'))
        self.screen.blit(self._w_horse, self.get_xy_from_chess_notation('g1'))
        self.screen.blit(self._w_bishop, self.get_xy_from_chess_notation('c1'))
        self.screen.blit(self._w_bishop, self.get_xy_from_chess_notation('f1'))
        self.screen.blit(self._w_king, self.get_xy_from_chess_notation('e1'))
        self.screen.blit(self._w_queen, self.get_xy_from_chess_notation('d1'))

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
        """




