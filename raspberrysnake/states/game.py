from core.application import Application
from core.states import State
from entities.fruit import Fruit
from entities.snake import Snake
from library.dimensions import Dimensions
from library.direction import Direction
from library.point import Point

# TEMP
import sys

class StateGame(State):

	# Constants
	world_pos = Point(32, 48)
	world_size = Dimensions(18, 13)
	directional_keys = {
		37: Direction.WEST,
		38: Direction.NORTH,
		39: Direction.EAST,
		40: Direction.SOUTH
	}

	def __init__(self, app):
		super().__init__(app, "GAME")
		self.paused = False
		self.score = 0
		self.snake = Snake()
		self.fruit = [Fruit(Point(2, 7)), Fruit(Point(9, 5))]

	def onKeyPressed(self, event):

		# Game Paused
		if self.paused is True:
			if event.keycode == 13:
				self.paused = False
			return

		# Pause Game
		if event.keycode == 13:
			self.paused = True
			return

		# Face Direction
		if event.keycode in StateGame.directional_keys.keys():
			self.snake.face(StateGame.directional_keys[event.keycode])

	def render(self, gfx):

		# Render Score
		gfx.draw_text("Score %s" % self.score, Point(10, 10))

		# Game Running
		if self.paused is False:

			# Render Entities
			self.render_entities(gfx.offset_graphics(StateGame.world_pos))

			# Render Border
			gfx.draw_rect(StateGame.world_pos, StateGame.world_size * 32, "white", False)

		# Game Paused
		else:
			gfx.draw_text("PAUSED", Point(Application.getDimensions().width / 2, Application.getDimensions().height / 2), True)

	def render_entities(self, gfx):

		# Render Snake
		self.snake.render(gfx)

		# Render Fruit
		for fruit in self.fruit:
			fruit.render(gfx)

	def tick(self):

		# Game Paused
		if self.paused is True:
			return

		# Snake Movement
		if self.snake.move():

			# Encountered Body
			print("encountered body!")
			sys.exit()
			# NOTE: this obviously needs to freeze animations then update state to show final score

		# NOTE: also need to handle hitting the world boundary

		# Collect Fruit
		# NOTE: match fruit entity where location is that of snake head
		#       if match exists then collect fruit (remove it), add score and invoke snake.grow()