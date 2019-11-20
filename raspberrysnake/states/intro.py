from core.states import State
from graphics.alignment import Align
from graphics.images import ImageLoader
from library.point import Point

# rubus idaeus ex machina

class StateIntro(State):

	def __init__(self, app):
		super().__init__(app, "INTRO")

		# Create Event
		self.add_event(2000, lambda: self.app.state_update("TITLE"))

	def render(self, gfx):

		# Render Logo
		gfx.draw_image(ImageLoader.load("brand/riem_logo"), Point(self.app.get_dimensions().width / 2, self.app.get_dimensions().height / 2), Align.CENTER)

		# Render Loading
		# NOTE: when resources are preloaded, there should be an object that fires off these tasks
		#       and provides a completion percentage to the a progress bar object that renders

	def tick(self):
		pass