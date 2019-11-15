from game.entities.entity import Entity
from graphics.images import ImageLoader
from library.dimensions import Dimensions
from library.point import Point
import random

class Obstacle(Entity):

	# Constants
	image_list = ["bush_0", "stone_0"]

	def __init__(self, position, image = None):
		super().__init__(position, Dimensions(32, 32))
		if image is None:
			image = Obstacle.image_list[random.randint(0, len(Obstacle.image_list)) - 1]
		self.image = image

	def render(self, gfx):
		gfx.draw_image(ImageLoader.load("obstacle/%s" % self.image), self.position * Point(self.size.width, self.size.height))

	def tick(self):
		pass