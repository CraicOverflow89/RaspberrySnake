from riem.core import Application, State
from riem.graphics import Align, Graphics, ImageLoader, Menu
from riem.input import Action
from riem.library import Dimensions, Point
from typing import Dict

class StateTitle(State):

	def __init__(self, app: Application) -> None:
		super().__init__(app)
		self.menu = Menu()
		self.menu.add_option("Start", Point(290, 260), lambda: self.app.state_update("StateGame"))
		self.menu.add_option("How to Play", Point(290, 290), lambda: self.app.state_update("StateInstructions", True))
		self.menu.add_option("About", Point(290, 320), lambda: self.app.state_update("StateAbout", True))
		self.menu.add_option("Exit", Point(290, 350), lambda: self.app.terminate())

	def on_action(self, action: Action) -> None:

		# Menu Events
		self.menu.on_action(action)

	def on_revert(self, data: Dict) -> None:

		# Reset Cursor
		self.menu.set_cursor()

	def render(self, gfx: Graphics) -> None:

		# Render Logo
		gfx.draw_image(ImageLoader.load("brand/game_logo"), Point(self.app.get_dimensions().width / 2, 40), Align.MIDDLE)

		# Render Menu
		self.menu.render(gfx)

		# Render Hint
		self.render_hint(gfx, "Press UP/DOWN to navigate, ENTER to select.")

	def tick(self) -> None:
		pass