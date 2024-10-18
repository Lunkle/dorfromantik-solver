from src.tile import render_tile

class Map:
    def __init__(self):
        self.tiles = {}

    def add_tile(self, tile, position):
        self.tiles[position] = tile

    def remove_tile(self, position):
        self.tiles.remove(position)

    def render_map(self, canvas, size):
        for position, tile in self.tiles.items():
            row, col = position
            render_tile(canvas, row, col, size, tile)
