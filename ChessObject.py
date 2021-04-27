import pygame
from ImageDatabase import ImageDatabase


class ChessObject(pygame.sprite.Sprite, ImageDatabase):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        ImageDatabase.__init__(self)

        # define image to can  using more function from pygame.sprite.Sprite.image
        self.image = self._b_piece
        # Square bonding
        self.rect = self.image.get_rect()

    def set_position(self, dx, dy):
        """
        set position of the object (piece), top-left corner is the center of object
        :param dx: value to set
        :param dy: value to set
        :return: none
        """
        self.rect.move_ip(dx, dy)

    def remove(self):
        """
        removing object from Sprite Group
        :return: none
        """
        self.kill()


class BlackPiece(ChessObject):
    """
    set image for black piece and set position on the board by given a chess notation, like "a1'
    :return: none
    """
    def __init__(self, chess_notation):
        super().__init__()
        self.image = self._b_piece


class BlackBishop(ChessObject):
    """
    set image for black bishop and set position on the board by given a chess notation, like "a1'
    :return: none
    """
    def __init__(self, chess_notation):
        super().__init__()
        self.image = self._b_bishop


class BlackKnight(ChessObject):
    """
    set image for black Knight and set position on the board by given a chess notation, like "a1'
    :return: none
    """
    def __init__(self, chess_notation):
        super().__init__()
        self.image = self._b_knight


class BlackRook(ChessObject):
    """
    set image for black Rook and set position on the board by given a chess notation, like "a1'
    :return: none
    """
    def __init__(self, chess_notation):
        super().__init__()
        self.image = self._b_rook


class BlackQueen(ChessObject):
    """
    set image for black Queen and set position on the board by given a chess notation, like "a1'
    :return: none
    """
    def __init__(self, chess_notation):
        super().__init__()
        self.image = self._b_queen


class BlackKing(ChessObject):
    """
    set image for black King and set position on the board by given a chess notation, like "a1'
    :return: none
    """
    def __init__(self, chess_notation):
        super().__init__()
        self.image = self._b_king


class WhitePiece(ChessObject):
    """
    set image for white piece and set position on the board by given a chess notation, like "a1'
    :return: none
    """

    def __init__(self, chess_notation):
        super().__init__()
        self.image = self._w_piece


class WhiteBishop(ChessObject):
    """
    set image for white bishop and set position on the board by given a chess notation, like "a1'
    :return: none
    """

    def __init__(self, chess_notation):
        super().__init__()
        self.image = self._w_bishop


class WhiteKnight(ChessObject):
    """
    set image for white Knight and set position on the board by given a chess notation, like "a1'
    :return: none
    """

    def __init__(self, chess_notation):
        super().__init__()
        self.image = self._w_knight


class WhiteRook(ChessObject):
    """
    set image for white Rook and set position on the board by given a chess notation, like "a1'
    :return: none
    """

    def __init__(self, chess_notation):
        super().__init__()
        self.image = self._w_rook


class WhiteQueen(ChessObject):
    """
    set image for white Queen and set position on the board by given a chess notation, like "a1'
    :return: none
    """
    def __init__(self, chess_notation):
        super().__init__()
        self.image = self._w_queen


class WhiteKing(ChessObject):
    """
    set image for white King and set position on the board by given a chess notation, like "a1'
    :return: none
    """
    def __init__(self, chess_notation):
        super().__init__()
        self.image = self._w_king


class ChessBoard(ChessObject):
    """
    set image for white King and set position on the board by given a chess notation, like "a1'
    :return: none
   """
    def __init__(self):
        super().__init__()
        self.image = self._chess_board



