import pygame
from Screen import Screen
from DataBank import DataBank
from Player import human, computer
from GameLogic import GameLogic


def main():


    game_logic = GameLogic()
    data_bank = DataBank()
    screen = Screen()
    clock = pygame.time.Clock()

    # Game Loop
    running = True
    while running:
        print(DataBank._board_sprite)
        print(DataBank._all_sprite)
        # declaration fps
        clock.tick(30)

        # Process input (events)
        for event in pygame.event.get():
            # check for closing window
            if event.type == pygame.QUIT:
                running = False
            elif event.type == data_bank.USER_MOVE:
                screen.board.move_piece(event.dict['dict'])
            elif event.type == data_bank.STOCK_FISH_MOVE:
                screen.board.move_piece(event.dict['dict'])
            elif event.type == data_bank.DRAW:
                print("==================DRAW===================")

        if data_bank.FLAG:
            human.move()
        else:
            computer.move()

        screen.update()

        game_logic.check_status_of_game_by()
if __name__ == '__main__':
    main()

