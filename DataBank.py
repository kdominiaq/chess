import pygame
from stockfish import Stockfish


class DataBank:
    def __init__(self):
        self.USER_MOVE = pygame.USEREVENT
        self.STOCK_FISH_MOVE = pygame.USEREVENT + 1
        self.sf = Stockfish("stockfish_13_linux_x64/stockfish_13_linux_x64")
        self.moves = []
        self.FLAG = 1



data_bank = DataBank()