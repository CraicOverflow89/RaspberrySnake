from core.application import Application
from core.states import State
from graphics.alignment import Align
from graphics.images import ImageLoader
from graphics.menu import Menu
from library.dimensions import Dimensions
from library.point import Point
from states.about import StateAbout
from states.game import StateGame
from states.instructions import StateInstructions
import sys

class StateTitle(State):

	def __init__(self, app):
		super().__init__(app, "TITLE")
		self.menu = Menu()
		self.menu.add_option("Classic Mode", Point(290, 260), lambda: self.app.stateUpdate(StateGame))
		self.menu.add_option("How to Play", Point(290, 290), lambda: self.app.stateUpdate(StateInstructions, True))
		self.menu.add_option("About", Point(290, 320), lambda: self.app.stateUpdate(StateAbout, True))
		self.menu.add_option("Exit", Point(290, 350), lambda: sys.exit())

	def on_key_pressed(self, event):

		# Menu Events
		self.menu.on_key_pressed(event)

	def onRevert(self, data):

		# Reset Cursor
		self.menu.set_cursor()

	def render(self, gfx):

		# Render Logo
		gfx.draw_image(ImageLoader.load("logo"), Point(160, 40))

		# Render Menu
		self.menu.render(gfx)

		# Render Version
		gfx.draw_text("Version %s" % Application.getVersion(), Point(10, Application.getDimensions().height - 25))

		# Render Hint
		gfx.draw_text("Press UP/DOWN to navigate, ENTER to select.", Point(Application.getDimensions().width - 10, Application.getDimensions().height - 25), Align.RIGHT)

	def tick(self):
		pass