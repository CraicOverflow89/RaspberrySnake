class Dimensions:

	def __init__(self, width, height):
		self.width = width
		self.height = height

	def __add__(self, value):
		return Dimensions(self.width + value, self.height + value)

	def __mul__(self, value):
		return Dimensions(self.width * value, self.height * value)

	def __sub__(self, value):
		return Dimensions(self.width - value, self.height - value)

	def __truediv__(self, value):
		return Dimensions(self.width / value, self.height / value)