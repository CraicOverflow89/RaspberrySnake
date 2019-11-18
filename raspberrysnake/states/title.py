from core.states import State
from graphics.alignment import Align
from graphics.images import ImageLoader
from graphics.menu import Menu
from library.dimensions import Dimensions
from library.point import Point

class StateTitle(State):

	def __init__(self, app):
		super().__init__(app, "TITLE")
		self.menu = Menu()
		self.menu.add_option("Start", Point(290, 260), lambda: self.app.state_update("GAME"))
		self.menu.add_option("How to Play", Point(290, 290), lambda: self.app.state_update("INSTRUCTIONS", True))
		self.menu.add_option("About", Point(290, 320), lambda: self.app.state_update("ABOUT", True))
		self.menu.add_option("Exit", Point(290, 350), lambda: self.app.terminate())

	def on_action(self, action):

		# Menu Events
		self.menu.on_action(action)

	def on_revert(self, data):

		# Reset Cursor
		self.menu.set_cursor()

	def render(self, gfx):

		# Render Logo
		gfx.draw_image(ImageLoader.load("logo_solid"), Point(self.app.get_dimensions().width / 2, 40), Align.MIDDLE)

		# Render Menu
		self.menu.render(gfx)

		# Render Hint
		self.render_hint(gfx, "Press UP/DOWN to navigate, ENTER to select.")

	def tick(self):
		pass