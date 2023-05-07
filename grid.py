import numpy as np
import pygame
from constants import *


class Grid:
    def __init__(self):
        self.data = np.zeros((3, 3))
        self.turn = 1

    def clicked(self, pos):
        """
        Modifie internal grid if the click is on an empty case and switches player
        :param pos:
        :return: None
        """
        j = int((pos[0] - POS0[0]) // CASE_LENGTH)
        i = int((pos[1] - POS0[1]) // CASE_LENGTH)

        if self.data[i, j] == 0:
            self.data[i, j] = self.turn
            self.switch_player()

    def played(self, pos):
        """
        used by AI so we know that the case is legal
        :param pos:
        :return: None
        """
        self.data[pos[0], pos[1]] = self.turn
        self.switch_player()

    def switch_player(self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1

    @staticmethod
    def draw_lines(win):
        mid = WINDOW_WIDTH // 2
        a = 50
        # verticales
        for i in range(2):
            pygame.draw.line(win, LINECOLOR,
                             (mid - CASE_LENGTH // 2 + i * CASE_LENGTH + a, OFFSET),
                             (mid - CASE_LENGTH // 2 + i * CASE_LENGTH + a, WINDOW_HEIGHT - OFFSET))
        # horizontales
        for i in range(2):
            pygame.draw.line(win, LINECOLOR,
                             (mid - CASE_LENGTH * 3 / 2 + a, CASE_LENGTH + OFFSET + i * CASE_LENGTH),
                             (mid - CASE_LENGTH * 3 / 2 + 3 * CASE_LENGTH + a, CASE_LENGTH + OFFSET + i * CASE_LENGTH))

    def draw_data(self, win):
        e = WINDOW_WIDTH // 50
        for i in range(3):
            for j in range(3):
                if self.data[i][j] == 1:

                    pygame.draw.circle(win, LINECOLOR,
                                       (POS0[0] + CASE_LENGTH // 2 + j * CASE_LENGTH,
                                        POS0[1] + CASE_LENGTH // 2 + i * CASE_LENGTH),
                                       CASE_LENGTH // 2 - CASE_LENGTH // 8, 2)
                elif self.data[i][j] == 2:

                    pygame.draw.line(win, LINECOLOR,
                                     (POS0[0] + j * CASE_LENGTH + e, POS0[1] + i * CASE_LENGTH + e),
                                     (POS0[0] + (j + 1) * CASE_LENGTH - e, POS0[1] + (i + 1) * CASE_LENGTH - e), 3)
                    pygame.draw.line(win, LINECOLOR,
                                     (POS0[0] + (j + 1) * CASE_LENGTH - e, POS0[1] + i * CASE_LENGTH + e),
                                     (POS0[0] + j * CASE_LENGTH + e, POS0[1] + i * CASE_LENGTH + CASE_LENGTH - e),
                                     3)
