from core.application import Application
from core.states import State
from graphics.alignment import Align
from library.point import Point

class StateResults(State):

	def __init__(self, app):
		super().__init__(app, "RESULTS")

	def onKeyPressed(self, event):
		pass
		# NOTE: menu with options to retry / quit to title?

	def onStart(self, data):
		self.data = data

	def render(self, gfx):

		# Render Title
		gfx.draw_text("RESULTS", Point(25, 25), Align.LEFT, "Inconsolata 22")

		# Render Info
		gfx.draw_text("Score: %d" % self.data["score"], Point(25, 100))
		gfx.draw_text("Time:  %ds" % self.data["time"], Point(25, 130))
		# NOTE: consider showing time as minutes and seconds

		# Render Options
		#self.render_options(gfx)
		# NOTE: this logic needs to be abstracted out from StateTitle

		# Render Version
		gfx.draw_text("Version %s" % Application.getVersion(), Point(10, Application.getDimensions().height - 25))

		# Render Hint
		gfx.draw_text("Press any key to return to title.", Point(Application.getDimensions().width - 10, Application.getDimensions().height - 25), Align.RIGHT)
		# NOTE: menu with options to retry / quit to title?

	def tick(self):
		pass