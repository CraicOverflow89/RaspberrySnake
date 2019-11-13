class Point:

	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __add__(self, point):
		return Point(self.x + point.x, self.y + point.y)