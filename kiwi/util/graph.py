from collections import deque


class DAG:
    def __init__(self):
        self.graph = dict()
        self.key2node = dict()

    def add_node(self, target_node) -> None:
        if target_node in self.graph:
            return
        self.graph[target_node] = set()
        self.key2node[target_node.key] = target_node

    def delete_node(self, target_node) -> None:
        if target_node not in self.graph:
            raise KeyError('node %s already exist' % target_node)
        self.graph.pop(target_node)
        for u in self.graph:
            for v in self.graph[u]:
                if v == target_node:
                    self.graph[u].remove(v)

    def delete_node_by_key(self, target_node_key) -> None:
        target_node = self.key2node[target_node_key]
        if target_node in self.graph:
            raise KeyError('node %s already exist' % target_node)
        self.graph.pop(target_node)
        for u in self.graph:
            for v in self.graph[u]:
                if v == target_node:
                    self.graph[u].remove(v)

    def add_edge(self, from_node, to_node) -> None:
        self.graph[from_node].add(to_node)

    def add_edge_by_key(self, from_node_key, to_node_key) -> None:
        from_node = self.key2node[from_node_key]
        to_node = self.key2node[to_node_key]
        self.graph[from_node].add(to_node)

    def delete_edge(self, from_node, to_node) -> None:
        if to_node not in self.graph.get(from_node, []):
            raise KeyError('edge not exist')
        self.graph[from_node].remove(to_node)

    def delete_edge_by_key(self, from_node_key, to_node_key) -> None:
        from_node = self.key2node[from_node_key]
        to_node = self.key2node[to_node_key]
        if to_node not in self.graph.get(from_node, []):
            raise KeyError('edge not exist')
        self.graph[from_node].remove(to_node)

    def is_edge_exist(self, from_node_key, to_node_key) -> bool:
        from_node = self.key2node[from_node_key]
        to_node = self.key2node[to_node_key]
        if to_node not in self.graph.get(from_node, []):
            return False
        return True

    def size(self):
        return len(self.graph)

    def predecessors(self, node):
        return [key for key in self.graph if node in self.graph[key]]

    def downstream(self, node):
        if node not in self.graph:
            raise KeyError('node %s not in graph' % node)
        return list(self.graph[node])

    def available_nodes(self) -> []:
        nodes = []
        in_degree = {}
        for u in self.graph:
            in_degree[u] = 0
        for u in self.graph:
            if u.done():
                continue
            for v in self.graph[u]:
                in_degree[v] += 1
        for u in self.graph:
            if not u.done() and in_degree[u] == 0:
                nodes.append(u)
        return nodes

    def topological_sort(self):
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
