class Node:
	def __init__(self, value=None, next_node=None):
		self.value = value
		self.next_node = next_node

	def get_value(self):
		return self.value

	def get_next(self):
		return self.next_node

	def set_next(self, new_next):
		self.next_node = new_next

class LinkedList:
	def __init__(self):
		self.head = None

	def add_to_head(self, value):
		node = Node(value)

		if self.head is not None:
			node.set_next(self.head)

		self.head = node

	def contains(self, value):
		if not self.head:
			return False

		current = self.head

		while current:
			if current.get_value() == value:
				return True

			current = current.get_next()

		return False

	def reverse_list(self, node, prev):
		# check if node exists
		if node:
			# if node doesn't have get next attr it is at the end
			if not node.get_next():
				# set head of list to be node at end of list
				self.head = node
				# set next attr of node to be the passed in prev value
				node.set_next(prev)
			# if node isn't at the end of the list
			else:
				# get next node from current node
				next = node.get_next()
				# set current node next attr to passed in prev value
				node.set_next(prev)
				# call reverse_list function passing in next node for
				# node parameter and current node for prev parameter
				self.reverse_list(next, node)
