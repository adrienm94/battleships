def grid_creation(size):
    grid = []
    for i in range(size):
        grid.append([])
        for j in range(size):
            grid[i].append(None)
    return grid
    