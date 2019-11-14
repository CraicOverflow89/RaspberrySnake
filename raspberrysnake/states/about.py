from core.application import Application
from core.states import State
from graphics.alignment import Align
from graphics.menu import Menu
from library.point import Point

class StateAbout(State):

	def __init__(self, app):
		super().__init__(app, "ABOUT")

		# Create Information
		self.info = []
		self.info.append("Python3: 3.8.0")
		self.info.append("Tkinter: 8.6")
		self.info.append("")
		self.info.append("Created: 13/11/2019")
		self.info.append("Updated: 14/11/2019")
		self.info.append("")
		self.info.append("Repository")
		self.info.append("https://github.com/CraicOverflow89/RaspberrySnake/")

	def on_key_pressed(self, event):

		# Title State
		self.app.state_revert()

	def render(self, gfx):

		# Render Title
		gfx.draw_text("ABOUT", Point(25, 25), Align.LEFT, "Inconsolata 22")

		# Render Info
		for x in range(len(self.info)):
			gfx.draw_text(self.info[x], Point(25, x * 30 + 100))

		# Render Version
		gfx.draw_text("Version %s" % Application.get_version(), Point(10, Application.get_dimensions().height - 25))

		# Render Hint
		gfx.draw_text("Press any key to return to title.", Point(Application.get_dimensions().width - 10, Application.get_dimensions().height - 25), Align.RIGHT)

	def tick(self):
		pass