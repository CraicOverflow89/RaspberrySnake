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
		self.app.state_revert()

	def render(self, gfx):

		# Render Title
		self.render_title(gfx, "HOW TO PLAY")

		# Render Info
		for x in range(len(self.info)):
			gfx.draw_text(self.info[x], Point(25, x * 30 + 100))

		# Render Hint
		self.render_hint(gfx, "Press any key to return to title.")

	def tick(self):
		pass