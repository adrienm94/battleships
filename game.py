from block_choice_computer import block_choice_computer
from block_choice_player import block_choice_player


def game(grid_computer, grid_player, grid_size, total_ships_by_player):
    sunk_counter_computer = 0
    sunk_counter_player = 0
    while sunk_counter_computer != total_ships_by_player and sunk_counter_player != total_ships_by_player:
        print(f'-------\nScore : Computer = {sunk_counter_computer}, Player = {sunk_counter_player}\n-------')
        # Player turn
        sunk_counter_player += block_choice_player(grid_computer, grid_size)
        # Computer turn
        sunk_counter_computer += block_choice_computer(grid_player, grid_size)
    # Endgame
    print("\n")
    if sunk_counter_computer == total_ships_by_player:
        print("Computer wins!")
    else:
        print("Player wins!")
