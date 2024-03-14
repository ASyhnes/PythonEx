#trouver si un charactére est présent ou non, et connaitre son index:
#si l'index est -1, c'st que le charactére chercher est absent
s = "mot à tester" 
ch = 'à' #charactere a tester

if s.find(ch) != -1:
    print("Character found")
else:
    print("Character not found")

#trouver si un charactére est présent et avoir un retour booléen
s = "mot à tester2"
ch = 'à'

# Utilisation de l'opérateur in pour obtenir une réponse booléenne
if ch in s:
    print("True, Character found") 
else:
    print("False, Character not found")

# la même en version retour booléen: 
s = "mot à tester3"
ch = 'à'

# Utilisation de l'opérateur in pour vérifier la présence du caractère et retourner un booléen
character_found = ch in s

print(character_found) #renvoie True ou False