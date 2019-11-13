from graphics.canvas import Graphics
from library.dimensions import Dimensions
from library.point import Point
from tkinter import Canvas, Tk

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
		self.state = None
		self.stateUpdate(state)

		# Create Loop
		def loop():

			# Application Tick
			self.state.tick()

			# Application Render
			gfx.draw_rect(Point(0, 0), self.size, "black", True)
			self.state.render(gfx)

			# Schedule Loop
			self.app.after(Application.tick_ms, loop)

		# Invoke Loop
		loop()

		# Start Application
		self.app.mainloop()

	def getDimensions():
		return Application.size

	def getVersion():
		return Application.version

	def stateUpdate(self, state):

		# Terminate Existing
		if self.state is not None:
			self.state.onTerminate()

		# Initialise State
		self.state = state(self)
		self.state.onStart()

		# Bind Events
		self.app.bind("<Key>", self.state.onKeyPressed)