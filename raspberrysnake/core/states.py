from abc import ABC, abstractmethod

class State(ABC):

	def __init__(self, app, name):
		self.app = app
		self.name = name

	def onStart(self):
		pass

	def onTerminate(self):
		pass

	@abstractmethod
	def render(self, canvas):
		pass
		# NOTE: should use an intermediate class that provides easy access to typical drawing methods
		#       rather than accepting canvas and having to repeat stuff in render methods

	@abstractmethod
	def tick(self):
		pass