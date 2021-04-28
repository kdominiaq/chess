from ChessObject import *


class Board(ChessBoard, BlackPiece, BlackBishop, BlackKing, BlackRook, BlackQueen, BlackKnight,
            WhiteBishop, WhiteKing,  WhiteRook, WhiteKnight, WhitePiece, WhiteQueen):
    def __init__(self):
        super().__init__()

        self.chess_board = ChessBoard()

        self.notation_to_xy_position = [{'notation': 'a1', 'position': (self.width_field * 0, self.height_field * 7)},
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

        self.initial_placement = [{'piece': WhiteRook(self.get_xy_from_chess_notation('a1')), 'position': 'a1'},
                                  {'piece': WhiteBishop(self.get_xy_from_chess_notation('b1')), 'position': 'b1'},
                                  {'piece': WhiteKnight(self.get_xy_from_chess_notation('c1')), 'position': 'c1'},
                                  {'piece': WhiteKing(self.get_xy_from_chess_notation('d1')), 'position': 'd1'},
                                  {'piece': WhiteQueen(self.get_xy_from_chess_notation('e1')), 'position': 'e1'},
                                  {'piece': WhiteKnight(self.get_xy_from_chess_notation('f1')), 'position': 'f1'},
                                  {'piece': WhiteBishop(self.get_xy_from_chess_notation('g1')), 'position': 'g1'},
                                  {'piece': WhiteRook(self.get_xy_from_chess_notation('h1')), 'position': 'h1'},
                                  {'piece': WhitePiece(self.get_xy_from_chess_notation('a2')), 'position': 'a2'},
                                  {'piece': WhitePiece(self.get_xy_from_chess_notation('b2')), 'position': 'b2'},
                                  {'piece': WhitePiece(self.get_xy_from_chess_notation('c2')), 'position': 'c2'},
                                  {'piece': WhitePiece(self.get_xy_from_chess_notation('d2')), 'position': 'd2'},
                                  {'piece': WhitePiece(self.get_xy_from_chess_notation('e2')), 'position': 'e2'},
                                  {'piece': WhitePiece(self.get_xy_from_chess_notation('f2')), 'position': 'f2'},
                                  {'piece': WhitePiece(self.get_xy_from_chess_notation('g2')), 'position': 'g2'},
                                  {'piece': WhitePiece(self.get_xy_from_chess_notation('h2')), 'position': 'h2'},

                                  {'piece': BlackRook(self.get_xy_from_chess_notation('a8')), 'position': 'a8'},
                                  {'piece': BlackBishop(self.get_xy_from_chess_notation('b8')), 'position': 'b8'},
                                  {'piece': BlackKnight(self.get_xy_from_chess_notation('c8')), 'position': 'c8'},
                                  {'piece': BlackKing(self.get_xy_from_chess_notation('d8')), 'position': 'd8'},
                                  {'piece': BlackQueen(self.get_xy_from_chess_notation('e8')), 'position': 'e8'},
                                  {'piece': BlackKnight(self.get_xy_from_chess_notation('f8')), 'position': 'f8'},
                                  {'piece': BlackBishop(self.get_xy_from_chess_notation('g8')), 'position': 'g8'},
                                  {'piece': BlackRook(self.get_xy_from_chess_notation('h8')), 'position': 'h8'},
                                  {'piece': BlackPiece(self.get_xy_from_chess_notation('a7')), 'position': 'a7'},
                                  {'piece': BlackPiece(self.get_xy_from_chess_notation('b7')), 'position': 'b7'},
                                  {'piece': BlackPiece(self.get_xy_from_chess_notation('c7')), 'position': 'c7'},
                                  {'piece': BlackPiece(self.get_xy_from_chess_notation('d7')), 'position': 'd7'},
                                  {'piece': BlackPiece(self.get_xy_from_chess_notation('e7')), 'position': 'e7'},
                                  {'piece': BlackPiece(self.get_xy_from_chess_notation('f7')), 'position': 'f7'},
                                  {'piece': BlackPiece(self.get_xy_from_chess_notation('g7')), 'position': 'g7'},
                                  {'piece': BlackPiece(self.get_xy_from_chess_notation('h7')), 'position': 'h7'}]

    def move_piece(self, chess_notation_move):
        for i in self.initial_placement:
            key = i.get('position')
            if key == chess_notation_move[0:2]:
                temp = self.get_xy_from_chess_notation(chess_notation_move[2:4])
                # run update in piece (the piece is object which has initialized by chess_notation_move[0:2}
                i.get("piece").update()
                # publish event with massage
                # - temp[0] - X value
                # - temp[1] - Y value
                my_event_1 = pygame.event.Event(MOVE, dict=[temp[0], temp[1]])
                pygame.event.post(my_event_1)

            break

    def get_xy_from_chess_notation(self, notation):
        for i in self.notation_to_xy_position:
            key = i.get('notation')
            if key == notation:
                return i.get('position')





