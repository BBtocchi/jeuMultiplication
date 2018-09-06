'''
  Un jeu ou il faut deviner le plus vite possible 
  les tables de multiplications
'''

import os
from random import randrange

premierNombre = randrange(10)
deuxiemeNombre = randrange(10)

premierNombre = int(premierNombre)
deuxiemeNombre = int(deuxiemeNombre)

score = premierNombre * deuxiemeNombre
print(premierNombre, "*" , deuxiemeNombre)

essai = input(">")

if int(essai) == score:
    print("bravo !")
else:
    print("erreur !")

# l'utilisation de commande "pause" n'est
# pas recommandée car elle n'est pas
# disponible sur tous les OS
# os.system("pause")

# on utilise pluttôt un simple "input"
# pour attendre une instruction avant
# la fin de l'execution du script
input('- fin du jeu -')








