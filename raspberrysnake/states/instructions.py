from riem.core import Application, State
from riem.graphics import Align, Graphics
from riem.input import Action
from riem.library import Point

class StateInstructions(State):

	def __init__(self, app: Application) -> None:
		super().__init__(app)

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

	def on_action(self, action: Action) -> None:

		# Title State
		self.app.state_revert()

	def render(self, gfx: Graphics) -> None:

		# Render Title
		self.render_title(gfx, "HOW TO PLAY")

		# Render Info
		for x in range(len(self.info)):
			gfx.draw_text(self.info[x], Point(25, x * 30 + 100))

		# Render Hint
		self.render_hint(gfx, "Press any key to return to title.")

	def tick(self) -> None:
		pass