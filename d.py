def afficher_triangle(hauteur):
    for i in range(1, hauteur + 1):
        ligne = i * '*' * 
        print(ligne)

# Exemple d'utilisation avec une hauteur de 5
afficher_triangle(10)
