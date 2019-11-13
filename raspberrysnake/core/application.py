from graphics.dimensions import Dimensions
from tkinter import *

class Application:

	def __init__(self, state):

		# Initial State
		state.onStart()

		# Configure Size
		size = Dimensions(640, 480)

		# Create Application
		app = Tk()
		app.title("Raspberry Snake")
		app.geometry("%dx%d" % (size.width, size.height))
		app.resizable(False, False)

		# Create Canvas
		canvas = Canvas(app, bg = "black", width = size.width, height = size.height, highlightthickness = 0)

		# State Render
		state.render(canvas)

		# Pack Canvas
		canvas.pack()

		# Start Application
		app.mainloop()