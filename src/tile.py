from src.main import draw_hexagon
import math

class Tile:
    def __init__(self, edges):
        self.edges = edges

    def rotate(self):
        self.edges = self.edges[-1:] + self.edges[:-1]

    def render_tile(self, canvas, row, col, size):
        color = 'white'  # You can customize the color based on tile properties
        x = col * size * 1.5
        y = row * size * math.sqrt(3) + (col % 2) * size * math.sqrt(3) / 2
        angle = math.pi / 3
        points = [
            (x + size * math.cos(i * angle), y + size * math.sin(i * angle)) for i in range(6)
        ]
        canvas.create_polygon(points, outline='black', fill=color, width=2)
