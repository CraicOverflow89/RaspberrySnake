from abc import ABC, abstractmethod

class State(ABC):

	def __init__(self, app, name):
		self.app = app
		self.name = name

	def onKeyPressed(event):
		pass

	def onRevert(self):
		pass

	def onStart(self):
		pass

	def onStore(self):
		pass

	def onTerminate(self):
		pass

	@abstractmethod
	def render(self, gfx):
		pass

	@abstractmethod
	def tick(self):
		pass