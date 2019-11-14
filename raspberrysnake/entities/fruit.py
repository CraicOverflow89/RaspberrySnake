from entities.entity import Entity
from graphics.images import ImageLoader
from library.dimensions import Dimensions
from library.point import Point
import random

class Fruit(Entity):

	# Constants
	image_list = ["apple_G", "apple_R", "banana_Y"]

	def __init__(self, position, image = None):
		super().__init__(position, Dimensions(32, 32))
		if image is None:
			image = Fruit.image_list[random.randint(0, len(Fruit.image_list)) - 1]
		self.image = image

	def get_score(self):
		return 50
		# NOTE: basic score for now

	def render(self, gfx):
		gfx.draw_image(ImageLoader.load("fruit/%s" % self.image), self.position * Point(self.size.width, self.size.height))