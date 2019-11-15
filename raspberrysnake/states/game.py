from core.states import State
from game.engine import GameEngine

class StateGame(State):

	def __init__(self, app):
		super().__init__(app, "GAME")
		self.engine = GameEngine(app, self)

	def on_key_pressed(self, event):
		self.engine.on_key_pressed(event)

	def render(self, gfx):
		self.engine.render(gfx)

	def tick(self):
		self.engine.tick()