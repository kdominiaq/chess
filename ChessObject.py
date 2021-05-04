import pygame
from ImageDatabase import ImageDatabase


class ChessObject(pygame.sprite.Sprite, ImageDatabase):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        ImageDatabase.__init__(self)

    def set_position(self, dx, dy):
        """
        set position of the object (piece), top-left corner is the center of object
        :param dx: value to set
        :param dy: value to set
        :return: none
        """
        self.rect.x =dx
        self.rect.y =dy

    def remove(self):
        """
        removing object from Sprite Group
        :return: none
        """
        self.kill()

    def update(self, *args, **kwargs):
        if len(args) == 2:
            self.set_position(args[0], args[1])


class BlackPiece(ChessObject):
    """
    set image for black piece and set position on the board by given a chess notation, like "a1'
    :return: none
    """
    def __init__(self, xy_notation=(0, 0)):
        super().__init__()
        self.image = self._b_piece
        self.rect = self.image.get_rect()
        self.rect.move_ip(xy_notation[0], xy_notation[1])


class BlackBishop(ChessObject):
    """
    set image for black bishop and set position on the board by given a chess notation, like "a1'
    :return: none
    """
    def __init__(self, xy_notation=(0, 0)):
        super().__init__()
        self.image = self._b_bishop
        self.rect = self.image.get_rect()
        self.rect.move_ip(xy_notation[0], xy_notation[1])


class BlackKnight(ChessObject):
    """
    set image for black Knight and set position on the board by given a chess notation, like "a1'
    :return: none
    """
    def __init__(self, xy_notation=(0, 0)):
        super().__init__()
        self.image = self._b_knight
        self.rect = self.image.get_rect()
        self.rect.move_ip(xy_notation[0], xy_notation[1])


class BlackRook(ChessObject):
    """
    set image for black Rook and set position on the board by given a chess notation, like "a1'
    :return: none
    """
    def __init__(self, xy_notation=(0, 0)):
        super().__init__()
        self.image = self._b_rook
        self.rect = self.image.get_rect()
        self.rect.move_ip(xy_notation[0], xy_notation[1])


class BlackQueen(ChessObject):
    """
    set image for black Queen and set position on the board by given a chess notation, like "a1'
    :return: none
    """
    def __init__(self, xy_notation=(0, 0)):
        super().__init__()
        self.image = self._b_queen
        self.rect = self.image.get_rect()
        self.rect.move_ip(xy_notation[0], xy_notation[1])


class BlackKing(ChessObject):
    """
    set image for black King and set position on the board by given a chess notation, like "a1'
    :return: none
    """
    def __init__(self, xy_notation=(0, 0)):
        super().__init__()
        self.image = self._b_king
        self.rect = self.image.get_rect()
        self.rect.move_ip(xy_notation[0], xy_notation[1])


class WhitePiece(ChessObject):
    """
    set image for white piece and set position on the board by given a chess notation, like "a1'
    :return: none
    """
    def __init__(self, xy_notation=(0, 0)):
        super().__init__()
        self.image = self._w_piece
        self.rect = self.image.get_rect()
        self.rect.move_ip(xy_notation[0], xy_notation[1])


class WhiteBishop(ChessObject):
    """
    set image for white bishop and set position on the board by given a chess notation, like "a1'
    :return: none
    """
    def __init__(self, xy_notation=(0, 0)):
        super().__init__()
        self.image = self._w_bishop
        self.rect = self.image.get_rect()
        self.rect.move_ip(xy_notation[0], xy_notation[1])


class WhiteKnight(ChessObject):
    """
    set image for white Knight and set position on the board by given a chess notation, like "a1'
    :return: none
    """
    def __init__(self, xy_notation=(0, 0)):
        super().__init__()
        self.image = self._w_knight
        self.rect = self.image.get_rect()
        self.rect.move_ip(xy_notation[0], xy_notation[1])


class WhiteRook(ChessObject):
    """
    set image for white Rook and set position on the board by given a chess notation, like "a1'
    :return: none
    """
    def __init__(self, xy_notation=(0, 0)):
        super().__init__()
        self.image = self._w_rook
        self.rect = self.image.get_rect()
        self.rect.move_ip(xy_notation[0], xy_notation[1])


class WhiteQueen(ChessObject):
    """
    set image for white Queen and set position on the board by given a chess notation, like "a1'
    :return: none
    """
    def __init__(self, xy_notation=(0, 0)):
        super().__init__()
        self.image = self._w_queen
        self.rect = self.image.get_rect()
        self.rect.move_ip(xy_notation[0], xy_notation[1])


class WhiteKing(ChessObject):
    """
    set image for white King and set position on the board by given a chess notation, like "a1'
    :return: none
    """
    def __init__(self, xy_notation=(0, 0)):
        super().__init__()
        self.image = self._w_king
        self.rect = self.image.get_rect()
        self.rect.move_ip(xy_notation[0], xy_notation[1])


class ChessBoard(ChessObject):
    """
    set image for white King and set position on the board by given a chess notation, like "a1'
    :return: none
   """
    def __init__(self):
        super().__init__()
        self.image = self._chess_board
        self.rect =  self.image.get_rect()



