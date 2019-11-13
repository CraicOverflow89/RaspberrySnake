from core.states import State
from library.point import Point

class StateGame(State):

	def __init__(self, app):
		super().__init__(app, "GAME")
		self.score = 0
		self.snake = Snake()
		self.fruit = []

	def onKeyPressed(self, event):

		# TEMP
		print(event)

	def render(self, gfx):

		# Render Snake
		self.render_snake(gfx)

		# Render Fruit
		self.render_fruit(gfx)

		# Render Score
		self.render_score(gfx)

	def render_fruit(self, gfx):
		pass

	def render_score(self, gfx):
		gfx.draw_text("Score %s" % self.score, Point(10, 10))

	def render_snake(self, gfx):
		pass

	def tick(self):
		pass