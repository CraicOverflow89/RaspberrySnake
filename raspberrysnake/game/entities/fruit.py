from game.entities.entity import Entity
from riem.graphics import ImageLoader
from riem.library import Dimensions, Point
import random

class Fruit(Entity):

	# Constants
	image_list = ["apple_G", "apple_R", "banana_Y"]

	def __init__(self, position, image = None, score = 50):
		super().__init__(position, Dimensions(32, 32))
		if image is None:
			image = Fruit.image_list[random.randint(0, len(Fruit.image_list)) - 1]
		self.image = image
		self.score = score

	def get_score(self):
		return self.score

	def render(self, gfx):
		gfx.draw_image(ImageLoader.load("fruit/%s" % self.image), self.position * Point(self.size.width, self.size.height))