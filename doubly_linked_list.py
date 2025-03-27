"""
Implementation of a Doubly Linked List data structure.
"""


class Node:
    """A node in the doubly linked list."""
    def __init__(self, data):
        """
        Initialize a new Node in the doubly linked list.

        Args:
            data: The data to be stored in the node
        """
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """A class implementing doubly linked list data structure."""
    def create(self, data):
        """
        Create a doubly linked list from an iterable.

        Args:
            data: An iterable containing elements to create the list
        """
        if len(data) == 0:
            return
        for item in data:
            self.add_last(item)

    def __init__(self, data=None):
        """
        Initialize a new Doubly Linked List.

        Args:
            data (optional): Initial data to populate the list
        """
        self.tail = None
        self.length = 0
        self.head = None
        if data:
            self.create(data)

    def add_last(self, data):
        """
        Add a new node with given data at the end of the list.

        Args:
            data: The data to be added to the list
        """
        temp = Node(data)
        if self.length == 0:
            self.head = temp
            self.tail = temp
            self.length += 1
            return

        self.tail.next = temp
        temp.prev = self.tail
        self.tail = temp
        self.length += 1

    def display(self):
        """
        Display the contents of the doubly linked list.
        Prints elements in the format: element1 <-> element2 <-> ... <-> None
        """
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

    def remove_last(self):
        """
        Remove the last node from the doubly linked list.
        If list is empty, does nothing.
        """
        if self.length == 0:
            return
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length -= 1
            return

        self.tail.prev.next = None
        temp = self.tail
        self.tail = self.tail.prev
        temp.prev = None
        del temp
        self.length -= 1


def test_doubly_linked_list():
    """Test function to demonstrate doubly linked list operations."""
    dll = DoublyLinkedList([1, 2, 3, 4])
    dll.display()  # Expected: 1 <-> 2 <-> 3 <-> 4 <-> None
    dll.remove_last()
    dll.display()  # Expected: 1 <-> 2 <-> 3 <-> None

    dll.remove_last()
    dll.display()  # Expected: 1 <-> 2 <-> None

    dll.remove_last()
    dll.display()  # Expected: 1 <-> None

    dll.remove_last()
    dll.display()  # Expected: None (empty list)

    dll.remove_last()
    dll.display()  # Expected: None (no errors)


if __name__ == "__main__":
    test_doubly_linked_list()
