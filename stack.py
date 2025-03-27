"""
Implementation of a Stack data structure using a Python list.
"""


class Stack:
    """A class implementing stack data structure using a list."""
    def create(self, data):
        """
        Create a stack from an iterable.

        Args:
            data: An iterable containing elements to create the stack
        """
        if len(data) == 0:
            return
        for item in data:
            self.push(item)

    def __init__(self, data=None):
        """
        Initialize a new Stack.

        Args:
            data (optional): Initial data to populate the stack
        """
        self.array = []
        if data:
            self.create(data)

    def push(self, item):
        """
        Push an item onto the top of the stack.

        Args:
            item: The item to be pushed onto the stack
        """
        self.array.append(item)

    def pop(self):
        """
        Remove and return the top item from the stack.

        Returns:
            The top item if stack is not empty, None otherwise
        """
        if self.length() == 0:
            return None
        return self.array.pop()

    def top(self):
        """
        Return the top item from the stack without removing it.

        Returns:
            The top item if stack is not empty, 'No TOP' otherwise
        """
        if self.length() == 0:
            return "No TOP"
        return self.array[-1]

    def length(self):
        """
        Get the current number of items in the stack.

        Returns:
            int: The number of items in the stack
        """
        return len(self.array)

    def display(self):
        """
        Display all elements in the stack.
        Prints the stack in array format.
        """
        print("Stack:", self.array)


def test_stack():
    """Test function to demonstrate stack operations."""
    stack = Stack([1, 2, 3])
    stack.display()         # Expected: Stack: [1, 2, 3]
    print(stack.top())      # Expected: 3
    stack.push(4)
    stack.display()         # Expected: Stack: [1, 2, 3, 4]
    print(stack.pop())      # Expected: 4
    stack.display()         # Expected: Stack: [1, 2, 3]
    print(stack.top())      # Expected: 3
    stack.pop()
    stack.pop()
    stack.pop()
    print(stack.pop())      # Expected: None


if __name__ == "__main__":
    test_stack()
