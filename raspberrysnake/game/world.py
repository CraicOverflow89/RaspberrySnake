from riem.graphics import Graphics
from riem.library import ArrayList, Dimensions, Direction, Point

class World:

	def __init__(self, size) -> None:
		self.size = size

	def get_dimensions(self) -> Dimensions:
		return self.size

	def get_direction_char(direction: Direction) -> str:
		return {
			Direction.EAST: "E",
			Direction.NORTH: "N",
			Direction.SOUTH: "S",
			Direction.WEST: "W"
		}[direction]

	def get_direction_to(source: Point, target: Point) -> Direction:
		if target.x < source.x:
			return Direction.WEST
		elif target.x > source.x:
			return Direction.EAST
		elif target.y < source.y:
			return Direction.NORTH
		else:
			return Direction.SOUTH

	def get_direction_opposite(direction: Direction) -> Direction:
		return {
			Direction.EAST: Direction.WEST,
			Direction.NORTH: Direction.SOUTH,
			Direction.SOUTH: Direction.NORTH,
			Direction.WEST: Direction.EAST
		}[direction]

	def get_position_list(self) -> ArrayList:
		result = []
		for x in range(self.size.width):
			for y in range(self.size.height):
				result.append(Point(x, y))
		return ArrayList(result)

	def render(self, gfx: Graphics) -> None:

		# Render Border
		gfx.draw_rect(Point(0, 0), self.size * 32, "white", False)