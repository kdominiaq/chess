import pygame

from Board import Board


class Screen(Board):
    """
    set caption also stores variables for initialize window (wth and hgt)
    :return: none
    """
    def __init__(self):
        super().__init__()

        # create instantiation of board
        self.board = Board()

        # set caption
        pygame.display.set_caption("Chess")

        # set icon
        icon = pygame.image.load('chess_png/icon.png')
        pygame.display.set_icon(icon)

        # initial screen
        self._width = self.width_chess_board
        self._height = self.height_chess_board
        self._screen = pygame.display.set_mode((self._width, self._height))

    @staticmethod
    def on():
        """
        initialize pygame
        :return: none
        """
        pygame.init()

    def update(self):
        """
        screen and sprite_group update
        :return: none
        """
        self.board.update_sprites(self._screen)
        self.board.update_sprites(self._screen)
        pygame.display.flip()

    @staticmethod
    def quit():
        """
        screen quit
        :return: none
        """
        pygame.display.quit()






