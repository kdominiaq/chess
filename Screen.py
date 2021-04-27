import pygame
from Board import Board


class Screen(Board):
    """
    set caption also stores variables for initialize window (wth and hgt)
    :return: none
    """
    def __init__(self):
        super().__init__()

        # set caption
        pygame.display.set_caption("Chess")

        # set icon
        icon = pygame.image.load('chess_png/icon.png')
        pygame.display.set_icon(icon)

        # initial screen
        self._width = (self.width_chess_board * 1.25).__round__()
        self._height = self.height_chess_board
        self.screen = pygame.display.set_mode((self._width, self._height))

        # initial sprite group
        self.all_sprite = pygame.sprite.Group()

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
        self.all_sprite.draw(self.screen)
        pygame.display.flip()


    def init_board_with_pieces(self):
        """
        add board and all pieces to  all_sprite (sprite.Gruop()) for start a game
        for example: black bishop on 'c8' and 'f8'
        :return: none
        """
        # add chess board
        self.all_sprite.add(self.chess_board)
        # add all pieces
        for i in self.initial_placement:
            key = i.get('piece')
            self.all_sprite.add(key)
        # display all sprites
        self.all_sprite.draw(self.screen)

    @staticmethod
    def quit():
        """
        screen quit
        :return: none
        """
        pygame.display.quit()






