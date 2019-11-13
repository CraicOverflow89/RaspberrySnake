from core.states import State
from entities.snake import Snake
from library.dimensions import Dimensions
from library.point import Point

class StateGame(State):

	def __init__(self, app):
		super().__init__(app, "GAME")
		self.world_pos = Point(32, 48)
		self.world_size = Dimensions(576, 416)
		self.score = 0
		self.snake = Snake(Point(5, 3))
		self.fruit = []

	def onKeyPressed(self, event):

		# TEMP
		print(event)

	def render(self, gfx):

		# Render Score
		gfx.draw_text("Score %s" % self.score, Point(10, 10))

		# Render Entities
		self.render_entities(gfx.offset_graphics(self.world_pos))

		# Render Border
		gfx.draw_rect(self.world_pos, self.world_size, "white", False)

	def render_entities(self, gfx):

		# Render Snake
		self.snake.render(gfx)

		# Render Fruit
		gfx.draw_rect(Point(32 * 2, 32 * 7), Dimensions(32, 32), "red", True)
		gfx.draw_rect(Point(32 * 9, 32 * 5), Dimensions(32, 32), "red", True)

	def tick(self):

		# Snake Movement
		self.snake.move()