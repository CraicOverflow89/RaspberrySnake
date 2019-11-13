from abc import ABC, abstractmethod

class State(ABC):

	def __init__(self, name):
		self.name = name

	def onStart(self):
		pass

	def onTerminate(self):
		pass

	@abstractmethod
	def render(self, canvas):
		pass

	@abstractmethod
	def tick(self):
		pass