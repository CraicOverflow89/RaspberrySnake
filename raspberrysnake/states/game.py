from game.engine import GameEngine
from riem.core import State

class StateGame(State):

	def __init__(self, app):
		super().__init__(app, "GAME")
		self.engine = GameEngine(app, self)

	def on_action(self, action):
		self.engine.on_action(action)

	def render(self, gfx):
		self.engine.render(gfx)

	def tick(self):
		self.engine.tick()