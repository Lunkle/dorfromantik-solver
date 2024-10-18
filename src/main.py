import tkinter as tk
from src.map import render_map

root = tk.Tk()
root.title("Dorfromantik")

canvas = tk.Canvas(root, width=800, height=600)
canvas.pack()

render_map(canvas, 30)

root.mainloop()
