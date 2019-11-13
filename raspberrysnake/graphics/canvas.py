import tkinter as tk

class Graphics:

	def __init__(self, canvas):
		self.canvas = canvas

	def draw_image(self, image, position):
		self.canvas.create_image(position.x, position.y, image = image, anchor = tk.NW)

	def draw_rect(self, position, size, colour, fill):

		# Solid
		if fill is True:
			self.canvas.create_rectangle(position.x, position.y, position.x + size.width, position.y + size.height, fill = colour)

		# Outline
		else:
			self.canvas.create_rectangle(position.x, position.y, position.x + size.width, position.y + size.height, outline = colour)

	def draw_text(self, text, position):
		self.canvas.create_text(position.x, position.y, text = text, font = "Inconsolata 14", fill = "white", anchor = tk.NW)