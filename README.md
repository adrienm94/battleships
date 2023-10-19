# Jeu de bataille navale

TO DO : 
- inclure des bateaux de différentes tailles (porte-avion=5, croiseur=4, contre torpilleur=3, sous-marin=3, torpilleur=2)
- placement des bateaux : boucle tant que tous les bateaux ne sont pas tous placés -> choix du
bateau -> bloquer aléatoirement une ligne (ou colonne) -> placer les éléments de bateau à la suite sur la ligne (ou
colonne) bloquée en regardant si les cases sont déjà prises ou pas (sans doute boucle tant que) -> mémoriser les
emplacements des bateaux dans un dictionnaire, {"porte-avions":[5,4] ,...} par exemple
- jeu : si bateau touché, alors vérifier à quel bateau correspondent les coordonnées proposées et enlever ces coordonnées dans le dictionnaire
si un bateau n'a plus de coordonnées dans le dictionnaire, alors il est coulé
- Peut-être créer des classes à la place des fonctions 
