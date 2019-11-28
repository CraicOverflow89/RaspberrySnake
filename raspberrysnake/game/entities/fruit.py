from game.entities.entity import Entity
from riem.graphics import Graphics, ImageLoader
from riem.library import Dimensions, Point
from typing import List
import random

class Fruit(Entity):

	# Constants
	image_list: List[str] = ["apple_G", "apple_R", "banana_Y"]

	def __init__(self, position: Point, image: str = None, score: int = 50) -> None:
		super().__init__(position, Dimensions(32, 32))
		if image is None:
			image = Fruit.image_list[random.randint(0, len(Fruit.image_list)) - 1]
		self.image = image
		self.score = score

	def get_score(self) -> int:
		return self.score

	def render(self, gfx: Graphics) -> None:
		gfx.draw_image(ImageLoader.load("fruit/%s" % self.image), self.position * Point(self.size.width, self.size.height))