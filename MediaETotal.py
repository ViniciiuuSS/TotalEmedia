import random
from time import sleep
import math
import datetime
print("\033[7;33;40m-=-" * 54)
jo = ("\033[7;33;40m LOJA")
print(jo.center(170))
print("\033[7;33;40m-=-" * 54)
#----------------------------------------------------------------------------------------------------------------------
s = 0
maior = 0
nomevelho = ""
totmulher = 0
for c in range(1, 3, 1):
    print("----- {} PESSOA -----".format(c))
    Nome = str(input("Nome:"))
    Idade = int(input("Idade:"))
    Sexo = str(input("Sexo [F/M]:"))
    s += Idade
    div = s / 4
    if (c == 1 and Sexo in "mM"):
        maior = Idade
        nomevelho = Nome
    if (Sexo in "mM" and Idade > maior):
        maior = Idade
        nomevelho = Nome
    if (Sexo in "Ff" and Idade > 20):
        totmulher += 1
print("A media de idade de todas as pessoas é de: {}".format(div))
print("O homem mais velho tem {} e se chama {}".format(maior, nomevelho))
print("Ao todo foram {} mulheres".format(totmulher))
