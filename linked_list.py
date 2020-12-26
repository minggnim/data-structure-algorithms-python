import logging

logger = logging.getLogger(__name__)


def __type_check__(fn):
    def decorated(*args, **kwargs):
        if isinstance(kwargs["new_node"], Node):
            return fn(*args, **kwargs)
        else:
            logger.error("Value error: not a Node instance")
            # raise Exception('Value error: not a Node instance')

    return decorated


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class linkedList(object):
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        if node is not None:
            yield node
            node = node.next

    @__type_check__
    def insert_first(self, new_node=None):
        new_node.next = self.head
        self.head = new_node

    def insert_middle(self, target_node_data, new_node):
        cur_node = self.head
        while cur_node is not None:
            if cur_node.data == target_node_data:
                new_node.next = cur_node.next
                cur_node.next = new_node
                break
            cur_node = cur_node.next

    @__type_check__
    def insert_last(self, new_node=None):
        if self.head is not None:
            cur_node = self.head
            while cur_node.next is not None:
                cur_node = cur_node.next
                pass
            last_node = cur_node
            last_node.next = new_node
        else:
            logger.error("Value error: no head node found")
