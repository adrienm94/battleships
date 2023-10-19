# BattleShips game

# TO DO : - include ships of different size (porte-avion=5, croiseur=4, contre torpilleur=3, sous-marin=3,
# torpilleur=2) : - placement des bateaux : boucle tant que tous les bateaux ne sont pas tous placés -> choix du
# bateau -> bloquer aléatoirement une ligne (ou colonne) -> placer les éléments de bateau à la suite sur la ligne (ou
# colonne) bloquée en regardant si les cases sont déjà prises ou pas (sans doute boucle tant que) -> mémoriser les
# emplacements des bateaux dans un dictionnaire, {"porte-avions":[5,4] ,...} par exemple - jeu : si bateau touché,
# alors vérifier à quel bateau correspondent les coordonnées proposées et enlever ces coordonnées dans le dictionnaire
# si un bateau n'a plus de coordonnées dans le dictionnaire, alors il est coulé - maybe create classes


from grid_creation import grid_creation
from block_placement_computer import block_placement_computer
from block_placement_player import block_placement_player
from game import game


def main(grid_size=10, total_ships_by_player=5):
    print("-----------------------------------------")
    print(
        f'Welcome to Battleships game ({grid_size}x{grid_size} grid, {total_ships_by_player} ships to place). It is supposed a ship has a size of 1.')
    print("-----------------------------------------\n")

    # 8x8 Grid creation for computer
    print("Computer Grid creation")
    grid_computer = grid_creation(grid_size)

    # 8x8 Grid creation for player
    print("Player Grid creation\n-----")
    grid_player = grid_creation(grid_size)

    # The computer places some ships
    print(f'Computer places {total_ships_by_player} ships.')
    block_placement_computer(grid_computer, grid_size, total_ships_by_player)

    # The player places some ships.
    print(f'Player places {total_ships_by_player} ships.')
    block_placement_player(grid_player, grid_size, total_ships_by_player)

    # print(grid_player, grid_computer)

    # Game
    game(grid_computer, grid_player, grid_size, total_ships_by_player)

    print("\n-----------------------------------------")
    print("Thanks for your playing!")
    print("-----------------------------------------")


main()
