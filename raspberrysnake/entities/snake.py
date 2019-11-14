from entities.entity import Entity
from graphics.images import ImageLoader
from library.dimensions import Dimensions
from library.direction import Direction
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

	def __init__(self):
		self.body = [Point(5, 3), Point(6, 3), Point(7, 3), Point(7, 4), Point(7, 5)]
		super().__init__(self.body[0], Dimensions(32, 32))
		self.direction = Direction.WEST
		self.grow_next = False

	def face(self, direction):
		if direction != direction_opposite[self.direction]: self.direction = direction

	def getLocation(self):
		return self.body[0]

	def grow(self):
		self.grow_next = True

	def move(self):

		# Calculate Target
		pos_this = self.body[0]
		target = when(self.direction, {
			Direction.EAST: pos_this + Point(1, 0),
			Direction.NORTH: pos_this + Point(0, -1),
			Direction.SOUTH: pos_this + Point(0, 1),
			Direction.WEST: pos_this + Point(-1, 0)
		})

		# Encounter Body
		if target in self.body:
			return True

		# Create Body
		body_new = [target]

		# Iterate Pieces
		for x in range(len(self.body) - 1):
			body_new.append(self.body[x])

		# Invoke Growth
		if self.grow_next is True:
			body_new.append(self.body[len(self.body) - 1])
			self.grow_next = False

		# Update Body
		self.body = body_new
		self.position = self.body[0]

		# No Encounter
		return False

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
			gfx.draw_image(ImageLoader.load("snake/%s" % image), Point(position.x * self.size.width, position.y * self.size.height))

		# Render Head
		render_piece("head_%s" % Snake.direction_map[self.direction], self.body[0])

		# Render Body
		for x in range(1, len(self.body) - 1):
			pos_this = self.body[x]
			char_prev = Snake.direction_map[direction_to(pos_this, self.body[x - 1])]
			char_next = Snake.direction_map[direction_to(pos_this, self.body[x + 1])]
			render_piece("body_%s" % "".join(sorted((char_prev, char_next))), pos_this)

		# Render Tail
		pos_this = self.body[len(self.body) - 1]
		pos_prev = self.body[len(self.body) - 2]
		render_piece("tail_%s" % Snake.direction_map[direction_to(pos_this, pos_prev)], pos_this)