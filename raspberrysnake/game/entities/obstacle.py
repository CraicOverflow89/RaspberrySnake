from game.entities.entity import Entity
from riem.graphics import ImageLoader
from riem.library import Dimensions, Point
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