from inspect import stack
from multiprocessing.dummy import current_process


graph_1 = {'a': ['b', 'c'], 'b': ['d'],
           'c': ['e'], 'd': ['f'], 'e': [], 'f': []}
print(graph_1.__class__)


def depthFirstSearch(graph, src):
    stack = [src]

    while (len(stack) > 0):
        current_node = stack.pop()
        print(current_node)
        for neighbor in graph[current_node]:
            stack.append(neighbor)


depthFirstSearch(graph_1, 'a')
