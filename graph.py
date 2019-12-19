
class UndirectedGraph:
	
	def __init__(self, total_verticies=None):
		super().__init__()
		if total_verticies is None:
			raise ValueError('Initialize total number of verticies')
		self.total_verticies = total_verticies
		self.graph = {vertex:[] for vertex in range(total_verticies)}

	def _valid_input(self, verticies):
		max_vertex = max(verticies)
		if max_vertex >= self.total_verticies:
			return False
		return True # Else

	def add_edge(self, begining, end, cost=0):
		if not self._valid_input(verticies=[begining, end]):
			raise ValueError('input vertex value is grater than total verticies')

		self.graph[begining].append(end)
		self.graph[end].append(begining)

	def init_edges(self, verticies, cost=0):
		for i, j in verticies:
			self.add_edge(i, j)	

	def print_graph(self):
		for vertex in range(self.total_verticies):
			print(vertex, '==>', self.graph[vertex])

	def BFS(self, starting_vertex=0):
		visited = [False] * self.total_verticies
		queue = []

		visited[starting_vertex] = True
		queue.append(starting_vertex)

		while len(queue):
			vertex = queue.pop(0)
			print(vertex, end=' --> ')

			for v in self.graph[vertex]:
				if not visited[v]:
					queue.append(v)
					visited[v] = True
		print('')

	def DFS(self, starting_vertex=0):
		visited = [False] * self.total_verticies
		stack = []

		stack.append(starting_vertex)

		while len(stack):
			vertex = stack.pop(-1)

			if not visited[vertex]:
				print(vertex, end=' --> ')
				visited[vertex] = True

			for v in self.graph[vertex]:
				if not visited[v]:
					stack.append(v)
		print('')


class DirectedGraph(UndirectedGraph):

	def __init__(self, *args,**kwargs):
		super().__init__(*args, **kwargs)

	def add_edge(self, begining, end, cost=0):
		if not super()._valid_input(verticies=[begining, end]):
			raise ValueError('input vertex value is grater than total verticies')

		self.graph[begining].append(end)



def main():
	graph = UndirectedGraph(total_verticies=10)
	verticies = [[1, 8], [2, 6], [3, 1], [5, 3], [7, 8], [8, 4], [8, 6]]
	graph.init_edges(verticies=verticies)
	graph.print_graph()
	graph.DFS(starting_vertex=1)
	graph.BFS(starting_vertex=1)

	print()

	graph = DirectedGraph(total_verticies=10)
	verticies = [[1, 8], [2, 6], [3, 1], [5, 3], [7, 8], [8, 4], [8, 6]]
	graph.init_edges(verticies=verticies)
	graph.print_graph()
	graph.DFS(starting_vertex=1)
	graph.BFS(starting_vertex=1)


if __name__ == '__main__':
	main()