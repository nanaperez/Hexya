# Alejandra Perez y Yeison Osorio
# Python 3
# Jupyter es usado
# Se utilizo Minimax + alpha/beta pruning + funcion de evaluacion 

import sys
import time
import random
import numpy as np

#FUNCION PRINCIPAL, DADO UN ESTADO Y UN JUGADOR SE RETORNA LA MEJOR JUGADA
def Agente_YeisonOsorio_AlejandraPerez (estado, jugador):

    adversario = 0
    if jugador == 1:
        adversario = 2
    else:
        adversario = 1

#if __name__ == '__main__':



#Hallar el tiempo de ejecucion
start = time.time()
cont = 0
for i in range(0,1000000):
    cont += 1
end = time.time()
print(end-start)

