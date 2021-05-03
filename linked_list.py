import logging
logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.INFO)


def __type_check__(fn):
    def decorated(*args, **kwargs):
        if isinstance(kwargs["new_node"], Node):
            return fn(*args, **kwargs)
        else:
            logging.error("Value error: not a Node instance")
    return decorated


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList(object):
    def __init__(self, head = None):
        self.head = head

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
            logging.error("Value error: no head node found")


def create_linked_list():
    head = Node(0)
    head.next = Node(1)
    head.next.next = Node(2)
    ll = LinkedList(head)
    return ll


def reverse_linked_list(ll):
    # initial setting
    cur_node = ll.head
    new_next = None
    while cur_node.next:
        # reverse the next node
        cur_next = cur_node.next
        cur_node.next = new_next
        # prepare for the next iter
        new_next = cur_node
        cur_node = cur_next
    cur_node.next = new_next
    return cur_node


def reverse_linked_list_recursive(cur_node):
    if cur_node is None or cur_node.next is None:
        return cur_node
    # reverse the rest of the list
    rest_list = reverse_linked_list_recursive(cur_node.next)
    # redirect the pointer from the next to the current
    cur_node.next.next = cur_node
    # break the pointer from the current to the next
    cur_node.next = None
    return rest_list


if __name__ == '__main__':
    ll = create_linked_list()
    logging.info(f'linked list {ll}')
    rev_head = reverse_linked_list(ll)
    rev_ll = LinkedList(rev_head)
    logging.info('1. Iterative Approach:')
    logging.info(f'reversed linked list {rev_ll}')
    logging.info(f'check original linked list {ll}')
    logging.info(f'2. Recursive Approach:')
    ll = create_linked_list()
    rev_head_rec = reverse_linked_list_recursive(ll.head)
    rev_ll_rec = LinkedList(rev_head_rec)
    logging.info(f'reversed linked list {rev_ll_rec}')
    logging.info(f'check original linked list {ll}')
