def block_placement_player(grid_player, grid_size, total_ships_by_player):
    ship_number_player = 0
    while ship_number_player < total_ships_by_player:
        print(f'Place your ship n°{ship_number_player+1} :')
        line_grid_player = int(input("Line number :"))
        col_grid_player = int(input("Column number :"))
        if not(line_grid_player in range(grid_size)) or not(col_grid_player in range(grid_size)):
            print("Out of grid.")
        elif grid_player[line_grid_player][col_grid_player] == 1:
            print(
                f'A ship has been already placed at {[line_grid_player, col_grid_player]}.')
        else:
            grid_player[line_grid_player][col_grid_player] = 1
            ship_number_player += 1
