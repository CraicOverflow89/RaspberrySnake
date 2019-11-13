from core.states import State
from graphics.images import ImageLoader
from library.dimensions import Dimensions
from library.methods import *
from library.point import Point
from states.game import StateGame
import sys

class StateTitle(State):

	def __init__(self, app):
		super().__init__(app, "TITLE")
		self.cursor_pos = 0

	def onKeyPressed(self, event):

		# Invoke Option
		if event.keycode == 13:
			when(self.cursor_pos, {
				0: lambda: self.app.stateUpdate(StateGame),
				1: lambda: print("about game"),
				2: lambda: sys.exit()
			})
			return

		# Cursor Up
		if event.keycode == 38:
			if self.cursor_pos > 0: self.cursor_pos -= 1
			return

		# Cursor Down
		if event.keycode == 40:
			if self.cursor_pos < 2: self.cursor_pos += 1
			return

	def render(self, gfx):

		# Render Logo
		gfx.draw_image(ImageLoader.load("logo"), Point(160, 40))

		# Render Options
		self.render_options(gfx)

		# Render Version
		gfx.draw_text("Version %s" % self.app.getVersion(), Point(10, self.app.getDimensions().height - 25))

	def render_options(self, gfx):

		# Render Cursor
		gfx.draw_text("->", Point(260, (self.cursor_pos * 30) + 260))

		# Render Text
		gfx.draw_text("Start", Point(290, 260))
		gfx.draw_text("About", Point(290, 290))
		gfx.draw_text("Exit", Point(290, 320))

	def tick(self):
		pass