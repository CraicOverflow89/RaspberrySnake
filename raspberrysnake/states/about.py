from core.application import Application
from core.states import State
from graphics.alignment import Align
from graphics.images import ImageLoader
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

	def onKeyPressed(self, event):

		# Title State
		self.app.stateRevert()

	def render(self, gfx):

		# Render Logo
		gfx.draw_image(ImageLoader.load("logo"), Point(160, 40))

		# Render Info
		for x in range(len(self.info)):
			gfx.draw_text(self.info[x], Point(60, x * 30 + 260))

		# Render Version
		gfx.draw_text("Version %s" % Application.getVersion(), Point(10, Application.getDimensions().height - 25))

		# Render Hint
		gfx.draw_text("Press any key to return.", Point(Application.getDimensions().width - 10, Application.getDimensions().height - 25), Align.RIGHT)

	def tick(self):
		pass