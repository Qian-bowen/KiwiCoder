from collections import deque, OrderedDict
from threading import Lock
from kiwi.common.common import with_defer, defer


class DAG:
    def __init__(self):
        self.graph = OrderedDict()
        self.mutex = Lock()

    @with_defer
    def add_node(self, target_node) -> None:
        self.mutex.acquire()
        defer(lambda: self.mutex.release())
        if target_node in self.graph:
            raise KeyError('node %s already exist' % target_node)
        self.graph[target_node] = set()

    @with_defer
    def delete_node(self, target_node) -> None:
        self.mutex.acquire()
        defer(lambda: self.mutex.release())
        if target_node in self.graph:
            raise KeyError('node %s already exist' % target_node)
        self.graph.pop(target_node)
        for u in self.graph:
            for v in self.graph[u]:
                if v == target_node:
                    self.graph[u].remove(v)

    @with_defer
    def add_edge(self, from_node, to_node) -> None:
        self.mutex.acquire()
        defer(lambda: self.mutex.release())
        self.graph[from_node].add(to_node)

    @with_defer
    def delete_edge(self, from_node, to_node) -> None:
        self.mutex.acquire()
        defer(lambda: self.mutex.release())
        if to_node not in self.graph.get(from_node, []):
            raise KeyError('edge not exist')
        self.graph[from_node].remove(to_node)

    @with_defer
    def size(self):
        self.mutex.acquire()
        defer(lambda: self.mutex.release())
        return len(self.graph)

    @with_defer
    def predecessors(self, node):
        self.mutex.acquire()
        defer(lambda: self.mutex.release())
        return [key for key in self.graph if node in self.graph[key]]

    @with_defer
    def downstream(self, node):
        self.mutex.acquire()
        defer(lambda: self.mutex.release())
        if node not in self.graph:
            raise KeyError('node %s not in graph' % node)
        return list(self.graph[node])

    @with_defer
    def topological_sort(self):
        self.mutex.acquire()
        defer(lambda: self.mutex.release())
        in_degree = {}
        for u in self.graph:
            in_degree[u] = 0
        for u in self.graph:
            for v in self.graph[u]:
                in_degree[v] += 1

        queue = deque()
        for u in in_degree:
            if in_degree[u] == 0:
                queue.appendleft(u)

        l = []
        while queue:
            u = queue.pop()
            l.append(u)
            for v in self.graph[u]:
                in_degree[v] -= 1
                if in_degree[v] == 0:
                    queue.appendleft(v)

        if len(l) == len(self.graph):
            return l
        else:
            raise ValueError('not a acyclic graph')
