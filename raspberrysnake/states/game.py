from core.application import Application
from core.states import State
from entities.fruit import Fruit
from entities.snake import Snake
from entities.world import World
from library.dimensions import Dimensions
from library.direction import Direction
from library.list import ArrayList
from library.point import Point

# TEMP
import sys

class StateGame(State):

	# Constants
	world_pos = Point(32, 48)
	directional_keys = {
		37: Direction.WEST,
		38: Direction.NORTH,
		39: Direction.EAST,
		40: Direction.SOUTH
	}

	def __init__(self, app):
		super().__init__(app, "GAME")
		self.world = World(Dimensions(18, 13))
		self.paused = False
		self.score = 0
		self.snake = Snake(self.world)
		self.fruit = ArrayList(Fruit(Point(2, 7)), Fruit(Point(9, 5)))

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

			# Render Game
			self.render_game(gfx.offset_graphics(StateGame.world_pos))

		# Game Paused
		else:
			gfx.draw_text("PAUSED", Point(Application.getDimensions().width / 2, Application.getDimensions().height / 2), True)

	def render_game(self, gfx):

		# Render Snake
		self.snake.render(gfx)

		# Render Fruit
		self.fruit.each(lambda it: it.render(gfx))

		# Render World
		self.world.render(gfx)

	def tick(self):

		# Game Paused
		if self.paused is True:
			return

		# Snake Tick
		if self.snake.tick():

			# Snake Collision
			sys.exit()
			# NOTE: this obviously needs to freeze animations then update state to show final score

		# Encounter Fruit
		fruit_match = self.fruit.first(lambda it: it.getPosition() == self.snake.getPosition())
		if(fruit_match is not None):

			# Update Score
			self.score += fruit_match.getScore()

			# Snake Grow
			self.snake.grow()

			# Remove Fruit
			self.fruit = self.fruit.remove(fruit_match)

			# Spawn Fruit
			# NOTE: can fruit spawn at other times in the game (not just after some is eaten?)