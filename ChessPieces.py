from Pieces import Pieces


class ChessPieces(Pieces):
    def __init__(self, x=0, y=0):
        super().__init__()
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x = dx
        self.y = dy

    def get_position(self):
        return self.x, self.y

