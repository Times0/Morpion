import random
import time

from fonctions import *


class EdouardLeBot:
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

    def playwise(self, board, turn, return_list):
        print("Started thinking")
        if turn == 1:
            maximizing = True
        else:
            maximizing = False
        start_time = time.time()
        evaluation, best_move_coord = self.minimax(board, maximizing)
        return_list[0] = best_move_coord
        print(f"Finished thinking in {time.time() - start_time:.2f} seconds")

    def minimax_root(self, board, maximizingPlayer):
        b = board.copy()
        # game terminée
        if game_state(board) == 1:
            return 1, (0, 0)
        elif game_state(board) == 2:
            return -1, (0, 0)
        elif game_state(board) == 3:
            return 0, (0, 0)

        else:
            # game pas terminée
            qi, qj = 0, 0
            if maximizingPlayer:
                maxEval = -1  # minimum possible
                for i in range(3):
                    for j in range(3):
                        if b[i][j] == 0:
                            b[i][j] = 1
                            evaluation, (_, _) = self.minimax_root(b, False)
                            if evaluation > maxEval:
                                maxEval = evaluation
                                qi, qj = i, j
                            b[i][j] = 0
                return maxEval, (qi, qj)

            else:
                minEval = 1
                for i in range(3):
                    for j in range(3):
                        if b[i][j] == 0:
                            b[i][j] = 2
                            evaluation, (_, _) = self.minimax_root(b, True)
                            if evaluation < minEval:
                                minEval = evaluation
                                qi, qj = i, j
                            b[i][j] = 0
                return minEval, (qi, qj)

    def minimax(self, a, maximizingPlayer):
        board = a.copy()
        # game terminée
        if game_state(board) == 1:
            return 1, (0, 0)
        elif game_state(board) == 2:
            return -1, (0, 0)
        elif game_state(board) == 3:
            return 0, (0, 0)
        else:
            # game pas terminée
            allevals = []
            if maximizingPlayer:
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == 0:
                            board[i][j] = 1
                            evaluation, pi, pj = self.minimax_root(board, False)
                            allevals.append((evaluation, (i, j)))
                            board[i][j] = 0

                maxeval = max(allevals)[0]
                allbestevals = [i for i in allevals if i[0] == maxeval]

                return random_elem_in(allbestevals)
            else:
                for i in range(3):
                    for j in range(3):
                        if board[i][j] == 0:
                            board[i][j] = 2
                            evaluation, (pi, pj) = self.minimax_root(board, True)
                            allevals.append((evaluation, (i, j)))
                            board[i][j] = 0
                mineval = min(allevals)[0]
                allbestevals = [i for i in allevals if i[0] == mineval]
                return random_elem_in(allbestevals)
