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


def evaluate(estado):
    function = random.randint(0, 11)
    return function


def alphabeta(state, depth, alpha, beta, player):
    moves = getMoves(state)
    if (depth == 0 or len(moves) == 0):
        return evaluate(state)

    if (player == 1):
        v = -infinity
        newState = state
        for child in moves:
            newState[child] = 1
            v = max(v, alphabeta(newState, depth - 1, alpha, beta, 2))
            alpha = max(alpha, v)
            if (beta <= alpha):
                break
        print newState
        return v
    else:
        v = infinity
        newState = state
        for child in moves:
            newState[child] = 2
            v = min(v, alphabeta(newState, depth - 1, alpha, beta, 1))
            beta = min(beta, v)
            if beta <= alpha:
                break
        print newState
        return v


def agente(state, player):
    return alphabeta(state, 100, -infinity, infinity, player)


tablero = np.zeros((11, 11))
print agente(tablero, 1)