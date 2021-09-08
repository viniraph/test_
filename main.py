import pygame as pg
from game.game import Game
from game.config import *

def main():

    running = True
    playing = True

    pg.init()
    screen = pg.display.set_mode((WIDTH,HEIGHT))
    clock = pg.time.Clock()

    game = Game(screen,clock)

    while running:

        while playing:
            game.run()

main()