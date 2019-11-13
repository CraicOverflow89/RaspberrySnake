from core.states import State
from graphics.point import Point

class StateGame(State):

	def __init__(self, app):
		super().__init__(app, "GAME")

	def onKeyPressed(self, event):

		# TEMP
		print(event)

	def render(self, gfx):

		# TEMP
		gfx.draw_text("GAME STATE", Point(10, 10))

	def tick(self):
		pass