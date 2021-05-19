import pygame
from DataBank import DataBank


class Player(DataBank):
    def __init__(self):
        DataBank.__init__(self)
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
            db.FLAG = 0
        """
        move = self.sf.get_best_move_time(70)
        self._send_notation_for_move_by_event(self.STOCK_FISH_MOVE, move)
        DataBank._moves.append(move)
        self.sf.set_position(DataBank._moves)
        self.FLAG = 1


class Computer(Player):
    def __init__(self):
        super().__init__()

    def move(self):
        move = self.sf.get_best_move_time(50)
        self._send_notation_for_move_by_event(self.STOCK_FISH_MOVE, move)
        DataBank._moves.append(move)
        self.sf.set_position(self.moves)

        self.FLAG = 1


human = Human()
computer = Computer()
