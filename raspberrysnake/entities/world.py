from library.point import Point

class World:

	def __init__(self, size):
		self.size = size

	def getDimensions(self):
		return self.size

	def render(self, gfx):

		# Render Border
		gfx.draw_rect(Point(0, 0), self.size * 32, "white", False)