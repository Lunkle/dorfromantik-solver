class Map:
    def __init__(self):
        self.tiles = {}

    def add_tile(self, tile, position):
        self.tiles[position] = tile

    def remove_tile(self, position):
        self.tiles.remove(position)
