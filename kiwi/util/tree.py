from kiwi.common.exception import NodeNotFoundException
from typing import List
from abc import ABCMeta, abstractmethod


class TreeNode(metaclass=ABCMeta):
    def __init__(self, key, children=None):
        if children is None:
            children = []
        self.key = key
        self.children = children

    def __str__(self):
        return str(self.key)

    def __lt__(self, other):
        return self.key < other.key

    @abstractmethod
    def done(self) -> bool:
        pass


class TreeAryN:
    def __init__(self, sort_func=None):
        self.root = None
        self.size = 0
        self.sort_func = sort_func

    def find_node(self, node, key):
        if node is None or node.key == key:
            return node
        for child in node.children:
            result = self.find_node(child, key)
            if result:
                return result
        return None

    def add_node(self, new_node, parent_key=None) -> None:
        if parent_key is None:
            self.root = new_node
        else:
            parent_node = self.find_node(self.root, parent_key)
            if parent_node is None:
                raise NodeNotFoundException('add node fail, parent not find')
            parent_node.children.append(new_node)
            if self.sort_func:
                self.sort_func(parent_node.children)
        self.size += 1

    def preorder(self, exclude_done=False) -> List[TreeNode]:
        res_seq = []

        def dfs(node: TreeNode):
            if node is None:
                return
            if exclude_done:
                if not node.done():
                    res_seq.append(node)
            else:
                res_seq.append(node)
            for child in node.children:
                dfs(child)

        dfs(self.root)
        return res_seq

    def _tree_view(self, node, res_str="") -> str:
        if node is None:
            return ""
        res_str += str(node) + '('
        child_num = len(node.children)
        for i in range(child_num):
            child = node.children[i]
            delimiter = ',' if i != child_num - 1 else ''
            res_str = self._tree_view(child, res_str) + delimiter
        res_str += ')'
        return res_str

    def __str__(self):
        return self._tree_view(self.root)
