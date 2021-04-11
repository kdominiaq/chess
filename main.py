import pygame
from Screen import Screen
from ChessPieces import ChessPieces


def main():

    screen = Screen(800, 800)

    # Game Loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # display board
        screen.display_board()

        # display pieces for start
        screen.init_pieces_on_board()

        # update screen
        screen.update()


if __name__ == '__main__':
    main()

