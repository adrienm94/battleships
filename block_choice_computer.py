from random import randint


def block_choice_computer(grid_player, grid_size):
    print("-----\nComputer :")
    blocks_already_chosen = []
    while True:  # this while loop avoids the computer to choose a block already seen
        line_chosen_computer = randint(0, grid_size - 1)
        col_chosen_computer = randint(0, grid_size - 1)
        if [line_chosen_computer, col_chosen_computer] not in blocks_already_chosen:
            blocks_already_chosen.append([line_chosen_computer, col_chosen_computer])
            break
    print(f'Has chosen {[line_chosen_computer, col_chosen_computer]} :')
    if grid_player[line_chosen_computer][col_chosen_computer] == 1:
        print("Sunk!")
        grid_player[line_chosen_computer][col_chosen_computer] = None
        return 1
    else:
        print("Miss!")
        return 0
