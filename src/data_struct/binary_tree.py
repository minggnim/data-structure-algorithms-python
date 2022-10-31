class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.max_depth = 0

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

    def print_tree(self, data_list=[]):
        if self.left:
            self.left.print_tree(data_list)
        data_list.append(self.data)
        print(self.data)
        if self.right:
            self.right.print_tree(data_list)
        return data_list

    def print_tree_rl(self, data_list=[]):
        if self.right:
            self.right.print_tree_rl(data_list)
        data_list.append(self.data)
        print(self.data)
        if self.left:
            self.left.print_tree_rl(data_list)
        return data_list


class NodeOperation(object):
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
            self.traversed_list += [node.data]
            self.inorder_traversal_recursive(node.right)
        return self.traversed_list

    def inorder_traversal_iterative(self, node):
        stack = [node]
        while stack:
            node = stack.pop()
            if isinstance(node, Node):
                stack.append(node.right)
                stack.append(node.data)
                stack.append(node.left)
            elif node:
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

    def check_symmetric_tree(self, root: Node) -> bool:
        if not root:
            return True
        return self.check_symmetric_recursive(root.left, root.right)

    def check_symmetric_recursive(self, branch_left: Node, branch_right: Node) -> bool:
        if branch_left and branch_right is None:
            return True
        if branch_left is None or branch_right is None:
            return False
        return (
            branch_left.data == branch_right.data
            and self.check_symmetric_recursive(branch_left.left, branch_right.right)
            and self.check_symmetric_recursive(branch_left.right, branch_right.left)
        )


class MaxDepth:
    '''
    time: O(num_nodes)
    space: O(num_levels)
    '''
    def max_depth_bottom_up(self, root) -> int:
        # bottom condition
        if not root:
            return 0
        # call function recursively for left child
        left_depth = self.max_depth_bottom_up(root.left)
        # call function recursively for right child
        right_depth = self.max_depth_bottom_up(root.right)
        return max(left_depth, right_depth) + 1

    def max_depth_top_down(self, root: Node, depth: int = 1) -> int:
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


class MinDepth:
    def min_depth_dfs(self, root) -> int:
        if not root:
            return 0
        if root.left and root.right:
            return min(self.min_depth_dfs(root.left), self.min_depth_dfs(root.right)) + 1
        else:
            return self.min_depth_dfs(root.left or root.right) + 1

    def min_depth_bfs(self, root) -> int:
        import collections
        if not root:
            return 0
        queue = collections.deque((root, 1))
        while queue:
            node, level = queue.popleft()
            # only consider when node exists
            if node:
                # terminates at the leaf node
                if not node.left and not node.right:
                    return level
                else: # at lease one node exists
                    queue.append((node.left, level + 1))
                    queue.append((node.right, level + 1))
                

class BinaryTreePath:
    def tree_path_dfs(self, root: Optional[TreeNode]) -> List[str]:
        if not root:
            return []
        if not root.left and not root.right:
            return [str(root.val)]
        return [str(root.val) + '->' + i for i in self.tree_path_dfs(root.left)] + [str(root.val) + '->' + i for i in self.tree_path_dfs(root.right)]
