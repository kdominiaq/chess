import pygame

from Screen import Screen


def main():

    screen = Screen()

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
            # event moving pieces

        screen.board.move_piece('a1h2')

        screen.update()


if __name__ == '__main__':
    main()

