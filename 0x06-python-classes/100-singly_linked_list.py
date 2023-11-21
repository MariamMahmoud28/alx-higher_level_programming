#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node:
    """Defines a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """Initializes a new instance of the Node class.

        Args:
            data (int): The data of the node.
            next_node (Node): The next node in the linked list (default is None).
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter method to retrieve the data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter method to set the data of the node.

        Args:
            value (int): The data to be set.

        Raises:
            TypeError: If data is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        else:
            self.__data = value

    @property
    def next_node(self):
        """Getter method to retrieve the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter method to set the next node.

        Args:
            value (Node): The next node to be set.

        Raises:
            TypeError: If next_node is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        else:
            self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list."""

    def __init__(self):
        """Initializes a new instance of the SinglyLinkedList class."""
        self.head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list (increasing order).

        Args:
            value (int): The value to be inserted.
        """
        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and current.next_node.data < value:
                current = current.next_node

            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Returns a string representation of the linked list."""
        result = ""
        current = self.head
        while current:
            result += str(current.data) + "\n"
            current = current.next_node
        return result.rstrip()


# Example usage:
linked_list = SinglyLinkedList()
linked_list.sorted_insert(5)
linked_list.sorted_insert(2)
linked_list.sorted_insert(8)
linked_list.sorted_insert(1)

print(linked_list)
