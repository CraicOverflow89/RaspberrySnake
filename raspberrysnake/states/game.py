from core.states import State
from entities.fruit import Fruit
from entities.obstacle import Obstacle
from entities.snake import Snake
from entities.world import World
from graphics.alignment import Align
from library.dimensions import Dimensions
from library.direction import Direction
from library.list import ArrayList
from library.point import Point
import random
import time

class StateGame(State):

	# Constants
	world_pos = Point(32, 48)
	directional_keys = {
		37: Direction.WEST,
		38: Direction.NORTH,
		39: Direction.EAST,
		40: Direction.SOUTH,
		111: Direction.NORTH,
		113: Direction.WEST,
		114: Direction.EAST,
		116: Direction.SOUTH
	}

	def __init__(self, app):
		super().__init__(app, "GAME")
		self.time_s = time.time()
		self.world = World(Dimensions(18, 13))
		self.paused = False
		self.score = 0
		self.snake = Snake(self.world)
		self.fruit = ArrayList(Fruit(Point(2, 7), "apple_R"), Fruit(Point(9, 5), "apple_G"))
		self.obstacle = ArrayList(Obstacle(Point(0, 2), "stone_0"), Obstacle(Point(4, 7), "bush_0"))

	def finish(self):
		# NOTE: would be better to freeze animations for a moment before updating state

		# Record Score
		new_highscore = self.app.new_score(self.score)

		# Results State
		self.app.state_update("RESULTS", False, {
			"score": self.score,
			"time": time.time() - self.time_s,
			"highest": new_highscore
		})

	def fruit_collect(self, fruit):

		# Update Score
		self.score += fruit.get_score()

		# Snake Grow
		self.snake.grow()

		# Remove Fruit
		self.fruit = self.fruit.remove(fruit)

		# Spawn Fruit
		self.fruit_spawn()

	def fruit_spawn(self):

		# Spawn Locations
		snake_point = self.snake.get_position_list()
		fruit_point = self.fruit.map(lambda it: it.get_position())
		obstacle_point = self.obstacle.map(lambda it: it.get_position())
		spawn_point = self.world.get_position_list().reject(lambda it: snake_point.contains(it)).reject(lambda it: fruit_point.contains(it))
		spawn_point = spawn_point.get(random.randint(0, spawn_point.size() - 1))

		# Create Fruit
		self.fruit.add(Fruit(spawn_point))

	def on_key_pressed(self, event):

		# Game Paused
		if self.paused is True:
			if event.keycode == 13 or event.keycode == 36:
				self.paused = False
			return

		# Pause Game
		if event.keycode == 13 or event.keycode == 36:
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
			gfx.draw_text("PAUSED", Point(self.app.get_dimensions().width / 2, self.app.get_dimensions().height / 2), Align.CENTER)

	def render_game(self, gfx):

		# Render Snake
		self.snake.render(gfx)

		# Render Fruit
		self.fruit.each(lambda it: it.render(gfx))

		# Render Obstacles
		self.obstacle.each(lambda it: it.render(gfx))

		# Render World
		self.world.render(gfx)

	def tick(self):

		# Game Paused
		if self.paused is True:
			return

		# Snake Tick
		if self.snake.tick():

			# Snake Collision
			self.finish()

		# Encounter Fruit
		fruit_match = self.fruit.first(lambda it: it.get_position() == self.snake.get_position())
		if fruit_match is not None: self.fruit_collect(fruit_match)

		# Encounter Obstacle
		if self.obstacle.any(lambda it: it.get_position() == self.snake.get_position()):
			self.finish()