import tkinter as tk

class Graphics:

	def __init__(self, canvas):
		self.canvas = canvas

	def draw_image(self, image, position):
		self.canvas.create_image(position.x, position.y, image = image, anchor = tk.NW)

	def draw_rect(self, position, size, fill):
		self.canvas.create_rectangle(position.x, position.y, size.width, size.height, fill = fill)

	def draw_text(self, text, position):
		self.canvas.create_text(position.x, position.y, text = text, font = "Inconsolata 14", fill = "white", anchor = tk.NW)