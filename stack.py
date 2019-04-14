from collections import deque # for fast push and pop operations

class Stack:
	"""
Args:
	1) array: is a list or empty
	

Functions:

	1) push(element):

	2) pop()

	3) getvalues()
	"""
	def __init__(self, array=None):
		if type(array) == list:
			self.obj = deque(array)
		else:
			self.obj = deque()

	def push(self, element):
		self.obj.append(element)

	def pop(self):
		return self.obj.pop()

	def getvalues(self):
		return list(self.obj)
		