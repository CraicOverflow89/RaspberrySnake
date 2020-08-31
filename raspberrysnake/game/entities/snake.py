from game.entities.entity import Entity
from game.world import World
from riem.graphics import Graphics, ImageLoader
from riem.library import ArrayList, Dimensions, Direction, Point
from typing import Any

class Snake(Entity):

	def __init__(self, game: Any, world: World) -> None:
		# NOTE: cannot specify game as GameEngine due to partial initialisation
		self.game = game
		self.world = world
		Snake.tileset_data = self._create_tileset()
		self.body = self._create_body()
		self.direction = Direction.WEST
		self.direction_next = None
		self.grow_next = False
		super().__init__(self.body.first().get_position(), Dimensions(32, 32))

	def _create_body(self) -> ArrayList:

		# Create Result
		result: list = []

		# Append Head
		result.append(SnakePieceHead(self, Point(5, 3), Direction.WEST))

		# Append Body
		result.append(SnakePieceBody(self, Point(6, 3), Direction.WEST, Direction.EAST))
		result.append(SnakePieceBody(self, Point(7, 3), Direction.WEST, Direction.SOUTH))
		result.append(SnakePieceBody(self, Point(7, 4), Direction.NORTH, Direction.SOUTH))
		result.append(SnakePieceBody(self, Point(7, 5), Direction.NORTH))

		# Return Result
		return ArrayList(result)

	def _create_tileset(self):

		# Create Result
		result: Dict = {}

		# Load Logic
		def add(key: str, point: Point):
			result[key] = ImageLoader.load("snake/tileset", Dimensions(32, 32), point)

		# Load Pieces
		add("body_EN", Point(0, 2))
		add("body_ES", Point(1, 2))
		add("body_EW", Point(0, 3))
		add("body_NE", Point(0, 2))
		add("body_NS", Point(1, 3))
		add("body_NW", Point(2, 2))
		add("body_SE", Point(1, 2))
		add("body_SN", Point(3, 3))
		add("body_SW", Point(3, 2))
		add("body_WE", Point(2, 3))
		add("body_WN", Point(2, 2))
		add("body_WS", Point(3, 2))
		add("head_E", Point(0, 0))
		add("head_N", Point(1, 0))
		add("head_S", Point(2, 0))
		add("head_W", Point(3, 0))
		add("tail_E", Point(0, 1))
		add("tail_N", Point(1, 1))
		add("tail_S", Point(2, 1))
		add("tail_W", Point(3, 1))

		# Return Result
		return result

	def face(self, direction: Direction) -> None:
		if direction != World.get_direction_opposite(self.direction):
			self.direction_next = direction

	def get_position_list(self) -> ArrayList:

		# Create Result
		result: ArrayList = ArrayList()

		# Actual Body
		result = result.add_all(self.body.map(lambda it: it.get_position()))

		# Spaces Ahead
		target: Point = self.game.get_position_adjacent(self.body.first().get_position(), self.direction)
		result = result.add(target)
		result = result.add(self.game.get_position_adjacent(target, self.direction))

		# Return Positions
		return result

	def grow(self) -> None:
		self.grow_next = True

	def render(self, gfx: Graphics) -> None:
		self.body.each(lambda it: it.render(gfx))

	def tick(self) -> None:

		# Target Direction
		if self.direction_next is None:
			self.direction_next = self.direction

		# Calculate Target
		target: Point = self.game.get_position_adjacent(self.body.first().get_position(), self.direction_next)

		# Body Collision
		if target in self.body.map(lambda it: it.get_position()):
			return True

		# Boundary Collision
		if not (self.world.get_dimensions() - 1).contains(target):
			return True

		# Obstacle Collision
		if self.game.is_obstacle(target):
			return True

		# Update Direction
		self.direction = self.direction_next
		self.direction_next = None

		# Update Body
		self.body = self.update_body(target)
		self.position = self.body.first().get_position()

		# No Encounter
		return False

	def update_body(self, target: Point) -> ArrayList:

		# Create Body
		result: List[SnakePiece] = [SnakePieceHead(self, target, self.direction)]
		result.append(SnakePieceBody(self, self.body.get(0).get_position(), self.direction, World.get_direction_to(self.body.get(0).get_position(), self.body.get(1).get_position())))

		# Handle Growth
		if self.grow_next is True:
			copy_body = self.body.size() - 1
			tail_position = self.body.get(self.body.size() - 1).get_position()
			tail_previous = self.body.get(self.body.size() - 2).get_position()
			self.grow_next = False
		else:
			copy_body = self.body.size() - 2
			tail_position = self.body.get(self.body.size() - 2).get_position()
			tail_previous = self.body.get(self.body.size() - 3).get_position()

		# Create Body
		for x in range(1, copy_body):
			result.append(self.body.get(x))

		# Create Tail
		result.append(SnakePieceBody(self, tail_position, World.get_direction_to(tail_position, tail_previous)))

		# Return Result
		return ArrayList(result)

class SnakePiece():

	def __init__(self, snake: Snake, position: Point, type: str, image str) -> None:
		self.snake = snake
		self.position = position
		self.image = "%s_%s" % (type, image)

	def get_position(self) -> Point:
		return self.position

	def render(self, gfx: Graphics) -> None:
		gfx.draw_image(Snake.tileset_data[self.image], self.position * Point(self.snake.size.width, self.snake.size.height))

class SnakePieceBody(SnakePiece):

	def __init__(self, snake: Snake, position: Point, direction_prev: Direction, direction_next: Direction = None) -> None:
		if direction_next is None:
			type: str = "tail"
			image: str = World.get_direction_char(direction_prev)
		else:
			type: str = "body"
			image: str = "".join([World.get_direction_char(direction_prev), World.get_direction_char(direction_next)])
		super().__init__(snake, position, type, image)

class SnakePieceHead(SnakePiece):

	def __init__(self, snake: Snake, position: Point, direction: Direction) -> None:
		super().__init__(snake, position, "head", World.get_direction_char(direction))
