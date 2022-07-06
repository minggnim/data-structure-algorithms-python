import math
import logging
from typing import Optional, List

logging.basicConfig(level=logging.INFO)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_bst():
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    return root


def build_invalid_bst():
    root = TreeNode(4)
    root.left = TreeNode(3)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(5)
    return root


def search_bst(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    '''
    Input: root = [4,2,7,1,3], val = 2
    Output: [2,1,3]
    '''
    if not root:
        return None
    elif root.val == val:
        return root
    elif root.val < val:
        return search_bst(root.right, val)
    else:
        return search_bst(root.left, val) 


def generate_trees(n: int) -> List[Optional[TreeNode]]:
    '''
    Example:
        Input: n = 3
        Output: [[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
    Solution:
        - at each node
            head = TreeNode(i)
            head.left = TreeNode(j) where j < i
            head.right = TreeNode(k) where k > i
        - stop when no more values to add
    '''
    def rec(start, end):
        if start == end:
            return [None]
        res = []
        for i in range(start, end):
            for l in rec(start, i):
                for r in rec(i+1, end):
                    node = TreeNode(i)
                    node.left = TreeNode(l)
                    node.right = TreeNode(r)
                    res.append(node)
        return res

    return rec(1, n+1)


class BSTIterator:
    '''
    Input
    ["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
    [[[7, 3, 15, null, null, 9, 20]], [], [], [], [], [], [], [], [], []]
    Output
    [null, 3, 7, true, 9, true, 15, true, 20, false]

    Explanation
    BSTIterator bSTIterator = new BSTIterator([7, 3, 15, null, null, 9, 20]);
    bSTIterator.next();    // return 3
    bSTIterator.next();    // return 7
    bSTIterator.hasNext(); // return True
    bSTIterator.next();    // return 9
    bSTIterator.hasNext(); // return True
    bSTIterator.next();    // return 15
    bSTIterator.hasNext(); // return True
    bSTIterator.next();    // return 20
    bSTIterator.hasNext(); // return False  
    '''
    def __init__(self, root: Optional[TreeNode]):
        self._vals = []
        self._counter = 0
        self.get_node_val(root)
        
    def get_node_val(self, root):
        if not root:
            return None
        self.get_node_val(root.left)
        self._vals.append(root.val)
        self.get_node_val(root.right) 

    def next(self) -> int:
        if self.hasNext():
            val = self._vals[self._counter]
            self._counter += 1
            return val
    
    def hasNext(self) -> bool:
        if self._counter < len(self._vals):
            return True
        return False


class validateBst(object):
    '''
    Given the root of a binary tree, determine if it is a valid binary search tree
    A valid BST is defined as follows:
        The left subtree of a node contains only nodes with keys less than the node's key
        The right subtree of a node contains only nodes with keys greater than the node's key
        Both the left and right subtrees must also be binary search trees
    A valid BST is created by function build_bst
    An invalid BST is created by function build_invalid_bst
    '''
    def __init__(self, root=None):
        self.root = root
    
    def validate_bst_rec(self, root: Optional[TreeNode]) -> bool:    
        def validate(node, low=-math.inf, high=math.inf):
            if not node:
                return True
            if node.val <= low or node.val >= high:
                return False
            logging.info(f'{node.val, low, high}')
            valid_left = validate(node.left, low, node.val)
            valid_right = validate(node.right, node.val, high)
            return valid_left and valid_right
        return validate(root)

    def validate_bst_iter(self, root: Optional[TreeNode]) -> bool:
        stack = [(root, -math.inf, math.inf)]
        while stack:
            root, low, high = stack.pop()
            if not root:
                continue
            elif root.val <= low or root.val >= high:
                return False
            else:
                stack.append([root.right, root.val, high])
                stack.append([root.left, low, root.val])
        return True
        