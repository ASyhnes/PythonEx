#CODING:utf-8
print("Hello\n\t World \n test")



'''
operateur:
+-/*
% modulo: reste d'une division euclidienne
5/2 = 2.5 ou 2 en fonction de entier ou float

'''

calcul = 5 / 2
calcul = int(calcul)

print("resultat int: ", calcul)

calcul = 5 / 2
calcul = float(calcul)

print("resultat float: ", calcul)

# modulo

calcul2 = 5 % 2
calcul2 = int(calcul2)
print("resultat modulo: ", calcul2)

# savoir si un nombre est pair: 
x = int(input("rentrez un nombre : "))
nombre = x % 2
if nombre == 0:
    print(x, " est nombre pair")
else:
    print(x, " est nombre impair")

# boucle
compteur = 0
while compteur < 5:
    compteur += 1
    print("je suis à ", compteur)