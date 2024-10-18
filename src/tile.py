class Tile:
    def __init__(self, edges):
        self.edges = edges

    def rotate(self):
        self.edges = self.edges[-1:] + self.edges[:-1]
