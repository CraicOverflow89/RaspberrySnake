from core.application import Application
from core.states import State
from graphics.alignment import Align
from library.point import Point

class StateResults(State):

	def __init__(self, app):
		super().__init__(app, "RESULTS")

		# Create Menu
		self.menu = Menu()
		self.menu.add_option("Retry", Point(290, 260), lambda: self.app.stateUpdate(StateGame))
		self.menu.add_option("Title", Point(290, 290), lambda: self.app.stateUpdate(StateTitle))

	def on_key_pressed(self, event):

		# Menu Events
		self.menu.on_key_pressed(event)

	def on_start(self, data):

		# Game Data
		self.data = data

	def render(self, gfx):

		# Render Title
		gfx.draw_text("RESULTS", Point(25, 25), Align.LEFT, "Inconsolata 22")

		# Render Info
		gfx.draw_text("Score: %d" % self.data["score"], Point(25, 100))
		gfx.draw_text("Time:  %ds" % self.data["time"], Point(25, 130))

		# Render Menu
		self.menu.render(gfx)

		# Render Version
		gfx.draw_text("Version %s" % Application.getVersion(), Point(10, Application.getDimensions().height - 25))

		# Render Hint
		gfx.draw_text("Press UP/DOWN to navigate, ENTER to select.", Point(Application.getDimensions().width - 10, Application.getDimensions().height - 25), Align.RIGHT)

	def tick(self):
		pass