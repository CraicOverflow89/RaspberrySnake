from core.application import Application
from core.states import State
from graphics.images import ImageLoader
from tkinter import *

class StateTitle(State):

	def __init__(self, app):
		super().__init__(app, "TITLE")

	def render(self, canvas):

		# Render Logo
		canvas.create_image(160, 160, image = ImageLoader.load("logo"), anchor = NW)
		# NOTE: should use an intermediate class that provides easy access to typical drawing methods
		#       rather than accepting canvas and having to repeat stuff in render methods

		# Render Version
		canvas.create_text(10, self.app.getDimensions().height - 25, text = "Version %s" % self.app.getVersion(), font = "Inconsolata 14", fill = "white", anchor = NW)
		# NOTE: should use an intermediate class that provides easy access to typical drawing methods
		#       rather than accepting canvas and having to repeat stuff in render methods

	def tick(self):
		pass