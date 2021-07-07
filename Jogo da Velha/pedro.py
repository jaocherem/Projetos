"""
Código do Pedro e de algumas funções do jogo
"""
from copy import deepcopy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Retorno o estado inicial do tabuleiro
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Retorna o player da vez
    """
    xCounter = 0
    oCounter = 0

    for rows in board:
        for collums in rows:
            if collums == X:
                xCounter += 1
            elif collums == O:
                oCounter += 1

    if xCounter >= oCounter:
        return O
    else:
        return X

def actions(board):
    """
   Retorna um set de todas as ações possíveis no tabuleiro
    """
    validMoves = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                validMoves.add((i, j))

    return validMoves

def result(board, action):
    """
    Retorna o tabuleiro após um movimento
    """
    boardCopy = deepcopy(board)

    if boardCopy[action[0]][action[1]] != EMPTY:
        raise Exception("Quadrado da ação deve estar vazio")
    else:
        boardCopy[action[0]][action[1]] = player(board)

    return boardCopy

def winner(board):
    """
    Retorna o ganhador do jogo, se tiver algum
    """
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != EMPTY:
            return board[0][i]

    if board[0][0] == board [1][1] == board[2][2] or board[0][2] == board[1][1] == board[2][0] and board[1][1] != EMPTY:
        return board[1][1]

    return None

def terminal(board):
    """
    Retorna 'True' se o jogo terminou e 'False' caso não tenha terminado
    """
    if winner(board) is not None:
        return True

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                return False
    
    return True

def utility(board):
    """
    Retorna 1 se X venceu o jogo, -1 se O ganhou ou 0 caso tenha dado velha
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Retorna a melhor opção de jogada para o Pedro
    """
    if terminal(board):
        return None

    if player(board) == X:
        score = -math.inf
        bestAction = None

        for action in actions(board):
            minVal = maxValue(result(board, action))

            if minVal > score:
                score = minVal
                bestAction = action

        return bestAction

    elif player(board) == O:
        score = math.inf
        bestAction = None

        for action in actions(board):
            maxVal = minValue(result(board, action))

            if maxVal < score:
                score = maxVal
                bestAction = action

        return bestAction

def maxValue(board):
    if terminal(board):
        return utility(board)

    num = -math.inf

    for action in actions(board):
        num = max(num, minValue(result(board, action)))

    return num

def minValue(board):
    if terminal(board):
        return utility(board)

    num = math.inf

    for action in actions(board):
        num = min(num, maxValue(result(board, action)))

    return num