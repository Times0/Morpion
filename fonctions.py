import numpy as np


def isInRect(pos, pos0, width, height):
    """
    Returns True if the point defined by the position is in the rectangle
    :param pos:
    :param pos0: top left point of the rectangle
    :param width:
    :param height:
    :return:bool
    """
    return pos0[0] <= pos[0] <= pos0[0] + width and pos0[1] <= pos[1] <= pos0[1] + height


def win_indexes(n):
    """
    Algo stylé qui génère toutes les combinaisons de win possibles
    :param n: taille du board
    :return: no idea
    """
    # Rows
    for r in range(n):
        yield [(r, c) for c in range(n)]
    # Columns
    for c in range(n):
        yield [(r, c) for r in range(n)]
    # Diagonal top left to bottom right
    yield [(i, i) for i in range(n)]
    # Diagonal top right to bottom left
    yield [(i, n - 1 - i) for i in range(n)]


def isBoardFull(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == 0:
                return False
    return True


def game_state(board):
    """
    Returns 0 if no one won and game is still going, 1 if player 1 won 2 if player 2 won (3 if draw)
    :param board: position
    :return:
    """
    n = len(board)

    for player in range(1, 3):
        for indexes in win_indexes(n):
            if all(board[r][c] == player for r, c in indexes):
                return player

    if isBoardFull(board):
        return 3
    return 0


def random_elem_in(L):
    n = len(L)
    return L[np.random.randint(0, n)]
