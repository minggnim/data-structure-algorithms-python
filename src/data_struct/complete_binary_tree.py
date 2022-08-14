from .binary_tree import Node


def build_complete_binary_tree():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    return root


def build_incomplete_binary_tree():
    root = Node(1)
    root.left = Node(2)
    root.left.left = Node(4)
    root.left.right = Node(5)
    return root


def count_nodes(root: Node) -> int:
    if not root:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


def is_complete_binary_tree(root, index, num_nodes):
    '''
    Check if the tree is a complete binary tree
    '''
    if root is None:
        return True
    # there'll be None in tree if it's not a complete binary tree
    if index >= num_nodes:
        return False
    return (is_complete_binary_tree(root.left, 2 * index + 1, num_nodes)
            and is_complete_binary_tree(root.right, 2 * index + 2, num_nodes))
