"""
steps that I need to take to implement a*:
1. Learn Priority queue data structure and implement it
2. Learn Graph data structure and implement it
3. ???
4. Profit
"""
import collections


class SimpleGraph:
    def __init__(self):
        self.edges = {}

    def neighbours(self, index):
        return self.edges[index]


example_graph = SimpleGraph()
example_graph.edges = {
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['A'],
    'D': ['E', 'A'],
    'E': ['B']
}

class Queue:
    def __init__(self):
        self.elements = collections.deque()

    def empty(self):
        return len(self.elements) == 0

    def put(self, x):
        self.elements.append(x)

    def get(self):
        return self.elements.popleft()


def breadth_first_search_1(graph, start):
    frontier = Queue()
    frontier.put(start)
    visited = {}
    visited[start] = True

    while not frontier.empty():
        current = frontier.get()
        print("Visiting %r" % current)
        for next in graph.neighbours(current):
            if next not in visited:
                frontier.put(next)
                visited[next] = True


breadth_first_search_1(example_graph, 'A')

