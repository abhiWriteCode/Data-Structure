class Tree:
	def __init__(self):
		pass
	class __Node:
		def __init__(self, data):
			self.data = data
			self.left = None
			self.right = None

	def _addnode(self, data, node):
		if node is None:
			node = Tree.__Node(data)
			return node

		if node.data > data: # if data is lower than node value
			node.left = self._addnode(data, node.left)
		else:
			node.right = self._addnode(data, node.right)
		return node

	def _remove_whole_tree(self, node):
		if node is None:
			return
		self._remove_whole_tree(node.left)
		self._remove_whole_tree(node.right)
		node.left = node.right = None

	def _delete_node(self, node, data):
		if node is None:
			print('The tree does not contains %s'%data)
			return node
		if node.data > data:
			node.left = self._delete_node(node.left, data)
		elif node.data < data:
			node.right = self._delete_node(node.right, data)
		else:
			if node.left is None:
				temp_node = node.right
				node = None
				return temp_node
			if node.right is None:
				temp_node = node.left
				node = None
				return temp_node

			left_subtree_largest_value = self._find_largest_node(node.left)
			node.data = left_subtree_largest_value.data
			node.left = self._delete_node(node.left, left_subtree_largest_value.data)
		return node

	def _find_largest_node(self, node):
		if node.right is None:
			return node
		else:
			return self._find_largest_node(node.right)

	def _search(self, node, data):
		if node is None:
			print('The tree does not contains %s'%data)
			return node # return None
		if node.data > data:
			self._search(node.left, data)
		elif node.data < data:
			self._search(node.right, data)
		else: 		# node.data == data
			print('The tree contains %s'%data)
			return node

	def _height(self, node):
		height = 0
		if node is None:
			return height

		left_subtree_height = self._height(node.left)
		right_subtree_height = self._height(node.right)

		height = max(left_subtree_height, right_subtree_height) + 1
		return height

	def _maxwidth(self, node):
		from collections import deque
		queue = deque()
		maxwidth = 0
		queue.appendleft(node) # PUSH

		while len(queue) != 0:
			this_level_width = len(queue)
			maxwidth = max(maxwidth, this_level_width)

			while this_level_width != 0:
				this_level_width -= 1
				temp_node = queue.pop() # POP
				if temp_node.left is not None:
					queue.appendleft(temp_node.left) # PUSH
				if temp_node.right is not None:
					queue.appendleft(temp_node.right) # PUSH
		return maxwidth

	def _preorder(self, node):
		if node is None:
			return
		print(node.data, end=' ')
		self._preorder(node.left)
		self._preorder(node.right)

	def _inorder(self, node):
		if node is None:
			return
		self._inorder(node.left)
		print(node.data, end=' ')
		self._inorder(node.right)

	def _postorder(self, node):
		if node is None:
			return
		self._postorder(node.left)
		self._postorder(node.right)
		print(node.data, end=' ')

	def _total_nodes(self, node):
		if node is None:
			return 0
		return (self._total_nodes(node.left) + self._total_nodes(node.right) + 1)


class BST(Tree):
	def __init__(self):
		self.root = None

	def insert(self, data):
		self.root = super()._addnode(data, self.root)

	def remove_tree(self):
		if self.root is None:
			print('Tree is Empty')
			return
		super()._remove_whole_tree(self.root)
		self.root = None
		print('Tree is removed')

	def delete_node(self, data):
		if self.root is None:
			print('Tree is Empty')
			return
		super()._delete_node(self.root, data)

	def search_node(self, data):
		if self.root is None:
			print('Tree is Empty')
			return
		super()._search(self.root, data)

	def find_largest_value(self):
		if self.root is None:
			print('Tree is Empty')
			return
		return super()._find_largest_node(self.root).data

	def determine_height(self):
		if self.root is None:
			return 0
		return super()._height(self.root)

	def determine_maxwidth(self):
		if self.root is None:
			return 0
		return super()._maxwidth(self.root)

	def preorder_traversal(self):
		if self.root is None:
			print('Tree is Empty')
			return
		super()._preorder(self.root)
		print()

	def inorder_traversal(self):
		if self.root is None:
			print('Tree is Empty')
			return
		super()._inorder(self.root)
		print()

	def postorder_traversal(self):
		if self.root is None:
			print('Tree is Empty')
			return
		super()._postorder(self.root)
		print()

	def total_node(self):
		return super()._total_nodes(self.root)

	def BFS(self): # Level order tree traversal ==> Breadth first search
		if self.root is None:
			print('Tree is Empty')
			return
		queue = []
		queue.append(self.root)

		while len(queue) != 0:
			node = queue.pop(0)
			print(node.data, end=' ')
			if node.left is not None:
				queue.append(node.left)
			if node.right is not None:
				queue.append(node.right)
			
		print()



def main():
	tree = BST()

	tree.insert(20)
	tree.insert(40)
	tree.insert(30)
	tree.insert(10)
	tree.insert(88)
	tree.insert(80)
	tree.insert(5)
	tree.insert(1)
	tree.insert(15)
	tree.insert(70)

	# import random as r
	# r.seed(6456341648)
	# l = set([r.randint(1, 999999) for _ in range(20000)])
	# print(len(l))
	# for i in l:
	# 	tree.insert(i)

	print('preorder traversal:', end=' ')
	tree.preorder_traversal()
	print('inorder traversal:', end=' ')
	tree.inorder_traversal()
	print('postorder traversal:', end=' ')
	tree.postorder_traversal()
	print('breadth first traversal:', end=' ')
	tree.BFS()

	print('Largest Value:', tree.find_largest_value())
	print('Max Width:', tree.determine_maxwidth())

	tree.delete_node(15)
	tree.delete_node(20)

	print('breadth first traversal:', end=' ')
	tree.BFS()
	print('Max Width:', tree.determine_maxwidth())

	tree.search_node(5)
	tree.search_node(50)

	print('Height:', tree.determine_height())

	print('Total Nodes:', tree.total_node())

	tree.remove_tree()
	print('inorder traversal:', end=' ')
	tree.inorder_traversal()

	tree.insert(5)
	tree.insert(1)
	tree.insert(15)
	print('breadth first traversal:', end=' ')
	tree.BFS()


if __name__ == '__main__':
	main()
