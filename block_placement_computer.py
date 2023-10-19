from random import randint


def block_placement_computer(grid_computer, grid_size, total_ships_by_player):
    ship_number_computer = 0
    while ship_number_computer < total_ships_by_player:
        line_grid_computer = randint(0, grid_size-1)
        col_grid_computer = randint(0, grid_size-1)
        if grid_computer[line_grid_computer][col_grid_computer] is None:
            grid_computer[line_grid_computer][col_grid_computer] = 1
            ship_number_computer += 1
