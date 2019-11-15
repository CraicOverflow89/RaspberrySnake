from library.list import ArrayList
from library.direction import Direction
from library.point import Point

class World:

	def __init__(self, size):
		self.size = size

	def get_dimensions(self):
		return self.size

	def get_direction_char(direction):
		return {
			Direction.EAST: "E",
			Direction.NORTH: "N",
			Direction.SOUTH: "S",
			Direction.WEST: "W"
		}[direction]

	def get_direction_to(source, target):
		if target.x < source.x:
			return Direction.WEST
		elif target.x > source.x:
			return Direction.EAST
		elif target.y < source.y:
			return Direction.NORTH
		else:
			return Direction.SOUTH

	def get_direction_opposite(direction):
		return {
			Direction.EAST: Direction.WEST,
			Direction.NORTH: Direction.SOUTH,
			Direction.SOUTH: Direction.NORTH,
			Direction.WEST: Direction.EAST
		}[direction]

	def get_position_list(self):
		result = []
		for x in range(self.size.width):
			for y in range(self.size.height):
				result.append(Point(x, y))
		return ArrayList(result)

	def render(self, gfx):

		# Render Border
		gfx.draw_rect(Point(0, 0), self.size * 32, "white", False)