
class Board:
    def __init__(self, width=800, height=800):

        # width and height of board
        self.width_board = width
        self.height_board = height

        # width_field and height_field of one field (fields on board are 64)
        self.width_field = ((self.width_board * 1.0) / 8).__round__()
        self.height_field = ((self.height_board * 1.0) / 8).__round__()

        self.initial_placement = [{'piece': 'w_rock_L', 'position': 'a1'},
                                  {'piece': 'w_bishop_L', 'position': 'b1'},
                                  {'piece': 'w_knight_L', 'position': 'c1'},
                                  {'piece': 'w_king', 'position': 'd1'},
                                  {'piece': 'bw_queen', 'position': 'e1'},
                                  {'piece': 'w_knight_R', 'position': 'f1'},
                                  {'piece': 'w_bishop_R', 'position': 'g1'},
                                  {'piece': 'w_rock_R', 'position': 'h1'},
                                  {'piece': 'w_piece_A', 'position': 'a2'},
                                  {'piece': 'w_piece_B', 'position': 'b2'},
                                  {'piece': 'w_piece_C', 'position': 'c2'},
                                  {'piece': 'w_piece_D', 'position': 'd2'},
                                  {'piece': 'w_piece_E', 'position': 'e2'},
                                  {'piece': 'w_piece_F', 'position': 'f2'},
                                  {'piece': 'w_piece_G', 'position': 'g2'},
                                  {'piece': 'w_piece_H', 'position': 'h2'},

                                  {'piece': 'b_rock_L', 'position': 'a8'},
                                  {'piece': 'b_bishop_L', 'position': 'b8'},
                                  {'piece': 'b_knight_L', 'position': 'c8'},
                                  {'piece': 'b_king', 'position': 'd8'},
                                  {'piece': 'b_queen', 'position': 'e8'},
                                  {'piece': 'b_knight_R', 'position': 'f8'},
                                  {'piece': 'b_bishop_R', 'position': 'g8'},
                                  {'piece': 'b_rock_R', 'position': 'h8'},
                                  {'piece': 'b_piece_A', 'position': 'a7'},
                                  {'piece': 'b_piece_B', 'position': 'b7'},
                                  {'piece': 'b_piece_C', 'position': 'c7'},
                                  {'piece': 'b_piece_D', 'position': 'd7'},
                                  {'piece': 'b_piece_E', 'position': 'e7'},
                                  {'piece': 'b_piece_F', 'position': 'f7'},
                                  {'piece': 'b_piece_G', 'position': 'g7'},
                                  {'piece': 'b_piece_H', 'position': 'h7'}]

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

    def get_xy_from_chess_notation(self, notation):
        for i in self.notation_to_xy_position:
            key = i.get('notation')
            if key is notation:
                return i.get('position')





