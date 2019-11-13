from graphics.canvas import Graphics
from library.dimensions import Dimensions
from library.point import Point
from tkinter import Canvas, Tk

class Application:

	def __init__(self, state):

		# Constants
		self.version = "0.0.1"
		self.size = Dimensions(640, 480)
		tick_ms = 250

		# Create Application
		app = Tk()
		app.title("Raspberry Snake")
		app.geometry("%dx%d" % (self.size.width, self.size.height))
		app.resizable(False, False)

		# Create Canvas
		canvas = Canvas(app, bg = "black", width = self.size.width, height = self.size.height, highlightthickness = 0)
		canvas.pack()

		# Create Graphics
		gfx = Graphics(canvas)

		# Initialise State
		self.state = state(self)
		self.state.onStart()

		# Bind Events
		app.bind("<Key>", self.state.onKeyPressed)

		# Create Loop
		def loop():

			# Application Tick
			self.state.tick()

			# Application Render
			gfx.draw_rect(Point(0, 0), self.size, "black", True)
			self.state.render(gfx)

			# Schedule Loop
			app.after(tick_ms, loop)

		# Invoke Loop
		loop()

		# Start Application
		app.mainloop()

	def getDimensions(self):
		return self.size

	def getVersion(self):
		return self.version

	def stateUpdate(self, state):

		# Terminate Old
		self.state.onTerminate()

		# Initialise New
		self.state = state(self)
		self.state.onStart()