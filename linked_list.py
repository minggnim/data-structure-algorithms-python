class linkedList(object):
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        return(' -> '.join(nodes))


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

        
