"""
Module contain all need parameters to create a board.

It has two specific pair of variables:
- width and height of the chess board
- width and height of the field on the chess board, witch is a 1/64 part of whole board

Code using this module has to handle following exceptions:
AttributeError,TypeError: invalid type of width or height chess board
"""

import os


class Params:
    def __init__(self, width_chess_board=800, height_chess_board=800, image_folder_path="chess_png"):
        """
        Parameters are responsible for creating board, so the best options for value of there are: number * 8, because chess
        board are made from 64 fields (8 by 8)
        :param width_chess_board: must be int
        :param height_chess_board: must be int
        :param image_folder_path: path to folder where are all image (format: *.png)
        """

        try:
            # width and height of board
            self.width_chess_board = width_chess_board
            self.height_chess_board = height_chess_board

            # width_field and height_field of one field (fields on board are 64)
            self.width_field = ((self.width_chess_board * 1.0) / 8).__round__()
            self.height_field = ((self.height_chess_board * 1.0) / 8).__round__()
        except (AttributeError, TypeError) as exc:
            print(f"Invalid type of parameters (expect Int): {exc}")

        self._path_folder = os.path.dirname(__file__)
        self.image_folder = os.path.join(self._path_folder, image_folder_path)
