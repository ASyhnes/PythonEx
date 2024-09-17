#coding:utf-8

"""
importer un module : importe <nom_module>
                     from <nom_modul> importe <nom_fonvtion>
                     from <nom_modul> importe *
"""

def parler(personnage, message):
    print("{} : {}".format(personnage, message)) 

def au_revoir():
    print(" Au revoir :) !")

if __name__ == "__main--": 
    parler("jason", "bonjour tout le monde")
    au_revoir()

    
