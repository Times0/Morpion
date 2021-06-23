import pygame
from constants import *


if __name__ == "__main__":
    pygame.init()
    win = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    from game import Game
    game = Game(win)
    game.run()
    
