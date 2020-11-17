class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.len = 0


    def __repr__(self):
        ls_node = []
        cur_node = self.head
        while cur_node:
            ls_node.append(str(cur_node.val))
            cur_node = cur_node.next
        return ' -> '.join(ls_node)
        

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if not self.head:
            return -1 
        else:
            idx = 0
            cur_node = self.head
            while idx < index and cur_node.next:
                cur_node = cur_node.next
                idx += 1
                
            if idx == index:
                return cur_node.val
            else:
                return -1
        

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. 
        After the insertion, the new node will be the first node of the linked list.
        """
        new_head = Node(val)
        if self.head:
            new_head.next = self.head
        self.head = new_head
        
        self.len += 1
        

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if self.head:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = Node(val)
        else:
            self.head = Node(val)
            
        self.len += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. 
        If index equals to the length of linked list, the node will be appended to the end of linked list. 
        If index is greater than the length, the node will not be inserted.
        """
        if index == 0:
            self.addAtHead(val)
        elif index == self.len:
            self.addAtTail(val)
        elif index < self.len:
            idx = 0
            cur_node = self.head
            while idx < index-1:
                cur_node = cur_node.next
                idx += 1

            new_node = Node(val)
            if cur_node.next:
                new_node.next = cur_node.next
                cur_node.next = new_node  
            else:
                cur_node.next = new_node
            
            self.len += 1


    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index == 0:
            self.head = self.head.next
            self.len -= 1
        elif index < self.len:
            cur_node = self.head
            idx = 0
            while idx < index-1:
                cur_node = cur_node.next
                idx += 1

            if cur_node.next.next:
                cur_node.next = cur_node.next.next
            else:
                cur_node.next = None
            
            self.len -= 1