from core.states import State
from graphics.alignment import Align
from graphics.menu import Menu
from library.point import Point

class StateResults(State):

	def __init__(self, app):
		super().__init__(app, "RESULTS")

		# Create Menu
		self.menu = Menu()
		self.menu.add_option("Play Again", Point(290, 260), lambda: self.app.state_update("GAME"))
		self.menu.add_option("Back to Title", Point(290, 290), lambda: self.app.state_update("TITLE"))

	def on_key_pressed(self, event):

		# Menu Events
		self.menu.on_key_pressed(event)

	def on_start(self, data):

		# Game Data
		self.data = data

	def render(self, gfx):

		# Render Title
		self.render_title(gfx, "RESULTS")

		# Render Celebration
		if self.data["highest"] is True:
			gfx.draw_text("NEW HIGHSCORE!!", Point(self.app.get_dimensions().width - 25, 25), Align.RIGHT, "Inconsolata 22")

		# Render Info
		gfx.draw_text("Time:  %ds" % self.data["time"], Point(25, 100))
		gfx.draw_text("Score: %d" % self.data["score"], Point(25, 130))
		gfx.draw_text("Best:  %d" % self.app.get_score(), Point(25, 160))

		# Render Menu
		self.menu.render(gfx)

		# Render Hint
		self.render_hint(gfx, "Press UP/DOWN to navigate, ENTER to select.")

	def tick(self):
		pass