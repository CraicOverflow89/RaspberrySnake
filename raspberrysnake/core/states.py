from abc import ABC, abstractmethod
from graphics.alignment import Align
from library.point import Point

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

	def render_title(self, gfx, value):
		gfx.draw_text(value, Point(25, 25), Align.LEFT, "Inconsolata 22", "#E62959", "#801731")

	@abstractmethod
	def tick(self):
		pass