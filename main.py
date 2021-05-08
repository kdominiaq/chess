import pygame
from Screen import Screen
from DataBank import data_bank
from Player import human, computer


def main():

    screen = Screen()
    clock = pygame.time.Clock()

    # Game Loop
    running = True
    while running:

        # declaration fps
        clock.tick(10)

        # Process input (events)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
            elif event.type == data_bank.USER_MOVE:
                screen.board.move_piece(event.dict['dict'])
            elif event.type == data_bank.STOCK_FISH_MOVE:
                screen.board.move_piece(event.dict['dict'])

        screen.update()

        if data_bank.FLAG:
            human.move()
        else:
            computer.move()


if __name__ == '__main__':
    main()

