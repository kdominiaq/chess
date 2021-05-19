from ChessObject import *
from DataBank import DataBank


class Board(ChessBoard, BlackPiece, BlackBishop, BlackKing, BlackRook, BlackQueen, BlackKnight,
            WhiteBishop, WhiteKing, WhiteRook, WhiteKnight, WhitePiece, WhiteQueen, DataBank):
    def __init__(self):
        super().__init__()
        DataBank.__init__(self)

        self._notation_to_xy_position = [{'notation': 'a1', 'position': (self.width_field * 0, self.height_field * 7)},
                                         {'notation': 'a2', 'position': (self.width_field * 0, self.height_field * 6)},
                                         {'notation': 'a3', 'position': (self.width_field * 0, self.height_field * 5)},
                                         {'notation': 'a4', 'position': (self.width_field * 0, self.height_field * 4)},
                                         {'notation': 'a5', 'position': (self.width_field * 0, self.height_field * 3)},
                                         {'notation': 'a6', 'position': (self.width_field * 0, self.height_field * 2)},
                                         {'notation': 'a7', 'position': (self.width_field * 0, self.height_field * 1)},
                                         {'notation': 'a8', 'position': (self.width_field * 0, self.height_field * 0)},

                                         {'notation': 'b1', 'position': (self.width_field * 1, self.height_field * 7)},
                                         {'notation': 'b2', 'position': (self.width_field * 1, self.height_field * 6)},
                                         {'notation': 'b3', 'position': (self.width_field * 1, self.height_field * 5)},
                                         {'notation': 'b4', 'position': (self.width_field * 1, self.height_field * 4)},
                                         {'notation': 'b5', 'position': (self.width_field * 1, self.height_field * 3)},
                                         {'notation': 'b6', 'position': (self.width_field * 1, self.height_field * 2)},
                                         {'notation': 'b7', 'position': (self.width_field * 1, self.height_field * 1)},
                                         {'notation': 'b8', 'position': (self.width_field * 1, self.height_field * 0)},

                                         {'notation': 'c1', 'position': (self.width_field * 2, self.height_field * 7)},
                                         {'notation': 'c2', 'position': (self.width_field * 2, self.height_field * 6)},
                                         {'notation': 'c3', 'position': (self.width_field * 2, self.height_field * 5)},
                                         {'notation': 'c4', 'position': (self.width_field * 2, self.height_field * 4)},
                                         {'notation': 'c5', 'position': (self.width_field * 2, self.height_field * 3)},
                                         {'notation': 'c6', 'position': (self.width_field * 2, self.height_field * 2)},
                                         {'notation': 'c7', 'position': (self.width_field * 2, self.height_field * 1)},
                                         {'notation': 'c8', 'position': (self.width_field * 2, self.height_field * 0)},

                                         {'notation': 'd1', 'position': (self.width_field * 3, self.height_field * 7)},
                                         {'notation': 'd2', 'position': (self.width_field * 3, self.height_field * 6)},
                                         {'notation': 'd3', 'position': (self.width_field * 3, self.height_field * 5)},
                                         {'notation': 'd4', 'position': (self.width_field * 3, self.height_field * 4)},
                                         {'notation': 'd5', 'position': (self.width_field * 3, self.height_field * 3)},
                                         {'notation': 'd6', 'position': (self.width_field * 3, self.height_field * 2)},
                                         {'notation': 'd7', 'position': (self.width_field * 3, self.height_field * 1)},
                                         {'notation': 'd8', 'position': (self.width_field * 3, self.height_field * 0)},

                                         {'notation': 'e1', 'position': (self.width_field * 4, self.height_field * 7)},
                                         {'notation': 'e2', 'position': (self.width_field * 4, self.height_field * 6)},
                                         {'notation': 'e3', 'position': (self.width_field * 4, self.height_field * 5)},
                                         {'notation': 'e4', 'position': (self.width_field * 4, self.height_field * 4)},
                                         {'notation': 'e5', 'position': (self.width_field * 4, self.height_field * 3)},
                                         {'notation': 'e6', 'position': (self.width_field * 4, self.height_field * 2)},
                                         {'notation': 'e7', 'position': (self.width_field * 4, self.height_field * 1)},
                                         {'notation': 'e8', 'position': (self.width_field * 4, self.height_field * 0)},

                                         {'notation': 'f1', 'position': (self.width_field * 5, self.height_field * 7)},
                                         {'notation': 'f2', 'position': (self.width_field * 5, self.height_field * 6)},
                                         {'notation': 'f3', 'position': (self.width_field * 5, self.height_field * 5)},
                                         {'notation': 'f4', 'position': (self.width_field * 5, self.height_field * 4)},
                                         {'notation': 'f5', 'position': (self.width_field * 5, self.height_field * 3)},
                                         {'notation': 'f6', 'position': (self.width_field * 5, self.height_field * 2)},
                                         {'notation': 'f7', 'position': (self.width_field * 5, self.height_field * 1)},
                                         {'notation': 'f8', 'position': (self.width_field * 5, self.height_field * 0)},

                                         {'notation': 'g1', 'position': (self.width_field * 6, self.height_field * 7)},
                                         {'notation': 'g2', 'position': (self.width_field * 6, self.height_field * 6)},
                                         {'notation': 'g3', 'position': (self.width_field * 6, self.height_field * 5)},
                                         {'notation': 'g4', 'position': (self.width_field * 6, self.height_field * 4)},
                                         {'notation': 'g5', 'position': (self.width_field * 6, self.height_field * 3)},
                                         {'notation': 'g6', 'position': (self.width_field * 6, self.height_field * 2)},
                                         {'notation': 'g7', 'position': (self.width_field * 6, self.height_field * 1)},
                                         {'notation': 'g8', 'position': (self.width_field * 6, self.height_field * 0)},

                                         {'notation': 'h1', 'position': (self.width_field * 7, self.height_field * 7)},
                                         {'notation': 'h2', 'position': (self.width_field * 7, self.height_field * 6)},
                                         {'notation': 'h3', 'position': (self.width_field * 7, self.height_field * 5)},
                                         {'notation': 'h4', 'position': (self.width_field * 7, self.height_field * 4)},
                                         {'notation': 'h5', 'position': (self.width_field * 7, self.height_field * 3)},
                                         {'notation': 'h6', 'position': (self.width_field * 7, self.height_field * 2)},
                                         {'notation': 'h7', 'position': (self.width_field * 7, self.height_field * 1)},
                                         {'notation': 'h8', 'position': (self.width_field * 7, self.height_field * 0)}]

        self._initial_placement = [{'piece': WhiteRook(self._get_xy_from_chess_notation('a1')), 'position': 'a1'},
                                   {'piece': WhiteKnight(self._get_xy_from_chess_notation('b1')), 'position': 'b1'},
                                   {'piece': WhiteBishop(self._get_xy_from_chess_notation('c1')), 'position': 'c1'},
                                   {'piece': WhiteQueen(self._get_xy_from_chess_notation('d1')), 'position': 'd1'},
                                   {'piece': WhiteKing(self._get_xy_from_chess_notation('e1')), 'position': 'e1'},
                                   {'piece': WhiteBishop(self._get_xy_from_chess_notation('f1')), 'position': 'f1'},
                                   {'piece': WhiteKnight(self._get_xy_from_chess_notation('g1')), 'position': 'g1'},
                                   {'piece': WhiteRook(self._get_xy_from_chess_notation('h1')), 'position': 'h1'},
                                   {'piece': WhitePiece(self._get_xy_from_chess_notation('a2')), 'position': 'a2'},
                                   {'piece': WhitePiece(self._get_xy_from_chess_notation('b2')), 'position': 'b2'},
                                   {'piece': WhitePiece(self._get_xy_from_chess_notation('c2')), 'position': 'c2'},
                                   {'piece': WhitePiece(self._get_xy_from_chess_notation('d2')), 'position': 'd2'},
                                   {'piece': WhitePiece(self._get_xy_from_chess_notation('e2')), 'position': 'e2'},
                                   {'piece': WhitePiece(self._get_xy_from_chess_notation('f2')), 'position': 'f2'},
                                   {'piece': WhitePiece(self._get_xy_from_chess_notation('g2')), 'position': 'g2'},
                                   {'piece': WhitePiece(self._get_xy_from_chess_notation('h2')), 'position': 'h2'},

                                   {'piece': BlackRook(self._get_xy_from_chess_notation('a8')), 'position': 'a8'},
                                   {'piece': BlackKnight(self._get_xy_from_chess_notation('b8')), 'position': 'b8'},
                                   {'piece': BlackBishop(self._get_xy_from_chess_notation('c8')), 'position': 'c8'},
                                   {'piece': BlackQueen(self._get_xy_from_chess_notation('d8')), 'position': 'd8'},
                                   {'piece': BlackKing(self._get_xy_from_chess_notation('e8')), 'position': 'e8'},
                                   {'piece': BlackBishop(self._get_xy_from_chess_notation('f8')), 'position': 'f8'},
                                   {'piece': BlackKnight(self._get_xy_from_chess_notation('g8')), 'position': 'g8'},
                                   {'piece': BlackRook(self._get_xy_from_chess_notation('h8')), 'position': 'h8'},
                                   {'piece': BlackPiece(self._get_xy_from_chess_notation('a7')), 'position': 'a7'},
                                   {'piece': BlackPiece(self._get_xy_from_chess_notation('b7')), 'position': 'b7'},
                                   {'piece': BlackPiece(self._get_xy_from_chess_notation('c7')), 'position': 'c7'},
                                   {'piece': BlackPiece(self._get_xy_from_chess_notation('d7')), 'position': 'd7'},
                                   {'piece': BlackPiece(self._get_xy_from_chess_notation('e7')), 'position': 'e7'},
                                   {'piece': BlackPiece(self._get_xy_from_chess_notation('f7')), 'position': 'f7'},
                                   {'piece': BlackPiece(self._get_xy_from_chess_notation('g7')), 'position': 'g7'},
                                   {'piece': BlackPiece(self._get_xy_from_chess_notation('h7')), 'position': 'h7'}]

        # add sprites to groups
        self._add_pieces_to_sprite_group()

    @staticmethod
    def update_sprites(screen):
        DataBank._board_sprite.draw(screen)
        DataBank._all_sprite.update()
        DataBank._all_sprite.draw(screen)

    def _add_pieces_to_sprite_group(self):
        self.chess_board = ChessBoard()
        # add chess board
        DataBank._board_sprite.add(self.chess_board)
        # add all pieces
        for i in self._initial_placement:
            # for example key is WhiteRock
            key = i.get('piece')
            DataBank._all_sprite.add(key)

    def move_piece(self, chess_notation_move):
        """
        :param chess_notation_move: is pair of chess fields, like 'a2a4'
        :return: None
        """

        # get (x,y) for previous_pos and next_pos by chess notation, like 'a1'
        previous_pos = self._get_xy_from_chess_notation(chess_notation_move[0:2])
        new_pos = self._get_xy_from_chess_notation(chess_notation_move[2:4])

        for i in DataBank._all_sprite.sprites():
            # key = rect.x, rect.f of sprite in group
            key = (i.rect.x, i.rect.y)
            # if on new position is some piece, must be remove - because beat
            if key == new_pos:
                i.remove()
                break

        # searching piece by compare (x, y)
        for i in DataBank._all_sprite.sprites():
            # key = rect.x, rect.f of sprite in group
            key = (i.rect.x, i.rect.y)

            # if previous pos is the same like key, set new position of piece
            if key == previous_pos:
                # fix the bug which has showed screen wrong (moved board)
                if isinstance(i, ChessBoard):
                    continue
                # looking for switch rook with king, so rooks are only in the corner on the board. In project I decide
                # to choose convention like this:
                # - sprites left top corner (x,y) = (0,0) - this is a reference point of move.
                # for example, top right field system interaction's of the board is (0, width_board - width_field)
                if isinstance(i, BlackKing) or isinstance(i, WhiteKing):
                    # ('b1', 'g1', 'b8', 'g8')
                    for rook in DataBank._all_sprite.sprites():
                        if chess_notation_move[2:4] == 'c1' and isinstance(rook, WhiteRook) and rook.rect.x == 0 \
                                and rook.rect.y == (self.height_chess_board - self.height_field):
                            temp = self._get_xy_from_chess_notation('d1')

                            rook.update(temp[0], temp[1])
                        elif chess_notation_move[2:4] == 'g1' and isinstance(rook, WhiteRook) and \
                                rook.rect.x == (self.width_chess_board - self.width_field) and rook.rect.y == (
                                self.height_chess_board - self.height_field):
                            temp = self._get_xy_from_chess_notation('f1')

                            rook.update(temp[0], temp[1])
                        elif chess_notation_move[2:4] == 'c8' and isinstance(rook, BlackRook) and rook.rect.x == 0 \
                                and rook.rect.y == 0:
                            temp = self._get_xy_from_chess_notation('d8')
                            rook.update(temp[0], temp[1])

                        elif chess_notation_move[2:4] == 'g8' and isinstance(rook, BlackRook) \
                                and rook.rect.x == (self.width_chess_board - self.width_field) and rook.rect.y == 0:
                            temp = self._get_xy_from_chess_notation('f8')
                            rook.update(temp[0], temp[1])

                # looking for changing pawn for queen
                if isinstance(i, BlackPiece) and (i.rect.y == self.height_chess_board - self.height_field):
                    print('w damka')
                    i = BlackQueen((i.rect.x, i.rect.y))
                if isinstance(i, WhiteRook) and i.rect.y == 0:
                    print('b damka')
                    i = WhiteQueen((i.rect.x, i.rect.y))

                # next_post is a tuple (x, y), for sprite.Sprite.update must send variable by variable
                i.update(new_pos[0], new_pos[1])

    def _get_xy_from_chess_notation(self, notation):
        """
        Returns position of 'X' and 'Y' by chess notation. Function scan list '_notation_to_xy_position'
        for dict with the same notation like passing notation. Example: passing 'a1' -> return (0,700), example is true
        if height and width of chess board i 800x800.
        :param notation: chess notation to one field, like 'a1'
        :return: tuple with x and y value
        """
        for i in self._notation_to_xy_position:
            key = i.get('notation')
            if key == notation:
                return i.get('position')

    def _get_chess_notation_from_xy(self, xy):
        """
        Returns position of 'X' and 'Y' by chess notation. Function scan list '_notation_to_xy_position'
        for dict with the same notation like passing notation. Example: passing 'a1' -> return (0,700), example is true
        if height and width of chess board i 800x800.
        :param xy: chess notation to one field, like 'a1'
        :return: tuple with x and y value
        """
        for i in self._notation_to_xy_position:
            key = i.get('position')
            if key == xy:
                return i.get('notation')

