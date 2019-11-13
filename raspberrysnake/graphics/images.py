from tkinter import PhotoImage

class ImageLoader:
	data = {}

	def load(image):

		# Store Image
		if image not in ImageLoader.data:
			ImageLoader.data[image] = PhotoImage(file = "resources/" + image + ".gif")

		# Return Image
		return ImageLoader.data[image]