from core.states import State
from graphics.images import ImageLoader
from graphics.point import Point
from tkinter import *

class StateTitle(State):

	def __init__(self, app):
		super().__init__(app, "TITLE")

	def render(self, gfx):

		# Render Logo
		gfx.draw_image(ImageLoader.load("logo"), Point(160, 160))

		# Render Version
		gfx.draw_text("Version %s" % self.app.getVersion(), Point(10, self.app.getDimensions().height - 25))

	def tick(self):
		pass