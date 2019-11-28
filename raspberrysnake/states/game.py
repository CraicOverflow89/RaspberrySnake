from game.engine import GameEngine
from riem.core import Application, State
from riem.input import Action
from riem.graphics import Graphics

class StateGame(State):

	def __init__(self, app: Application) -> None:
		super().__init__(app)
		self.engine = GameEngine(app, self)

	def on_action(self, action: Action) -> None:
		self.engine.on_action(action)

	def render(self, gfx: Graphics) -> None:
		self.engine.render(gfx)

	def tick(self) -> None:
		self.engine.tick()