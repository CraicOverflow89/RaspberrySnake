from abc import ABC, abstractmethod

class State(ABC):

	def __init__(self, app, name):
		self.app = app
		self.name = name

	def on_key_pressed(event):
		pass

	def on_revert(self, data):
		pass

	def on_start(self, data):
		pass

	def on_store(self):
		pass

	def on_terminate(self):
		pass

	@abstractmethod
	def render(self, gfx):
		pass

	@abstractmethod
	def tick(self):
		pass