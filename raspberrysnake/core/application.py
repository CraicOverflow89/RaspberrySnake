from graphics.dimensions import Dimensions
from tkinter import *

class Application:

	def __init__(self, state):

		# Configure Application
		size = Dimensions(640, 480)
		tick_ms = 1000

		# Create Application
		app = Tk()
		app.title("Raspberry Snake")
		app.geometry("%dx%d" % (size.width, size.height))
		app.resizable(False, False)

		# Create Canvas
		canvas = Canvas(app, bg = "black", width = size.width, height = size.height, highlightthickness = 0)

		# Initial State
		state.onStart()

		# Application Loop
		def loop():
			state.tick()
			state.render(canvas)
			app.after(tick_ms, loop)

		# Initial Execution
		loop()

		# Pack Canvas
		canvas.pack()

		# Start Application
		app.mainloop()