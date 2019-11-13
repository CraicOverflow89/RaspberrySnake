from abc import ABC, abstractmethod

class Entity(ABC):

	def __init__(self, position):
		self.position = position

	@abstractmethod
	def render(self, gfx):
		pass