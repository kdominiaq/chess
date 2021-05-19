import pygame
from DataBank import data_bank as db

class GameLogic:
    def __init__(self):
        self.moves = []

    def _send_status_of_game_by(self, event_type):
        self.event = pygame.event.Event(event_type, dict="True")
        pygame.event.post(self.event)

    def _is_draw(self):
        """
        If position of the board is repeating three times, that is draw. List "self.moves" contains all moves, if last
        four moves (moves_4) are the same like previous moves (moves_8_4) and next previous moves (moves_12_8) are also
        the same like that is draw.
        :return: True if is a draw, False if is not a draw
        """
        if len(self.moves) > 12:
            moves_4 = self.moves[-4:]
            moves_8_4 = self.moves[-8:-4]
            moves_12_8 = self.moves[-12:-8]
            if moves_4 == moves_12_8 and moves_4 == moves_8_4:
                return True
            else:
                return False

    def check_status_of_game_by(self, move):
        # add move
        self.moves.append(move)

        # checking is it draw
        if self._is_draw():
            self._send_status_of_game_by(db.DRAW)








