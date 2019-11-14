from entities.entity import Entity
from library.dimensions import Dimensions
from library.point import Point

class Fruit(Entity):

	def __init__(self, position):
		super().__init__(position, Dimensions(32, 32))
		#self.image = image
		# NOTE: maybe have a fruit type enum with mapped images

	def getScore(self):
		return 50
		# NOTE: basic score for now

	def render(self, gfx):
		gfx.draw_rect(Point(self.position.x * self.size.width, self.position.y * self.size.height), self.size, "red", True)