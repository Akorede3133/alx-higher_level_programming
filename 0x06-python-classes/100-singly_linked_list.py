#!/usr/bin/python3
"""Defining a Node class"""

class Node:
    """A singly list node"""
    def __init__(self, data, next_node=None):
        """initializing the node"""
        self.data = data
        self.next_node = next_node
    
    @property
    def data(self):
        """return data"""
        return (self.__data)
    @data.setter
    def data(self, value):
        """sets the data"""
        if type(value) != int:
            raise TypeError('data must be an integer')
        else:
            self.__data = value
    @property
    def next_node(self):
        """returns next node"""
        return (self.__next_node)
    @next_node.setter
    def next_node(self, value):
        """sets next node"""
        if value != None and type(value) != Node:
            raise TypeError('next_node must be a Node object')
        else:
            self.__next_node = value

class SinglyLinkedList:
    """singly linked list class"""
    def __init__(self):
        self.__head = None
    def sorted_insert(self, value):
        newNode = Node(value)
        if self.__head is None:
            newNode.next_node = None
            self.__head = newNode
        elif self.__head.data > value:
            newNode.next_node = self.__head
            self.__head = newNode
        else:
            current = self.__head
            while (current.next_node is not None and
                    current.next_node.data < value):
                current = current.next_node
            newNode.next_node = current.next_node
            current.next_node = newNode

    def __str__(self):
        nums = []
        current = self.__head
        while (current):
            string = str(current.data)
            nums.append(string)
            current = current.next_node
        return ("\n".join(nums))



sll = SinglyLinkedList()
sll.sorted_insert(2)
sll.sorted_insert(5)
sll.sorted_insert(3)
sll.sorted_insert(10)
sll.sorted_insert(1)
sll.sorted_insert(-4)
sll.sorted_insert(-3)
sll.sorted_insert(4)
sll.sorted_insert(5)
sll.sorted_insert(12)
sll.sorted_insert(3)
print(sll)

