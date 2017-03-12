import numpy as np
import random

infinity = float('inf')
print -infinity




# def alphabeta(estado, profundidad, alfa, beta, jugador):
#     if(jugador == 1):
#         v = -infinity
       
def getMoves(estado):
    libres = []
    for i in range(len(estado)):
        for j in range(len(estado)):
          if ( estado[i][j] == 0 ):
            libres.append((i,j))
    return libres
    
def evaluate(estado):
    heuristic = random.randint(0, 11)
    return heuristic


def alphabeta(state, depth, alpha, beta, player):
    moves = getMoves(state)
    if (depth == 0 or len(moves) == 0):
        return evaluate(state)

    if (player == 1):
        v = -infinity
        for child in moves:
            v = max(v, alphabeta(child, depth -1, alpha, beta, 2))
            alpha = max(alpha, v)
            if (beta <= alpha):
                break
        return v
    else:
        v = infinity
        for child in moves:
            v = min(v, alphabeta(child, depth -1, alpha, beta, 1))
            beta = min(beta, v)
            if beta <= alpha:
                break
        return v

def agente(state, player):
    return alphabeta(state, 3, -infinity, infinity, player)
    

    
tablero = np.zeros((5, 5))
print agente(tablero, 2)
vacios = getMoves(tablero)




##https://github.com/aimacode/aima-python/blob/master/games.py
##https://github.com/tllano11/AI/blob/master/Project1/Agente_Tomas_Mateo.py