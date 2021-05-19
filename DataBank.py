import pygame
from stockfish import Stockfish


class DataBank:
    def __init__(self):
        self.USER_MOVE = pygame.USEREVENT
        self.STOCK_FISH_MOVE = pygame.USEREVENT + 1
        self.DRAW = pygame.USEREVENT + 2
        self.sf = Stockfish("stockfish_13_linux_x64/stockfish_13_linux_x64")
        self.FLAG = 1
        self.moves = []

        # initial sprite group
        self.board_sprite = pygame.sprite.GroupSingle()
        self.all_sprite = pygame.sprite.Group()



data_bank = DataBank()