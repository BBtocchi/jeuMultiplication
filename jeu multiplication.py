import os
'''un jeu ou il faut deviner le plus vite possible les tables de multiplications'''
from random import randrange

premierNombre=randrange(10)
deuxiemeNombre=randrange(10)

premierNombre=int(premierNombre)
deuxiemeNombre=int(deuxiemeNombre)

score=premierNombre*deuxiemeNombre
print(premierNombre, "*" , deuxiemeNombre)
input(int(essai))
if essai==score:
    print("gg")
    end
else:
    print("non")
    end
os.system("pause")
