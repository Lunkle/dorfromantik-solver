import tkinter as tk
import math

def draw_hexagon(canvas, x, y, size, color):
    angle = math.pi / 3
    points = [
        (x + size * math.cos(i * angle), y + size * math.sin(i * angle)) for i in range(6)
    ]
    canvas.create_polygon(points, outline='black', fill=color, width=2)

def create_hexagon_tiling(canvas, rows, cols, size):
    for row in range(rows):
        for col in range(cols):
            x = col * size * 1.5
            y = row * size * math.sqrt(3) + (col % 2) * size * math.sqrt(3) / 2
            draw_hexagon(canvas, x, y, size, 'white')

root = tk.Tk()
root.title("Hexagon Tiling")

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

create_hexagon_tiling(canvas, 10, 10, 30)

root.mainloop()
