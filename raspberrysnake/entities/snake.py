from entities.entity import Entity
from graphics.images import ImageLoader
from library.dimensions import Dimensions
from library.direction import Direction
from library.list import ArrayList
from library.methods import *
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

	def __init__(self, world):
		self.world = world
		self.body = ArrayList(Point(5, 3), Point(6, 3), Point(7, 3), Point(7, 4), Point(7, 5))
		self.direction = Direction.WEST
		self.direction_next = None
		self.grow_next = False
		super().__init__(self.body.get(0), Dimensions(32, 32))

	def face(self, direction):
		if direction != Snake.direction_opposite[self.direction]:
			self.direction_next = direction

	def get_position_list(self):
		return self.body

	def grow(self):
		self.grow_next = True

	def render(self, gfx):

		# Direction Logic
		def direction_to(source, target):
			if target.x < source.x:
				return Direction.WEST
			elif target.x > source.x:
				return Direction.EAST
			elif target.y < source.y:
				return Direction.NORTH
			else:
				return Direction.SOUTH

		# Render Logic
		def render_piece(image, position):
			gfx.draw_image(ImageLoader.load("snake/%s" % image), position * Point(self.size.width, self.size.height))

		# Render Head
		render_piece("head_%s" % Snake.direction_map[self.direction], self.body.get(0))

		# Render Body
		for x in range(1, self.body.size() - 1):
			pos_this = self.body.get(x)
			char_prev = Snake.direction_map[direction_to(pos_this, self.body.get(x - 1))]
			char_next = Snake.direction_map[direction_to(pos_this, self.body.get(x + 1))]
			render_piece("body_%s" % "".join(sorted((char_prev, char_next))), pos_this)

		# Render Tail
		pos_this = self.body.get(self.body.size() - 1)
		pos_prev = self.body.get(self.body.size() - 2)
		render_piece("tail_%s" % Snake.direction_map[direction_to(pos_this, pos_prev)], pos_this)

	def tick(self):

		# Update Direction
		if self.direction_next is not None:
			self.direction = self.direction_next
			self.direction_next = None

		# Calculate Target
		pos_this = self.body.get(0)
		target = {
			Direction.EAST: pos_this + Point(1, 0),
			Direction.NORTH: pos_this + Point(0, -1),
			Direction.SOUTH: pos_this + Point(0, 1),
			Direction.WEST: pos_this + Point(-1, 0)
		}[self.direction]

		# Encounter Body
		if target in self.body:
			return True

		# Encounter Boundary
		if not (self.world.get_dimensions() - 1).contains(target):
			return True

		# Create Body
		body_new = [target]

		# Iterate Pieces
		for x in range(self.body.size() - 1):
			body_new.append(self.body.get(x))
			# NOTE: might be better to say [target].add_all(body.take(up to grow_next ? size : size -1))

		# Invoke Growth
		if self.grow_next is True:
			body_new.append(self.body.get(self.body.size() - 1))
			self.grow_next = False

		# Update Body
		self.body = ArrayList(body_new)
		self.position = self.body.get(0)

		# No Encounter
		return False