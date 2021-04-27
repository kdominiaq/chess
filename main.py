import pygame
from Screen import Screen
from Board import Board


def main():

    screen = Screen()
    board = Board()
    screen.init_board_with_pieces()

    clock = pygame.time.Clock()

    # Game Loop
    running = True
    while running:

        # declaration fps
        clock.tick(60)

        # Process input (events)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False

        # update screen
        print(screen.all_sprite.sprites()[1].rect.x)

        board.move_piece('a1a3')
        screen.all_sprite.update()


        screen.update()

        pygame.display.flip()



if __name__ == '__main__':
    main()

