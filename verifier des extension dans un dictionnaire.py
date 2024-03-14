import sys

n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.

# Créer un dictionnaire pour stocker les associations extension-type MIME
assoc_table = {}

for i in range(n): 
    ext, mt = input().split()
    # Stocker les associations dans le dictionnaire (en minuscule pour ignorer la casse)
    assoc_table[ext.lower()] = mt

for i in range(q):
    fname = input()  # Nom de fichier
    # Trouver la dernière occurrence d'un point pour extraire l'extension
    dot_position = fname.rfind(".")
    if dot_position != -1:
        extension = fname[dot_position + 1:].lower()  # Extraire l'extension et convertir en minuscule
        # Imprimer le type MIME si l'extension est trouvée dans la table d'association, sinon "UNKNOWN"
        print(assoc_table.get(extension, "UNKNOWN"))
    else:
        # Si aucun point trouvé dans le nom de fichier, imprimer "UNKNOWN"
        print("UNKNOWN")
