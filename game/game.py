import pygame as pg
import sys
from .config import FPS, TILE_SIZE
from .world import World

class Game:

    def __init__(self,screen,clock):
        self.screen = screen
        self.clock = clock
        self.width, self.height = self.screen.get_size()

        self.world = World(10,10,self.width, self.height)


    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def update(self):
        pass

    def draw(self):
        self.screen.fill((150,150,150))
        
        '''
        Desenha o grid isometrico,
        p: é uma lista com os pontos em coordedas isometricas
        pcor: pontos corrigidos devido ao sistema de origem do pygame

        '''

        for x in range(self.world.grid_length_x):
            for y in range(self.world.grid_length_y):

                '''
                Loop de desenho, desenha a linha primeiro e depois a coluna
                '''

                #sq = self.world.world[x][y]["cart_rect"]

                p = self.world.world[x][y]["iso_poly"]
                pcor = [(x + self.width/2 , y + self.height/6) for x,y in p]

                render_pos = self.world.world[x][y]['render_pos']
                self.screen.blit(self.world.tiles['grass'],(render_pos[0]+self.width/2, render_pos[1]+self.height/6))
                
                
                pg.draw.polygon(self.screen,(0,160,0),pcor,0)
               # pg.draw.polygon(self.screen,(255,0,0),pcor,1)

        self.screen.blit(self.world.tiles['rockflat'],(1 * TILE_SIZE + self.width/2, 3 * TILE_SIZE + self.height/6))

        pg.display.flip()