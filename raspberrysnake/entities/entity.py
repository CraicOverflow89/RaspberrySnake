from abc import ABC, abstractmethod

class Entity(ABC):

	def __init__(self, position, size):
		self.position = position
		self.size = size

	@abstractmethod
	def render(self, gfx):
		pass