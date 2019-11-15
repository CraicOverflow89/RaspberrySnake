from library.list import ArrayList
from library.point import Point

class World:

	def __init__(self, size):
		self.size = size

	def get_dimensions(self):
		return self.size

	def get_position_list(self):
		result = []
		for x in range(self.size.width):
			for y in range(self.size.height):
				result.append(Point(x, y))
		return ArrayList(result)

	def render(self, gfx):

		# Render Border
		gfx.draw_rect(Point(0, 0), self.size * 32, "white", False)