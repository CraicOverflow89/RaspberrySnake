class ArrayList():

	def __init__(self, *value):
		if isinstance(value[0], list) and len(value) == 1:
			value = value[0]
		self.value = []
		for element in value:
			self.value.append(element)
		self.iter_pos = 0

	def __iter__(self):
		self.iter_pos = 0
		return self

	def __next__(self):
		if self.iter_pos == len(self.value):
			raise StopIteration
		result = self.value[self.iter_pos]
		self.iter_pos += 1
		return result

	def __str__(self):
		return "[" + ", ".join(map(lambda it: "'" + str(it) + "'", self.value)) + "]"

	def add(self, value):
		result = self.value
		result.append(value)
		return ArrayList(result)

	def addAll(self, value):
		result = self.value
		for element in value:
			result.append(element)
		return ArrayList(result)

	def all(self, logic):
		for element in self.value:
			if not logic(element):
				return False
		return True

	def contains(self, value):
		for element in self.value:
			if element == value:
				return True
		return False

	def each(self, logic):
		for element in self.value:
			logic(element)
		return self

	def filter(self, logic):
		result = []
		for element in self.value:
			if logic(element):
				result.append(element)
		return ArrayList(result)

	def first(self, logic):
		for element in self.value:
			if logic(element):
				return element
		return None

	def get(self, position):
		return self.value[position]

	def isEmpty(self):
		return len(self.value) > 0

	def map(self, logic):
		result = []
		for element in self.value:
			result.append(logic(element))
		return ArrayList(result)

	def none(self, logic):
		for element in self.value:
			if logic(element):
				return False
		return True

	def reject(self, logic):
		result = []
		for element in self.value:
			if not logic(element):
				result.append(element)
		return ArrayList(result)

	def remove(self, value):
		result = []
		for element in self.value:
			if element != value:
				result.append(element)
		return ArrayList(result)

	def size(self):
		return len(self.value)

	def take(self, count):
		if len(self.value) < count:
			count = len(self.value)
		result = []
		for x in range(count):
			result.append(self.value[x])
		return ArrayList(result)

	def toList(self, count):
		result = []
		for element in self.value:
			result.append(element)
		return result