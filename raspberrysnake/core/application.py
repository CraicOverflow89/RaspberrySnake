from graphics.canvas import Graphics
from input.controller import Controller
from input.keyboard import Keyboard
from library.dimensions import Dimensions
from library.point import Point
from states.about import StateAbout
from states.game import StateGame
from states.instructions import StateInstructions
from states.results import StateResults
from states.title import StateTitle
from tkinter import Canvas, Tk
import time
import sys

class Application:

	# Constants
	version = "0.0.1"
	size = Dimensions(640, 480)
	tick_ms = 250
	state_create = {
		"ABOUT": StateAbout,
		"GAME": StateGame,
		"INSTRUCTIONS": StateInstructions,
		"RESULTS": StateResults,
		"TITLE": StateTitle
	}
	highscore = 0

	def __init__(self, state):

		# State Management
		self.state_active = None
		self.state_stored = None

		# Create Application
		self.app = Tk()
		self.app.title("Raspberry Snake")
		self.app.geometry("%dx%d" % (Application.size.width, Application.size.height))
		self.app.resizable(False, False)

		# Create Canvas
		canvas = Canvas(self.app, bg = "black", width = Application.size.width, height = Application.size.height, highlightthickness = 0)
		canvas.pack()

		# Create Graphics
		gfx = Graphics(canvas)

		# Initial State
		self.state_update(state)

		# Initialise Controller
		self.controller = Controller(self)

		# Application Status
		self.running = True

		# Create Loop
		def loop():

			# Not Running
			if self.running is not True:
				return

			# Timer Start
			loop_time = (time.time() * 1000)

			# Application Tick
			self.state_active.tick()
			self.state_active.tick_event()

			# Application Render
			gfx.draw_rect(Point(0, 0), self.size, "black", True)
			self.state_active.render(gfx)

			# Schedule Loop
			loop_time = (time.time() * 1000) - loop_time
			loop_wait = 0
			if loop_time < Application.tick_ms:
				loop_wait = Application.tick_ms - loop_time
			self.app.after(int(loop_wait), loop)

		# Invoke Loop
		loop()

		# Start Application
		self.app.mainloop()

	def action(self, action):
		self.state_active.on_action(action)

	def get_dimensions(self):
		return Application.size

	def get_score(self):
		return Application.highscore

	def get_version(self):
		return Application.version

	def new_score(self, value):
		if value > Application.highscore:
			Application.highscore = value
			return True
		return False

	def on_key_pressed(self, event):
		if event.keycode in Keyboard.action:
			self.action(Keyboard.action[event.keycode])

	def state_bind(self):
		self.app.bind("<Key>", self.on_key_pressed)

	def state_revert(self, data = None):

		# Nothing Stored
		if self.state_stored is None:
			raise Exception("No stored state to revert to!")

		# Terminate Existing
		self.state_active.on_terminate()

		# Revert State
		self.state_active = self.state_stored
		self.state_active.on_revert(data)
		self.state_stored = None

		# Bind Events
		self.state_bind()

	def state_update(self, state, store = False, data = None):

		# Existing State
		if self.state_active is not None:

			# Store Existing
			if store is True:
				self.state_active.on_store()
				self.state_stored = self.state_active

			# Terminate Existing
			else:
				self.state_active.on_terminate()

		# Initialise State
		self.state_active = Application.state_create[state](self)
		self.state_active.on_start(data)

		# Bind Events
		self.state_bind()

	def terminate(self):

		# Application Status
		self.running = False

		# Terminate Controller
		self.controller.terminate()

		# System Exit
		sys.exit()