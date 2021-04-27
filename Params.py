class Params:
    def __init__(self, width_chess_board=800, height_chess_board=800):

        # width and height of board
        self.width_chess_board = width_chess_board
        self.height_chess_board = height_chess_board

        # width_field and height_field of one field (fields on board are 64)
        self.width_field = ((self.width_chess_board * 1.0) / 8).__round__()
        self.height_field = ((self.height_chess_board * 1.0) / 8).__round__()
