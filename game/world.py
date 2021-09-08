import pygame as pg
from .config import TILE_SIZE

class World:

    def __init__(self, grid_length_x, grid_length_y, width, height):
        self.grid_length_x = grid_length_x
        self.grid_length_y = grid_length_y
        self.width = width
        self.height = height

        self.world = self.create_world()
        self.tiles = self.load_images()

    def create_world(self):
        '''Em cada x(linha) é colocado 10y(coluna) na lista'''

        world = []

        
        for grid_x in range(self.grid_length_x):
            world.append([])
            for grid_y in range(self.grid_length_y):
                world_tile = self.grid_to_world(grid_x, grid_y)
                world[grid_x].append(world_tile)

        #print(world)
        return world

    def grid_to_world(self, grid_x, grid_y):
        '''rect: são 4 pontos que representam os verticies do quadrado'''
        rect = [
            (grid_x * TILE_SIZE, grid_y * TILE_SIZE),
            (grid_x * TILE_SIZE + TILE_SIZE, grid_y * TILE_SIZE),
            (grid_x * TILE_SIZE + TILE_SIZE, grid_y * TILE_SIZE + TILE_SIZE),
            (grid_x * TILE_SIZE, grid_y * TILE_SIZE + TILE_SIZE)
        ]
        
        '''iso_poly: os mesmo pontos do rect mas traduzidos para uma coordenada isometrica'''
        iso_poly = [self.cart_to_iso(x, y) for x, y in rect]

        '''Pega o vertices na parte superior esquerda para realizar o render isometrico'''
        minx = min([x for x,y in iso_poly])
        miny = min([y for x,y in iso_poly])

        '''Dicionario de saida'''
        out = {
            "grid": [grid_x, grid_y],
            "cart_rect": rect,
            "iso_poly": iso_poly,
            "render_pos": [minx,miny]
        }
        #print(out)
        return out

    def cart_to_iso(self, x, y):
        iso_x = x - y
        iso_y = (x + y)/2
        return iso_x, iso_y

    def load_images(self):

        grass = pg.image.load('assets/img/grass.png')
        flatRockGrass = pg.image.load('assets/img/rockFlatGrass_W.png')
        flatRockGrass = pg.transform.scale(flatRockGrass,(TILE_SIZE*3,TILE_SIZE*3))


        return {'grass': grass,
                'rockflat': flatRockGrass}