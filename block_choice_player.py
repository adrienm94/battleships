def block_choice_player(grid_computer, grid_size):
    print("-----\nPlayer :")
    line_chosen_player = int(input("Line to choose :"))
    col_chosen_player = int(input("Column to choose :"))
    print(f'Has chosen {[line_chosen_player, col_chosen_player]} :')
    if not(line_chosen_player in range(grid_size)) or not(col_chosen_player in range(grid_size)):
        print("Out of grid.")
        return 0
    elif grid_computer[line_chosen_player][col_chosen_player] == 1:
        print("Sunk!")
        grid_computer[line_chosen_player][col_chosen_player] = None
        return 1
    else:
        print("Miss!")
        return 0
