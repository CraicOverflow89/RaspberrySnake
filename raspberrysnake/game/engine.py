from game.entities.fruit import Fruit
from game.entities.obstacle import Obstacle
from game.entities.snake import Snake
from game.world import World
from graphics.alignment import Align
from library.dimensions import Dimensions
from library.direction import Direction
from library.list import ArrayList
from library.point import Point
import random
import time

class GameEngine:

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

	def __init__(self, app, state):
		self.app = app
		self.state = state
		self.time_s = time.time()
		self.paused = False
		self.finish = False
		self.score = 0
		self.world = World(Dimensions(18, 13))
		self.snake = None
		self.fruit = ArrayList()
		self.obstacle = ArrayList()
		self.create_entities()

	def create_entities(self):

		# Create Snake
		self.snake = Snake(self, self.world)

		# Create Friut
		self.fruit_spawn(3)

		# Create Obstacles
		self.obstacle_spawn(6)

	def empty_locations(self):

		# Occupied Locations
		snake_point = self.snake.get_position_list()
		fruit_point = self.fruit.map(lambda it: it.get_position())
		obstacle_point = self.obstacle.map(lambda it: it.get_position())

		# Empty Locations
		return self.world.get_position_list().reject(lambda it: snake_point.contains(it)).reject(lambda it: fruit_point.contains(it))

	def end_game(self):

		# Finished Status
		self.finish = True

		# Record Score
		new_highscore = self.app.new_score(self.score)

		# Create Event
		self.state.add_event(1500, lambda: self.app.state_update("RESULTS", False, {
			"score": self.score,
			"time": time.time() - self.time_s,
			"highest": new_highscore
		}))

	def fruit_collect(self, fruit):

		# Update Score
		self.score += fruit.get_score()

		# Snake Grow
		self.snake.grow()

		# Remove Fruit
		self.fruit = self.fruit.remove(fruit)

		# Spawn Fruit
		self.fruit_spawn()

	def fruit_spawn(self, count = 1):

		# Spawn Locations
		spawn_point = self.empty_locations()

		# Create Fruit
		for x in range(count):
			spawn_final = spawn_point.get(random.randint(0, spawn_point.size() - 1))
			spawn_point = spawn_point.remove(spawn_final)
			self.fruit.add(Fruit(spawn_final))

	def is_obstacle(self, point):
		return self.obstacle.any(lambda it: it.get_position() == point)

	def obstacle_spawn(self, count = 1):

		# Spawn Locations
		spawn_point = self.empty_locations()

		# Create Obstacles
		for x in range(count):
			spawn_final = spawn_point.get(random.randint(0, spawn_point.size() - 1))
			spawn_point = spawn_point.remove(spawn_final)
			self.obstacle.add(Obstacle(spawn_final))

	def on_key_pressed(self, event):

		# Game Finished
		if self.finish is True:
			return

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
		if event.keycode in GameEngine.directional_keys.keys():
			self.snake.face(GameEngine.directional_keys[event.keycode])

	def render(self, gfx):

		# Render Score
		gfx.draw_text("Score %s" % self.score, Point(25, 10))

		# Game Finished
		if self.finish is True:
			gfx.draw_text("GAME OVER!!", Point(self.app.get_dimensions().width - 25, 10), Align.RIGHT)

		# Game Running
		if self.paused is False:

			# Render Game
			self.render_game(gfx.offset_graphics(GameEngine.world_pos))

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

		# Game Finished
		if self.finish is True:
			return

		# Game Paused
		if self.paused is True:
			return

		# Snake Tick
		if self.snake.tick():

			# Snake Collision
			self.end_game()
			return

		# Encounter Fruit
		fruit_match = self.fruit.first(lambda it: it.get_position() == self.snake.get_position())
		if fruit_match is not None: self.fruit_collect(fruit_match)