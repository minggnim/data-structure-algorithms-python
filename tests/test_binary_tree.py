from binary_tree import Node, nodeOperation
import pytest


@pytest.fixture(scope="module")
def empty_tree():
    return None


@pytest.fixture(scope="module")
def tree():
    root = Node(5)
    nodes = [3, 4, 1, 10, 8, 6, 2, 7, 9]
    for n in nodes:
        root.insert_node(n)
    return root


@pytest.fixture(scope="module")
def sym_tree():
    root = Node(5)
    root.left = root.right = Node(3)
    root.left.left = root.right.right = Node(1)
    root.left.right = root.right.left = Node(2)
    return root


def test_print_tree(tree, empty_tree):
    data_list = tree.print_tree()
    assert data_list == list(range(1, 11))


def test_print_tree_rl(tree):
    data_list = tree.print_tree_rl()
    assert data_list == list(range(10, 0, -1))


def test_preorder_traversal(tree):
    preorder_iterative = nodeOperation().preorder_traversal_iterative(tree)
    preorder_recursive = nodeOperation().preorder_traversal_recursive(tree)
    assert preorder_iterative == preorder_recursive == [5, 3, 1, 2, 4, 10, 8, 6, 7, 9]


def test_inorder_traversal(tree):
    inorder_recursive = nodeOperation().inorder_traversal_recursive(tree)
    inorder_iterative = nodeOperation().inorder_traversal_iterative(tree)
    assert inorder_recursive == inorder_iterative == list(range(1, 11))


def test_postorder_traversal(tree):
    postorder_recursive = nodeOperation().postorder_traversal_recursive(tree)
    assert postorder_recursive == [2, 1, 4, 3, 7, 6, 9, 8, 10, 5]


def test_max_depth(tree, empty_tree):
    top_down = nodeOperation().max_depth_top_down(tree)
    bottom_up = nodeOperation().max_depth_bottom_up(tree)
    assert top_down == bottom_up == 5
    top_down = nodeOperation().max_depth_top_down(empty_tree)
    bottom_up = nodeOperation().max_depth_bottom_up(empty_tree)
    assert top_down == bottom_up == 0


def test_check_tree_symmetric(empty_tree, tree, sym_tree):
    assert nodeOperation().check_symmetric_tree(empty_tree)
    assert not nodeOperation().check_symmetric_tree(tree)
    assert nodeOperation().check_symmetric_tree(sym_tree)
