print(1 != 2) # True
print(1 == 2) # False
print(bool(2.4)) # True
print(bool(0.0)) # False


# Demande à l'utilisateur de choisir un mot de passe et calcule son modulo
mot_de_passe = int(input('Choisissez un mot de passe (entier positif) : '))
resultat_modulo = mot_de_passe % 7  # Vous pouvez choisir un autre nombre pour le modulo

# Demande à une autre personne de deviner le mot de passe
essai = int(input('Devinez le mot de passe : '))

# Vérifie si l'essai correspond au résultat du modulo
if essai % 7 == resultat_modulo:
    print('Mot de passe correct !')
else:
    print('Mot de passe incorrect.')
