from core.application import Application
from core.states import State
from graphics.alignment import Align
from library.point import Point

class StateInstructions(State):

	def __init__(self, app):
		super().__init__(app, "INSTRUCTIONS")

		# Create Information
		self.info = []
		self.info.append("Movement")
		self.info.append("Press the UP/DOWN/LEFT/RIGHT keys to alter direction.")
		self.info.append("")
		self.info.append("Fruit")
		self.info.append("Collect fruit to build up the highest score you can.")
		self.info.append("")
		self.info.append("Collision")
		self.info.append("It's game over if you hit the your tail or the boundary.")

	def on_key_pressed(self, event):

		# Title State
		self.app.stateRevert()

	def render(self, gfx):

		# Render Title
		gfx.draw_text("HOW TO PLAY", Point(25, 25), Align.LEFT, "Inconsolata 22")

		# Render Info
		for x in range(len(self.info)):
			gfx.draw_text(self.info[x], Point(25, x * 30 + 100))

		# Render Version
		gfx.draw_text("Version %s" % Application.getVersion(), Point(10, Application.getDimensions().height - 25))

		# Render Hint
		gfx.draw_text("Press any key to return to title.", Point(Application.getDimensions().width - 10, Application.getDimensions().height - 25), Align.RIGHT)

	def tick(self):
		pass