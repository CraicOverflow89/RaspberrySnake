from core.application import Application
from core.states import State
from graphics.alignment import Align
from graphics.images import ImageLoader
from library.dimensions import Dimensions
from library.list import ArrayList
from library.methods import *
from library.pair import Pair
from library.point import Point
from states.about import StateAbout
from states.game import StateGame
import sys

class StateTitle(State):

	def __init__(self, app):
		super().__init__(app, "TITLE")
		self.menu_option = ArrayList(Pair("Start", Point(290, 260)), Pair("Instructions", Point(290, 290)), Pair("About", Point(290, 320)), Pair("Exit", Point(290, 350)))
		self.menu_active = 0

	def onKeyPressed(self, event):

		# Invoke Option
		if event.keycode == 13:
			when(self.menu_active, {
				0: lambda: self.app.stateUpdate(StateGame),
				1: lambda: print("how to play"),
				2: lambda: self.app.stateUpdate(StateAbout, True),
				3: lambda: sys.exit()
			})()
			return

		# Cursor Up
		if event.keycode == 38:
			if self.menu_active > 0: self.menu_active -= 1
			return

		# Cursor Down
		if event.keycode == 40:
			if self.menu_active < self.menu_option.size() - 1: self.menu_active += 1
			return

	def onRevert(self):

		# Reset Cursor
		self.menu_active = 0

	def render(self, gfx):

		# Render Logo
		gfx.draw_image(ImageLoader.load("logo"), Point(160, 40))

		# Render Options
		self.render_options(gfx)

		# Render Version
		gfx.draw_text("Version %s" % Application.getVersion(), Point(10, Application.getDimensions().height - 25))

		# Render Hint
		gfx.draw_text("Press UP/DOWN to navigate, ENTER to select.", Point(Application.getDimensions().width - 10, Application.getDimensions().height - 25), Align.RIGHT)

	def render_options(self, gfx):

		# Render Cursor
		cursor_point = self.menu_option.get(self.menu_active).second
		gfx.draw_text("->", Point(cursor_point.x - 30, cursor_point.y))

		# Render Text
		self.menu_option.each(lambda it: gfx.draw_text(it.first, it.second))

	def tick(self):
		pass