import threading

from AI import EdouardLeBot
from Button import Button
from fonctions import *
from grid import *
import multiprocessing


class Game:
    def __init__(self, win):
        self.running = True
        self.gameOn = True

        self.win = win
        self.grid = Grid()
        self.bot = EdouardLeBot()
        self.ai_turn = 2
        self.j = [None, "human", "bot"]

        self.j2Button = Button(BUTTONDEFAULTCOLOR, BUTTONHOVERCOLOR, 15, 15, 180, 55, self.toggle_j2,
                               f"J2 : {self.j[2]}")
        self.restart_button = Button(BUTTONDEFAULTCOLOR, BUTTONHOVERCOLOR, 15, 107, 120, 55, self.restart,
                                     "Restart")
        self.quit_button = Button(BUTTONDEFAULTCOLOR, BUTTONQUITHOVERCOLOR, 15, 200, 100, 55, quit, "Quit")
        self.buttons = [self.quit_button, self.j2Button, self.restart_button]

    def run(self):
        hasToThink = True
        return_list = [None]

        self.running = True
        clickedOnGrid = False
        clock = pygame.time.Clock()
        while self.running:

            clock.tick(30)
            self.win.fill(BG_COLOR)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and isInRect(event.pos, POS0,
                                                                                           GRID_LENGTH,
                                                                                           GRID_LENGTH):
                    clickedOnGrid = True
                    pos = event.pos
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    for button in self.buttons:
                        if button.isMouseOnIt(event.pos):
                            button.onclick()

                if event.type == pygame.MOUSEMOTION:
                    for button in self.buttons:
                        if button.isMouseOnIt(event.pos):
                            button.hover()
                        else:
                            button.default()  # pas ouf, pour opti il faut que on remette à default seulement quand
                            # on sort du button et pas 60x par secondes

            if self.gameOn:
                if self.j[self.grid.turn] == "human" and clickedOnGrid:
                    clickedOnGrid = False
                    self.grid.clicked(pos)
                    if game_state(self.grid.data) != 0:
                        self.gameOn = False
                        print(game_state(self.grid.data))
                elif self.j[self.grid.turn] == "bot":
                    if hasToThink:
                        botThinks = threading.Thread(target=self.bot.playwise,
                                                            args=(self.grid.data, self.grid.turn, return_list))
                        botThinks.start()
                        hasToThink = False

                    if return_list[0] is not None:
                        self.grid.played(return_list[0])
                        return_list[0] = None
                        hasToThink = True
                        if game_state(self.grid.data) != 0:
                            self.gameOn = False
                            print(game_state(self.grid.data))
            self.draw()
            pygame.display.flip()
        pygame.quit()

    def draw(self):
        self.grid.draw_lines(self.win)
        self.grid.draw_data(self.win)
        for button in self.buttons:
            button.draw(self.win)

    @staticmethod
    def quit():
        pygame.quit()

    def toggle_j2(self):
        if self.j[2] == 'human':
            self.j[2] = 'bot'
            self.j2Button.text = "J2 : bot"
        else:
            self.j[2] = "human"
            self.j2Button.text = "J2 : human"

    def restart(self):
        for i in range(3):
            for j in range(3):
                self.grid.data[i][j] = 0
        self.running = True
        self.gameOn = True
        self.grid.turn = 1
