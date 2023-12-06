nb1 = input("Entrez un chiffre / nombre nb1 :")
nb2 = input("Entrez un chiffre / nombre nb2 :")

# vérifie si nb1 est un chiffre
while not nb1.isdigit():
   nb1 = input("Entrez un chiffre / nombre :")


# vérifie si nb2 est un chiffre
while not nb2.isdigit():
    nb2 = input("Entrez un chiffre / nombre :")

# Convertit en fllotant
nb1 = float(nb1)
nb2 = float(nb2)

op = input("Saisissez l'opérateur :")

# Execute l'opération
if op == "+": 
    print(nb1, " + ", nb2, "=", nb1 + nb2)
elif op == "-": 
    print(nb1, " - ", nb2, "=", nb1 - nb2)
elif op == "/": 
    if nb2 != 0:
        print(nb1, " / ", nb2, "=", nb1 / nb2)
    else:
        print("La division par zéro est impossible")
elif op == "x":
    print(nb1, " x ", nb2, "=", nb1 * nb2)
elif op == "=":
    print(nb1, " = ", nb1)

# Erreur si l'opérateur est incorrect
else:
    print("L'opérateur est incorrect")
