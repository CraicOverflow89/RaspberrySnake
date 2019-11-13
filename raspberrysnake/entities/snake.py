from entities.entity import Entity
from library.dimensions import Dimensions
from library.point import Point

class Snake(Entity):

	def __init__(self, position):
		super().__init__(position, Dimensions(32, 32))
		#self.direction = NORTH

	def face(self, direction):
		self.direction = direction

	def grow(self):
		pass
		# NOTE: tail gets longer due to fruit being eaten

	def move(self):
		pass

	def render(self, gfx):
		gfx.draw_rect(Point(self.position.x * self.size.width, self.position.y * self.size.height), self.size, "blue", True)