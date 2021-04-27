import pygame
from Screen import Screen


def main():

    screen = Screen(800, 800)

    clock = pygame.time.Clock()

    # Game Loop
    running = True
    while running:

        # declare fps
        clock.tick(30)

        # Process input (events)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False


        # update screen
        screen.update()


if __name__ == '__main__':
    main()

