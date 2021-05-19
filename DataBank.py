import pygame
from stockfish import Stockfish


class DataBank(object):
    _moves = []
    # initial sprite group
    _board_sprite = pygame.sprite.GroupSingle(None)
    _all_sprite = pygame.sprite.Group()

    def __init__(self):
        self.USER_MOVE = pygame.USEREVENT
        self.STOCK_FISH_MOVE = pygame.USEREVENT + 1
        self.DRAW = pygame.USEREVENT + 2
        self.sf = Stockfish("stockfish_13_linux_x64/stockfish_13_linux_x64")
        self.FLAG = 1
"""
    @property
    def all_sprite(self):
        return self._all_sprite

    @property
    def moves(self):
        return self._moves



"""



