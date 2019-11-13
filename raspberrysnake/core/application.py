from graphics.dimensions import Dimensions
from tkinter import *

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

		# Initialise State
		state = state(self)
		state.onStart()

		# Create Loop
		def loop():

			# Clear Canvas
			canvas.create_rectangle(0, 0, self.size.width, self.size.height, fill = "black")

			# Invoke Tick
			state.tick()

			# Invoke Render
			state.render(canvas)

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