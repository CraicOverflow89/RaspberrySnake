from graphics.alignment import Align
from library.point import Point
import tkinter as tk

class Graphics:

	# Constants
	text_default = {
		"font": "Inconsolata 14",
		"colour": "white"
	}

	def __init__(self, canvas, offset = Point(0, 0)):
		self.canvas = canvas
		self.offset = offset

	def draw_image(self, image, position):

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

	def draw_text(self, text, position, align = Align.LEFT, font = None, colour = None, shadow = None):

		# Apply Offset
		position = position + self.offset

		# Anchor Position
		anchor = {
			Align.LEFT: tk.NW,
			Align.CENTER: tk.CENTER,
			Align.RIGHT: tk.NE
		}[align]

		# Default Font
		if font is None: font = Graphics.text_default["font"]

		# Default Colour
		if colour is None: colour = Graphics.text_default["colour"]

		# Render Shadow
		if shadow is not None:
			self.canvas.create_text(position.x + 1, position.y + 1, text = text, font = font, fill = shadow, anchor = anchor)

		# Render Text
		self.canvas.create_text(position.x, position.y, text = text, font = font, fill = colour, anchor = anchor)

	def offset_graphics(self, offset):
		return Graphics(self.canvas, self.offset + offset)