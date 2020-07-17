class RingBuffer:
	def __init__(self, capacity):
		# capacity attr set by passed in value
		self.capacity = capacity
		# create current index attr and set it at 0
		self.current = 0
		# create a list that has the size of the passed
		# in capacity setting each item to none
		self.storage = [None for spot in range(self.capacity)]

	def append(self, item):
		# set passed in item to the current index
		self.storage[self.current] = item
		# if current attr is at last index in storage
		# reset it to 0/beginning of the list
		if self.current == (self.capacity - 1):
			self.current = 0
		# otherwise add one to current index
		else:
			self.current += 1


	def get(self):
		# return list with only existing items
		return [item for item in self.storage if item]
