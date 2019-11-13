from graphics.canvas import Graphics
from graphics.dimensions import Dimensions
from graphics.point import Point
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
		state = state(self)
		state.onStart()

		# Bind Events
		app.bind("<Key>", state.onKeyPressed)

		# Create Loop
		def loop():

			# Application Tick
			state.tick()

			# Application Render
			gfx.draw_rect(Point(0, 0), self.size, "black")
			state.render(gfx)

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