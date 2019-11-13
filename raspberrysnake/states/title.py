from core.states import State
from graphics.images import ImageLoader
from tkinter import *

class StateTitle(State):

	def __init__(self, name):
		super().__init__(name)

	def render(self, canvas):

		# Create Logo
		logo = canvas.create_image(160, 160, image = ImageLoader.load("logo"), anchor = NW)