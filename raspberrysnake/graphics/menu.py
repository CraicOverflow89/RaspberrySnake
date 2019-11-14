from library.list import ArrayList
from library.point import Point

class Menu:

	def __init__(self, offset = Point(-30, 0)):
		self.option = ArrayList()
		self.active = 0
		self.offset = offset

	def add_option(self, label, position, logic):
		self.option = self.option.add(MenuItem(self, label, position, logic))

	def get_offset(self):
		return self.offset

	def on_key_pressed(self, event):

		# Invoke Option
		if event.keycode == 13 or event.keycode == 36:
			self.option.get(self.active).invoke()
			return

		# Cursor Up
		if event.keycode == 38 or event.keycode == 111:
			if self.active > 0: self.active -= 1
			return

		# Cursor Down
		if event.keycode == 40 or event.keycode == 116:
			if self.active < self.option.size() - 1: self.active += 1
			return

	def render(self, gfx):

		# Render Text
		self.option.each(lambda it: it.render_label(gfx))

		# Render Cursor
		self.option.get(self.active).render_cursor(gfx)

	def set_cursor(self, position = 0):
		if position >= self.option.size(): position = 0
		self.active = position

class MenuItem():

	def __init__(self, menu, label, position, logic):
		self.menu = menu
		self.label = label
		self.position = position
		self.logic = logic

	def invoke(self):
		self.logic()

	def render_cursor(self, gfx):
		gfx.draw_text("->", self.position + self.menu.get_offset())

	def render_label(self, gfx):
		gfx.draw_text(self.label, self.position)