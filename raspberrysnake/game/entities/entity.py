from abc import ABC, abstractmethod
from riem.graphics import Graphics
from riem.library import Dimensions, Point

class Entity(ABC):

	def __init__(self, position: Point, size: Dimensions) -> None:
		self.position = position
		self.size = size

	def get_position(self) -> Point:
		return self.position

	@abstractmethod
	def render(self, gfx: Graphics) -> None:
		pass