from game.entities.fruit import Fruit
from game.entities.obstacle import Obstacle
from game.entities.snake import Snake
from game.world import World
from riem.audio import SoundLoader
from riem.core import Application, State
from riem.graphics import Align, Graphics
from riem.input import Action
from riem.library import ArrayList, Dimensions, Direction, Point
from typing import Dict
import random, time

class GameEngine:

	# Constants
	world_pos: Point = Point(32, 48)
	directional_action: Dict[Action, Direction] = {
		Action.DOWN: Direction.SOUTH,
		Action.LEFT: Direction.WEST,
		Action.RIGHT: Direction.EAST,
		Action.UP: Direction.NORTH
	}

	def __init__(self, app: Application, state: State) -> None:
		self.app = app
		self.state = state
		self.time_s = time.time()
		self.paused = False
		self.finish = False
		self.score = 0
		self.world = World(Dimensions(28, 20))
		self.snake = None
		self.fruit = ArrayList()
		self.obstacle = ArrayList()
		self.create_entities()

	def create_entities(self) -> None:

		# Create Snake
		self.snake = Snake(self, self.world)

		# Create Friut
		self.fruit_spawn(3)

		# Create Obstacles
		self.obstacle_spawn(6)

	def empty_locations(self) -> ArrayList:

		# Occupied Locations
		snake_point: ArrayList = self.snake.get_position_list()
		fruit_point: ArrayList = self.fruit.map(lambda it: it.get_position())
		obstacle_point: ArrayList = self.obstacle.map(lambda it: it.get_position())

		# Empty Locations
		return self.world.get_position_list().reject(lambda it: snake_point.contains(it)).reject(lambda it: fruit_point.contains(it)).reject(lambda it: obstacle_point.contains(it))

	def end_game(self) -> None:

		# Play Sound
		SoundLoader.play("collision")

		# Finished Status
		self.finish = True

		# Record Score
		new_highscore: int = self.app.new_score(self.score)

		# Create Event
		self.state.add_event(1500, lambda: self.app.state_update("StateResults", False, {
			"score": self.score,
			"time": time.time() - self.time_s,
			"highest": new_highscore
		}))

	def fruit_collect(self, fruit: Fruit) -> None:

		# Play Sound
		SoundLoader.play("collect")

		# Update Score
		self.score += fruit.get_score()

		# Snake Grow
		self.snake.grow()

		# Remove Fruit
		self.fruit = self.fruit.remove(fruit)

		# Spawn Fruit
		self.fruit_spawn()

	def fruit_spawn(self, count: int = 1) -> None:

		# Spawn Locations
		spawn_point: ArrayList = self.empty_locations()

		# Create Fruit
		for _ in range(count):
			spawn_final: Point = spawn_point.get(random.randint(0, spawn_point.size() - 1))
			spawn_point = spawn_point.remove(spawn_final)
			self.fruit.add(Fruit(spawn_final))

	def get_position_adjacent(self, position: Point, direction: Direction) -> Point:
		return {
			Direction.EAST: position + Point(1, 0),
			Direction.NORTH: position + Point(0, -1),
			Direction.SOUTH: position + Point(0, 1),
			Direction.WEST: position + Point(-1, 0)
		}[direction]

	def is_obstacle(self, point: Point) -> bool:
		return self.obstacle.any(lambda it: it.get_position() == point)

	def obstacle_spawn(self, count: int = 1) -> None:

		# Spawn Locations
		spawn_point: ArrayList = self.empty_locations()

		# Create Obstacles
		for _ in range(count):
			spawn_final: Point = spawn_point.get(random.randint(0, spawn_point.size() - 1))
			spawn_point = spawn_point.remove(spawn_final)
			self.obstacle.add(Obstacle(spawn_final))

	def on_action(self, action: Action) -> None:

		# Game Finished
		if self.finish is True:
			return

		# Game Paused
		if self.paused is True:
			if action == Action.ACTION:
				self.paused = False
			return

		# Pause Game
		if action == Action.ACTION:
			self.paused = True
			return

		# Face Direction
		if action in GameEngine.directional_action.keys():
			self.snake.face(GameEngine.directional_action[action])

	def render(self, gfx: Graphics) -> None:

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
			gfx.draw_text("PAUSED", Point(self.app.get_dimensions().width / 2, self.app.get_dimensions().height / 2), Align.CENTER, "Inconsolata 22")

	def render_game(self, gfx: Graphics) -> None:

		# Render Snake
		self.snake.render(gfx)

		# Render Fruit
		self.fruit.each(lambda it: it.render(gfx))

		# Render Obstacles
		self.obstacle.each(lambda it: it.render(gfx))

		# Render World
		self.world.render(gfx)

	def tick(self) -> None:

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
		fruit_match: ArrayList = self.fruit.first(lambda it: it.get_position() == self.snake.get_position())
		if fruit_match is not None: self.fruit_collect(fruit_match)