from game.entities.entity import Entity
from graphics.images import ImageLoader
from library.dimensions import Dimensions
from library.direction import Direction
from library.list import ArrayList
from library.point import Point

class Snake(Entity):

	# Constants
	direction_map = {
		Direction.EAST: "E",
		Direction.NORTH: "N",
		Direction.SOUTH: "S",
		Direction.WEST: "W"
	}
	direction_opposite = {
		Direction.EAST: Direction.WEST,
		Direction.NORTH: Direction.SOUTH,
		Direction.SOUTH: Direction.NORTH,
		Direction.WEST: Direction.EAST
	}

	def __init__(self, game, world):
		self.game = game
		self.world = world
		self.body = self.create_body()
		self.direction = Direction.WEST
		self.direction_next = None
		self.grow_next = False
		super().__init__(self.body.first().get_position(), Dimensions(32, 32))

	def create_body(self):
		result = []
		result.append(SnakePieceHead(self, Point(5, 3), Direction.WEST))
		result.append(SnakePieceBody(self, Point(6, 3), Direction.WEST, Direction.EAST))
		result.append(SnakePieceBody(self, Point(7, 3), Direction.WEST, Direction.SOUTH))
		result.append(SnakePieceBody(self, Point(7, 4), Direction.NORTH, Direction.SOUTH))
		result.append(SnakePieceBody(self, Point(7, 5), Direction.NORTH))
		return ArrayList(result)

	def direction_to(source, target):
		if target.x < source.x:
			return Direction.WEST
		elif target.x > source.x:
			return Direction.EAST
		elif target.y < source.y:
			return Direction.NORTH
		else:
			return Direction.SOUTH
		# NOTE: this should live in another class

	def face(self, direction):
		if direction != Snake.direction_opposite[self.direction]:
			self.direction_next = direction

	def get_position_list(self):

		# Create Result
		result = ArrayList()

		# Actual Body
		result = result.add_all(self.body.map(lambda it: it.get_position()))

		# Spaces Ahead
		target = self.game.get_position_adjacent(self.body.first().get_position(), self.direction)
		result = result.add(target)
		result = result.add(self.game.get_position_adjacent(target, self.direction))

		# Return Positions
		return result

	def grow(self):
		self.grow_next = True

	def render(self, gfx):
		self.body.each(lambda it: it.render(gfx))

	def tick(self):

		# Target Direction
		if self.direction_next is None:
			self.direction_next = self.direction

		# Calculate Target
		target = self.game.get_position_adjacent(self.body.first().get_position(), self.direction_next)

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

	def update_body(self, target):

		# Create Body
		result = [SnakePieceHead(self, target, self.direction)]
		result.append(SnakePieceBody(self, self.body.get(0).get_position(), self.direction, Snake.direction_to(self.body.get(0).get_position(), self.body.get(1).get_position())))

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
		result.append(SnakePieceBody(self, tail_position, Snake.direction_to(tail_position, tail_previous)))

		# Return Result
		return ArrayList(result)

class SnakePiece():

	def __init__(self, snake, position, type, image):
		self.snake = snake
		self.position = position
		self.image = "%s_%s" % (type, image)

	def get_position(self):
		return self.position

	def render(self, gfx):
		gfx.draw_image(ImageLoader.load("snake/%s" % self.image), self.position * Point(self.snake.size.width, self.snake.size.height))

class SnakePieceBody(SnakePiece):

	def __init__(self, snake, position, direction_prev, direction_next = None):
		if direction_next is None:
			type = "tail"
			image = Snake.direction_map[direction_prev]
		else:
			type = "body"
			image = "".join(sorted((Snake.direction_map[direction_prev], Snake.direction_map[direction_next])))
		super().__init__(snake, position, type, image)

class SnakePieceHead(SnakePiece):

	def __init__(self, snake, position, direction):
		super().__init__(snake, position, "head", Snake.direction_map[direction])