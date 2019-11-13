from entities.entity import Entity
from library.dimensions import Dimensions
from library.point import Point

class Fruit(Entity):

	def __init__(self, position):
		super().__init__(position, Dimensions(32, 32))
		#self.image = image
		# NOTE: maybe have a fruit type enum with mapped images

	def collect(self):
		pass
		# NOTE: need to provide score (is this variable?) and kill this
		#       although that will be done from without

	def render(self, gfx):
		gfx.draw_rect(Point(self.position.x * self.size.width, self.position.y * self.size.height), self.size, "red", True)