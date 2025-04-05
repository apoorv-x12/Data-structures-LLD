"""Implementation of a Least Recently Used (LRU) Cache using a doubly linked list."""


# pylint: disable=too-few-public-methods
class Node:
    """A node in a doubly linked list with key-value pair."""
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkedList:
    """Doubly Linked List implementation for LRU Cache."""
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.previous = self.head

    def insert_front(self, node):
        """Insert a node at the front of the list."""
        node.next = self.head.next
        node.next.previous = node
        self.head.next = node
        node.previous = self.head
        return self.head.next

    def pop(self, node):
        """Remove a node from the list and return it."""
        temp = node.previous
        temp.next = node.next
        node.next.previous = temp
        node.next = node.previous = None
        return node


class LRUCache:
    """Least Recently Used (LRU) cache implementation."""
    def __init__(self, capacity):
        self.capacity = capacity
        self.map = {}
        self.dll = DoublyLinkedList()

    def get(self, key):
        """Get the value for the given key. Returns -1 if key doesn't exist."""
        if key not in self.map:
            return -1
        remove_node = self.dll.pop(self.map[key])
        self.dll.insert_front(remove_node)
        return remove_node.value

    def put(self, key, value):
        """Insert or update a key-value pair in the cache."""
        if key in self.map:
            self.map[key].key = key
            self.map[key].value = value
            remove_node = self.dll.pop(self.map[key])
            self.dll.insert_front(remove_node)
            return

        if len(self.map) == self.capacity:
            node = self.dll.tail.previous
            remove_node = self.dll.pop(node)
            del self.map[remove_node.key]

        new_node = Node(key, value)
        self.dll.insert_front(new_node)
        self.map[key] = new_node
