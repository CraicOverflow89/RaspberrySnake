from graphics.alignment import Align
from library.point import Point
import tkinter as tk

class Graphics:

	def __init__(self, canvas, offset = Point(0, 0)):
		self.canvas = canvas
		self.offset = offset

	def draw_image(self, image, position):
		# NOTE: could add optional Align argument

		# Apply Offset
		position = position + self.offset

		# Render Image
		self.canvas.create_image(position.x, position.y, image = image, anchor = tk.NW)

	def draw_rect(self, position, size, colour, fill):

		# Apply Offset
		position = position + self.offset

		# Render Solid
		if fill is True:
			self.canvas.create_rectangle(position.x, position.y, position.x + size.width, position.y + size.height, fill = colour)

		# Render Outline
		else:
			self.canvas.create_rectangle(position.x, position.y, position.x + size.width, position.y + size.height, outline = colour)

	def draw_text(self, text, position, align = Align.LEFT):

		# Apply Offset
		position = position + self.offset

		# Anchor Position
		anchor = {
			Align.LEFT: tk.NW,
			Align.CENTER: tk.CENTER,
			Align.RIGHT: tk.NE
		}[align]

		# Render Text
		self.canvas.create_text(position.x, position.y, text = text, font = "Inconsolata 14", fill = "white", anchor = anchor)

	def offset_graphics(self, offset):
		return Graphics(self.canvas, self.offset + offset)