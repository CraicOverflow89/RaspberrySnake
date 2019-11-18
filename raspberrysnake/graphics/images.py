from PIL import Image, ImageTk

class ImageLoader:
	data = {}

	def load(image):

		# Store Image
		if image not in ImageLoader.data:
			ImageLoader.data[image] = ImageTk.PhotoImage(Image.open("resources/" + image + ".gif"))

		# Return Image
		return ImageLoader.data[image]