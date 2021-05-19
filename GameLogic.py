from DataBank import DataBank
from ChessObject import *


class GameLogic(DataBank, BlackPiece, BlackBishop, BlackKing, BlackRook, BlackQueen, BlackKnight, WhiteBishop,
                WhiteKing, WhiteRook, WhiteKnight, WhitePiece, WhiteQueen):
    def __init__(self):
        super().__init__()

    def _send_status_of_game_by(self, event_type):
        """
        :param event_type: Type of event which will caught in main of the program.
        :return: None.
        """
        self.event = pygame.event.Event(event_type)
        pygame.event.post(self.event)

    @staticmethod
    def _is_draw_by_repeating_moves():
        """
        If position of the board is repeating three times, that is draw. List "self.moves" contains all moves, if last
        four moves (moves_4) are the same like previous moves (moves_8_4) and next previous moves (moves_12_8) are also
        the same like that is draw.
        :return: True if is a draw, False if is not a draw
        """
        if len(DataBank._moves) > 12:
            moves_4 = DataBank._moves[-4:]
            moves_8_4 = DataBank._moves[-8:-4]
            moves_12_8 = DataBank._moves[-12:-8]
            if moves_4 == moves_12_8 and moves_4 == moves_8_4:
                return True
            else:
                return False

    @staticmethod
    def _is_draw_by_pieces():
        """
        Looking for insufficient counter of piece on the board. Like 3, when on Board are only King, King, Knight or
        King, King, Bishop. Like 2, when on board are only King and King.
        :return: True if is a draw, False if is not a draw.
        """
        # Only Kings on the board
        if len(DataBank._all_sprite) <= 2:
            return True
        # Only Kings and one Knight or Bishop on the board
        if len(DataBank._all_sprite) == 3:
            # If counter is three that means is draw, counter++ if one of the list of bishops, knights and kings exists.
            counter_of_piece = 0
            for single_piece in DataBank._all_sprite:
                if isinstance(BlackKing, single_piece):
                    counter_of_piece += 1
                elif isinstance(WhiteKing, single_piece):
                    counter_of_piece += 1
                elif isinstance(BlackBishop, single_piece):
                    counter_of_piece += 1
                elif isinstance(WhiteBishop, single_piece):
                    counter_of_piece += 1
                elif isinstance(WhiteKnight, single_piece):
                    counter_of_piece += 1
                elif isinstance(BlackKnight, single_piece):
                    counter_of_piece += 1

            if counter_of_piece <= 3:
                return True

    def check_status_of_game_by(self):
        # Checking is it draw
        if self._is_draw_by_repeating_moves() or self._is_draw_by_pieces():
            self._send_status_of_game_by(self.DRAW)








