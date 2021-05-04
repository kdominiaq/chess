import pygame
from DataBank import data_bank as db


class Player(object):
    def __init__(self):
        super().__init__()
        self.event = None

    def _send_notation_for_move_by_event(self, event_type, notation):
        self.event = pygame.event.Event(event_type, dict=notation)
        pygame.event.post(self.event)

    def move(self):
        pass


class Human(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        """
        move = input()
        move = str(move)
        if move != '' and db.sf.is_move_correct(move):
            self._send_notation_for_move_by_event(db.USER_MOVE, move)
            db.moves.append(move)
            db.sf.set_position(db.moves)
            #print(db.sf.get_board_visual())
            #print(db.moves)
            db.FLAG = 0
        """
        move = db.sf.get_best_move_time(100)
        self._send_notation_for_move_by_event(db.STOCK_FISH_MOVE, move)
        db.moves.append(move)
        db.sf.set_position(db.moves)
        db.FLAG = 1


class Computer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        move = db.sf.get_best_move_time(100)
        self._send_notation_for_move_by_event(db.STOCK_FISH_MOVE, move)
        db.moves.append(move)
        db.sf.set_position(db.moves)

        db.FLAG = 1




human = Human()
computer = Computer()
