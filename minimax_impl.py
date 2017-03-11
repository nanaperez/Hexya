import random
import sys
import collections

#Implementacion algoritmo Minimax
def minimax_decision(nodo):

    if len(nodo.succesors) == 0:
        return getUtility(nodo)

    if nodo.isMax:
        return maxValue(nodo)
    else:
        return minValue(nodo)

    #Max value in minimax
    def maxValue(nodo):
    
        alpha = -inf
        
        if len(nodo.getSuccesors()) == 0:
            v = getUtility(nodo)
        else:
            for child in nodo.succesors:
                v = max(v, minimax_decision(child))
        return v
    
    #Min value in minimax
    def minValue(nodo):
    
        beta = inf
        if len(nodo.getSuccesors()) == 0:
            v = getUtility(nodo)

        else:
            for child in nodo.succesors:
                v = min(v, minimax_decision(child))
        return v

    def getUtility(nodo):
        return nodo.getValue()





#Funcion de evaluacion
def evalFunction(gameState):
    prevTurn=gameState.currentTurn
    gameState.currentTurn=curP
    
    gameState.countScore()
    val = 0
    if curP==1:
        val=(gameState.player1Score-gameState.player2Score)
    else:
        val=(gameState.player2Score-gameState.player1Score)

    gameState.currentTurn=prevTurn
    return val

#Implementacion Alpha Beta sin funcion de evaluacion
def alphabeta_full_search(estado, game):
    """Search game to determine best action; use alpha-beta pruning.
    As in [Fig. 6.7], this version searches all the way to the leaves."""

    player = game.to_move(estado)

    def max_value(estado, alpha, beta):
        if game.terminal_test(estado):
            return game.utility(estado, player)
        v = -infinity
        for (a, s) in game.successors(estado):
            v = max(v, min_value(s, alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(estado, alpha, beta):
        if game.terminal_test(estado):
            return game.utility(estado, player)
        v = infinity
        for (a, s) in game.successors(estado):
            v = min(v, max_value(s, alpha, beta))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    # Body of alphabeta_search starts here:
    accion, estado = argmax(game.successors(estado),
                           lambda ((a, s)): min_value(s, -infinity, infinity))
    return accion

def alphabeta_search(state, game, d=4, cutoff_test=None, eval_fn=None):
    """Search game to determine best action; use alpha-beta pruning.
    This version cuts off search and uses an evaluation function."""

    player = game.to_move(state)

    def max_value(state, alpha, beta, depth):
        if cutoff_test(state, depth):
            return eval_fn(state)
        v = -infinity
        for (a, s) in game.successors(state):
            v = max(v, min_value(s, alpha, beta, depth+1))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v

    def min_value(state, alpha, beta, depth):
        if cutoff_test(state, depth):
            return eval_fn(state)
        v = infinity
        for (a, s) in game.successors(state):
            v = min(v, max_value(s, alpha, beta, depth+1))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v

    # Body of alphabeta_search starts here:
    # The default test cuts off at depth d or at a terminal state
    cutoff_test = (cutoff_test or
                   (lambda state,depth: depth>d or game.terminal_test(state)))
    eval_fn = eval_fn or (lambda state: game.utility(state, player))
    action, state = argmax(game.successors(state),
                           lambda ((a, s)): min_value(s, -infinity, infinity, 0))
    return action

# Players for Games
def query_player(game, state):
    game.display(state)
    return num_or_str(raw_input('Your move? '))

def random_player(game, state):
    return random.choice(game.legal_moves())

def alphabeta_player(game, state):
    return alphabeta_search(state, game)

def play_game(game, *players):
    state = game.initial
    while True:
        for player in players:
            move = player(game, state)
            state = game.make_move(move, state)
            if game.terminal_test(state):
                return game.utility(state, players[0])

#Clase Game donde se definen unos parametros
class Game:
    """A game is similar to a problem, but it has a utility for each
    state and a terminal test instead of a path cost and a goal
    test. To create a game, subclass this class and implement
    legal_moves, make_move, utility, and terminal_test. You may
    override display and successors or you can inherit their default
    methods. You will also need to set the .initial attribute to the
    initial state; this can be done in the constructor."""

    def legal_moves(self, state):
        "Return a list of the allowable moves at this point."
        abstract

    def make_move(self, move, state):
        "Return the state that results from making a move from a state."
        abstract

    def utility(self, state, player):
        "Return the value of this final state to player."
        abstract

    def terminal_test(self, state):
        "Return True if this is a final state for the game."
        return not self.legal_moves(state)

    def to_move(self, state):
        "Return the player whose move it is in this state."
        return state.to_move

    def display(self, state):
        "Print or otherwise display the state."
        print state

    def successors(self, state):
        "Return a list of legal (move, state) pairs."
        return [(move, self.make_move(move, state))
                for move in self.legal_moves(state)]

    def __repr__(self):
        return '<%s>' % self.__class__.__name__