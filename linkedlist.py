class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	"""
LinkedList:
	
	Initialize as follows:
		l_list = LinkedList()

	Functions:
		1) insert_at_beginning(data)
		2) insert_at_end(data)
		3) delete_node(data)
		4) is_contain(data)
		5) printlist()
	"""
	def __init__(self):
		self.__head = None
		self.__currentnode = None

	def insert_at_beginning(self, data):
		node = Node(data)

		if self.__head == None:
			self.__head = node
			self.__currentnode = node
		else:
			node.next = self.__head
			self.__head = node

		return self

	def insert_at_end(self, data):
		node = Node(data)

		if self.__head == None:
			self.__head = node
			self.__currentnode = node
		else:
			self.__currentnode.next = node
			self.__currentnode = node
			
		return self

	def __search(self, data):
		pointer = self.__head
		if pointer.data == data:
			return None, pointer

		while pointer.next:
			if pointer.next.data == data:
				return pointer, pointer.next	# return previous node
			pointer = pointer.next
		return None, None

	def get_node(self, data):
		prev_node, search_node = self.__search(data)
		return search_node

	def delete_node(self, data):
		if self.__head == None:
			print('You did not added any value')
			return

		if self.__head == self.__currentnode: # if one node exists
			self.__head = None
			self.__currentnode = None
			return

		prev_node, search_node = self.__search(data)

		if prev_node == search_node == None:
			print('LinkedList does not contains %s'%data)
			return

		if prev_node == None and search_node != None: # if the search_node is first node
			self.__head = self.__head.next
			return

		prev_node.next = search_node.next # else
		del search_node
			
		return self

	def is_contain(self, data):
		pointer = self.__head
		while pointer:
			if pointer.data == data:
				print('LinkedList contains %s'%data) 
				return
			pointer = pointer.next
		print('LinkedList does not contains %s'%data) 

	def print_list(self):
		pointer = self.__head
		while pointer:
			print(pointer.data, end=' ')
			pointer = pointer.next
		print()

	def __rev(self, node):
		if node.next is None:
			self.__head = node
			return self.__head
		curr_node = self.__rev(node.next)
		curr_node.next = node
		return node

	def reverse(self):
		self.__rev(self.__head).next = None # assign last node to None to break loop
			
		return self

	def print_head(self):
		print('head:', self.__head.data)

	def sort(self):
		"""
		MergeSort()
		"""
		pass


def main():
	l_list = LinkedList()

	l_list.insert_at_end(11)
	l_list.insert_at_end(22)
	l_list.insert_at_end(33)
	l_list.insert_at_end(44)
	l_list.insert_at_beginning(111)
	l_list.insert_at_beginning(222)
	l_list.insert_at_beginning(333)
	l_list.insert_at_beginning(444)
	l_list.print_head()
	l_list.print_list()

	l_list.reverse()
	l_list.print_head()
	l_list.print_list()

	# l_list.delete_node(44)
	# l_list.delete_node(444)
	# l_list.delete_node(22)
	# l_list.delete_node(4)

	# l_list.print_list()
	# l_list.is_contain(10)
	# l_list.is_contain(11)

if __name__ == '__main__':
	main()