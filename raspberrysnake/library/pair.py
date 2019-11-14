class Pair():

	def __init__(self, first, second):
		self.first = first
		self.second = second

	def __str__(self):
		return "(%s, %s)" % (str(self.first), str(self.second))

	def values(self):
		return (self.first, self.second)