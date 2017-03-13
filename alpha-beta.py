import numpy as np
import random

infinity = float('inf')


def getMoves(estado):
    libres = []
    for i in range(len(estado)):
        for j in range(len(estado)):
            if (estado[i][j] == 0):
                libres.append((i, j))
    return libres


def evaluate(estado, player):
    function = random.randint(0, 11)
    return function


def alphabeta(state, depth, alpha, beta, player, oponente, maxi):
    moves = getMoves(state)
    if (depth == 0 or len(moves) == 0):
        return evaluate(state, player)

    if (maxi):
        v = -infinity
        newState = state
        for child in moves:
            newState[child] = player
            v = max(v, alphabeta(newState, depth - 1, alpha, beta, player, oponente, False))
            alpha = max(alpha, v)
            if (beta <= alpha):
                break
        return v
    else:
        v = infinity
        newState = state
        for child in moves:
            newState[child] = oponente
            v = min(v, alphabeta(newState, depth - 1, alpha, beta, player, oponente, True))
            beta = min(beta, v)
            if beta <= alpha:
                break
        return v


def agente_YeisonOsorio_AlejandraPerez(state, player):
    if (player== 1):
        oponente = 2
    else:
        oponente = 1
    return alphabeta(state, 50, -infinity, infinity, player, oponente, True)


#tablero = np.zeros((11, 11))
#print agente_YeisonOsorio_AlejandraPerez(tablero, 2)