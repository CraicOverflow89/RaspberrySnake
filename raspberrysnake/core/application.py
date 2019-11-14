from graphics.canvas import Graphics
from library.dimensions import Dimensions
from library.point import Point
from tkinter import Canvas, Tk
import time

class Application:

	# Constants
	version = "0.0.1"
	size = Dimensions(640, 480)
	tick_ms = 250

	def __init__(self, state):

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
		self.state_active = None
		self.state_stored = None
		self.stateUpdate(state)

		# Create Loop
		def loop():

			# Timer Start
			loop_time = (time.time() * 1000)

			# Application Tick
			self.state_active.tick()

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

	def getDimensions():
		return Application.size

	def getVersion():
		return Application.version

	def stateRevert(self):

		# Nothing Stored
		if self.state_stored is None:
			raise Exception("No stored state to revert to!")

		# Terminate Existing
		self.state_active.onTerminate()

		# Revert State
		self.state_active = self.state_stored
		self.state_active.onRevert()
		self.state_stored = None

		# Bind Events
		self.app.bind("<Key>", self.state_active.onKeyPressed)

	def stateUpdate(self, state, store = False):

		# Existing State
		if self.state_active is not None:

			# Store Existing
			if store is True:
				self.state_active.onStore()
				self.state_stored = self.state_active

			# Terminate Existing
			else:
				self.state_active.onTerminate()

		# Initialise State
		self.state_active = state(self)
		self.state_active.onStart()

		# Bind Events
		self.app.bind("<Key>", self.state_active.onKeyPressed)