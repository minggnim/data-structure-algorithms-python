class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def insert_node(self, data):
        if self.data:
            if self.data > data:
                if self.left:
                    self.left.insert_node(data)
                else:
                    self.left = Node(data)
            else:
                if self.right:
                    self.right.insert_node(data)
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

class nodeOperation(object):
    def __init__(self):
        self.sorted_nodes = []
        self.traversed_list = []
        self.max_depth = 0

    def preorder_traversal_recursive(self, node):
        if node:
            self.traversed_list.append(node.data)
            self.preorder_traversal_recursive(node.left)
            self.preorder_traversal_recursive(node.right)
        return self.traversed_list

    def preorder_traversal_iterative(self, node):
        stack = [node]
        while stack:
            node = stack.pop()
            if node is not None:
                self.traversed_list.append(node.data)
                stack.append(node.right)
                stack.append(node.left)
        return self.traversed_list

    def inorder_traversal_recursive(self, node):
        if node:
            self.inorder_traversal_recursive(node.left)
            self.traversed_list += [node.val]
            self.inorder_traversal_recursive(node.right)
        return self.traversed_list

    def inorder_traversal_iterative(self, node):
        if node:
            if isinstance(node, Node):
                self.inorder_traversal_recursive(node.right)
                self.inorder_traversal_recursive(node.val)
                self.inorder_traversal_recursive(node.left)
            else:
                self.traversed_list += [node]
        return self.traversed_list

    def postorder_traversal_recursive(self, node):
        res = []
        def pot(node, res=res):
            if node:
                pot(node.left)
                pot(node.right)
                res += [node.data]
        pot(node)
        return res

    def max_depth_bottom_up(self, root) -> int:
        # bottom condition
        if not root:
            return 0
        # call function recursively for left child
        left_depth = self.max_depth_bottom_up(root.left)
        # call function recursively for right child
        right_depth = self.max_depth_bottom_up(root.right)
        return max(left_depth, right_depth) + 1

    def max_depth_top_down(self, root, depth: int = 1) -> int:
        # bottom condition
        if not root:
            return self.max_depth
        # update condition -- when the node is a leaf
        if not root.left and not root.right:
            self.max_depth = max(self.max_depth, depth)
        # call function recursively for left child
        self.max_depth_top_down(root.left, depth + 1)
        # call function recursively for right child
        self.max_depth_top_down(root.right, depth + 1)
        return self.max_depth


if __name__ == '__main__':
    n = Node(5)
    n.insert_node(3)
    n.insert_node(8)
    n.insert_node(13)
    n.insert_node(10)
    print('print tree in ascending order:')
    n.print_tree()
    print('print tree in descending order:')
    n.print_tree_rl()
