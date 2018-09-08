'''
Un jeu ou il faut deviner le plus vite possible 
les tables de multiplications
'''

import os
from random import randrange

game = True
score = 0

while game:

  # plus le score est élevé,
  # plus le jeu devient dur 
  premierNombre = randrange(10 + score)
  deuxiemeNombre = randrange(10 + score)

  premierNombre = int(premierNombre)
  deuxiemeNombre = int(deuxiemeNombre)

  devine = premierNombre * deuxiemeNombre
  
  # on efface la console
  os.system('clear')

  # on affiche le jeu
  print("=== Votre score : " + str(score) + " ===")
  print("-> Pour quitter, taper 'q' <-")
  print(premierNombre, "*" , deuxiemeNombre)

  # on attend la réponse
  essai = input("> ")

  if essai == "q":
    # on test si le joueur veut quitter
    game = False
  elif int(essai) == devine:
    # on test si la réponse est bonne
    print("** bravo ! **")
    score += 1
  else:
    # sinon, la réponse est mauvaise
    print("!! erreur !!")


# l'utilisation de commande "pause" n'est
# pas recommandée car elle n'est pas
# disponible sur tous les OS
# os.system("pause")

# on utilise pluttôt un simple "input"
# pour attendre une instruction avant
# la fin de l'execution du script
input('- fin du jeu -')








