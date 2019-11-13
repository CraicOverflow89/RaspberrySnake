from tkinter import PhotoImage

class ImageLoader:
	data = {}

	def load(image):

		# Create Image
		result = PhotoImage(file = "resources/" + image + ".gif")

		# Store Image
		ImageLoader.data[image] = result

		# Return Image
		return result