from core.states import State
from graphics.alignment import Align
from graphics.menu import Menu
from library.point import Point

class StateAbout(State):

	def __init__(self, app):
		super().__init__(app, "ABOUT")

		# Create Information
		self.info = []
		self.info.append("Version: %s" % self.app.get_version())
		self.info.append("Created: 13/11/2019")
		self.info.append("Updated: 15/11/2019")
		self.info.append("")
		self.info.append("Python3: 3.8.0")
		self.info.append("Tkinter: 8.6")
		self.info.append("")
		self.info.append("Repository")
		self.info.append("https://github.com/CraicOverflow89/RaspberrySnake/")
		self.info.append("")
		self.info.append("Sounds")
		self.info.append("https://www.zapsplat.com/")

	def on_action(self, action):

		# Title State
		self.app.state_revert()

	def render(self, gfx):

		# Render Title
		self.render_title(gfx, "ABOUT")

		# Render Info
		for x in range(len(self.info)):
			gfx.draw_text(self.info[x], Point(25, x * 30 + 100))

		# Render Hint
		self.render_hint(gfx, "Press any key to return to title.")

	def tick(self):
		pass