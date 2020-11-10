class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.sorted_nodes = []

    def insert(self, data):
        if self.data:
            if self.data > data:
                if self.left:
                    self.left.insert(data)
                else:
                    self.left = Node(data)
            else:
                if self.right:
                    self.right.insert(data)
                else:
                    self.right = Node(data)
        else:
            self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()

    def print_tree_rl(self):
        if self.right:
            self.right.print_tree_rl()
        print(self.data)
        if self.left:
            self.left.print_tree_rl()


if __name__ == '__main__':
    n = Node(5)
    n.insert(3)
    n.insert(8)
    n.insert(13)
    print('print tree in ascending order:')
    n.print_tree()
    print('print tree in descending order:')
    n.print_tree_rl()


from functools import lru_cache
lru_cache