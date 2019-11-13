from graphics.dimensions import Dimensions
from graphics.images import ImageLoader
from tkinter import *

class Application:

	def __init__(self):

		# Configure Size
		size = Dimensions(640, 480)

		# Create Application
		app = Tk()
		app.title("Raspberry Snake")
		app.geometry("%dx%d" % (size.width, size.height))
		app.resizable(False, False)

		# Create Canvas
		canvas = Canvas(app, bg = "black", width = size.width, height = size.height, highlightthickness = 0)

		# Create Logo
		logo = canvas.create_image(160, 160, image = ImageLoader.load("logo"), anchor = NW)
		# NOTE: this is where we will handle the rendering of the current state

		# Pack Canvas
		canvas.pack()

		# Start Application
		app.mainloop()