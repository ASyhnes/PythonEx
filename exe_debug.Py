#gerer les exeptions
agesUtilisateur = input("quel age as tu? ")

try:
    agesUtilisateur = int(agesUtilisateur)
except:
    print("Peut tu rentrer un nombre, ecrit avec des chiffres? Merci ... ")
else: 
    print("Tu as ", agesUtilisateur, "ans")
finally:
    print("END of program")


print("########################################")
print("Voici un nombre X")
number1 = 150
print(number1)
number2 = input("choisissez un nombre par lequel diviser X : ")
try: 
    number2 = int(number2)
except: 
    print("il fallait rentrer des nombres avec des chiffres")
else:
    try:
        print(" le resultat de {} / {} est egal à {}".format(number1, number2, number1 / number2))
    except ZeroDivisionError:
        print("Malheureusement, les mathématiques ne permettent pas de faire une division par Zero ...")
    except ValueError:
        print("Il faut un nombre ... ")
    except :
        print("Elle etait pourtant pas compliquée la consigne...")
    else:
        print("félicitation, vous avez réussi à rentrer un nombre valide !")

finally:
    print("Parce que c'est plus propre de faire une fin qui se termine par un 'Finally'")

# Type d'erreur:  NameError
#                 ValueError
#                 TypeError
#                 OSError
#                 AssertionError
#                 ValueError

# faire un raise
# try:
#     age = 18
#     age2 = int(input("chois un age "))

#     if age > age2:
#         raise MinorError("coucou :) !")
# except MinorError:
#     print ("j'ai capturé ton erreur")

#Assert

try: 
    age = int(input("quel age as tu? "))
    assert age > 18
except AssertionError:
    print("capture d'Assertion")