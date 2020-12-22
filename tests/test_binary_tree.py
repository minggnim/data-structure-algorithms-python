from binary_tree import Node

def test_node():
    n = Node(5)
    n.insert(3)
    n.insert(8)

    n.print_tree_rl()
