import random
import numpy as np
from fonctions import *


class Edouard:
    def __init__(self):
        pass

    def play_random(self, board):
        """
        returns the pos of where it wants to play in order to win
        :param board:
        :return: Tuple
        """
        available = []

        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    available.append((i, j))

        return available[random.randint(0, len(available) - 1)]

    def play_bad(self, board):
        for i in range(3):
            for j in range(3):
                if board[i][j] == 0:
                    board[i][j] = 2
                    if game_state(board) == 2:
                        return i, j
                    else:
                        board[i][j] = 0
        return self.play_random(board)

    def playwise(self, board, turn, return_list):
        print("Started thinking")
        if turn == 1:
            maximizingPlayer = True
        else:
            maximizingPlayer = False
        a = self.minimax2(board, maximizingPlayer)
        return_list[0] = (a[1], a[2])
        print("returned")

    def minimax(self, a, maximizingPlayer):
        board = a.copy()
        # game terminée
        if game_state(board) == 1:
            return 1, 0, 0
        elif game_state(board) == 2:
            return -1, 0, 0
        elif game_state(board) == 3:
            return 0, 0, 0

        else:
            # game pas terminée
            qi, qj = 0, 0
            if maximizingPlayer:
                maxEval = -1  # minimum possible
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == 0:
                            board[i][j] = 1
                            evaluation, _, _ = self.minimax(board, False)  # _ = useless
                            if evaluation > maxEval:
                                maxEval = evaluation
                                qi, qj = i, j
                            board[i][j] = 0
                return maxEval, qi, qj

            else:
                minEval = 1
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == 0:
                            board[i][j] = 2
                            evaluation, v, w = self.minimax(board, True)
                            if evaluation < minEval:
                                minEval = evaluation
                                qi, qj = i, j
                            board[i][j] = 0
                return minEval, qi, qj

    def minimax2(self, a, maximizingPlayer):
        board = a.copy()
        # game terminée
        if game_state(board) == 1:
            return 1, 0, 0
        elif game_state(board) == 2:
            return -1, 0, 0
        elif game_state(board) == 3:
            return 0, 0, 0
        else:
            # game pas terminée
            allevals = []
            if maximizingPlayer:
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == 0:
                            board[i][j] = 1
                            evaluation, pi, pj = self.minimax(board, False)
                            allevals.append((evaluation, i, j))
                            board[i][j] = 0

                maxeval = max(allevals)[0]
                allbestevals = [i for i in allevals if i[0] == maxeval]

                return random_elem_in(allbestevals)
            else:
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == 0:
                            board[i][j] = 2
                            evaluation, pi, pj = self.minimax(board, True)
                            allevals.append((evaluation, i, j))
                            board[i][j] = 0
                mineval = min(allevals)[0]
                allbestevals = [i for i in allevals if i[0] == mineval]
                return random_elem_in(allbestevals)
