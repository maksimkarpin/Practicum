# Задание 1
print("Задание 1")
from collections import deque
class DirectedGraph:
    def __init__(self):
        self.graph = {}
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = {}
    def add_edge(self, u, v,):
        if u not in self.graph:
            self.add_vertex(u)
        if v not in self.graph:
            self.add_vertex(v)
        self.graph[u] = [v]
    def print_graph(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")
gr = DirectedGraph()
gr.add_edge("A", "B")
gr.add_edge("A", "C")
gr.add_edge("B", "C")
gr.print_graph()
# Задание 2
print("Задание 2")
def breadth_first_search(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        node = queue.popleft()
        if node not in visited:
            print(node)
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
breadth_first_search(gr.graph, "A")
breadth_first_search(gr.graph, "B")
# Задание 3
print("Задание 3")
def matrix(arr):
    len_mat = len(arr) // 2
    mat = [[0] * len_mat for _ in range(len_mat)]
    x = arr
    y = x[0::2]
    z = x[1::2]
    for i in y:
        for j in z:
            mat[i][j] = 1
    for row in mat:
        print(row)
    print(y,z)
arr = [0,1,2,0,3,1,1,0]
matrix(arr)
class Graph3:
    def __init__(self, graphs):
        self.V = graphs
        self.graph = [[0]*graphs for _ in range(graphs)]
    def add_edge(self, u,v):
        self.graph[u][v] = 1
    def print_graph(self):
        for row in self.graph:
            print(row)
gm = Graph3(4)
gm.add_edge(0,1)
gm.add_edge(2,0)
gm.add_edge(3,1)
gm.add_edge(1,0)
gm.print_graph()
# Задание 4
print("Задание 4")
class Graph4:
    def __init__(self):
        self.graph = {}
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
    def print_graph(self):
        for node in self.graph:
            print(f"{node} -> {self.graph[node]}")
gr = Graph4()
gr.add_edge("A", "B")
gr.add_edge("B", "D")
gr.add_edge("D", "C")
gr.add_edge("C", "D")
gr.print_graph()