#!usr/bin/env python

from myLinkedList import LinkedList
from myLinkedList import Node


my_LinkedList = LinkedList()

first_node = Node("a")
my_LinkedList.head = first_node

second_node = Node("b")
third_node = Node("c")

first_node.next = second_node
second_node.next = third_node

print(my_LinkedList)

my_LinkedList.add_first(Node("k"))
my_LinkedList.add_first(Node("v"))
my_LinkedList.add_first(Node("e"))

for node in my_LinkedList:
    print(node)

my_LinkedList.add_last(Node("y"))
my_LinkedList.add_last(Node("i"))

print(my_LinkedList)

my_LinkedList.add_after("v", Node("22"))

print(my_LinkedList)

my_LinkedList.add_before("c", Node("ttt"))

print(my_LinkedList)

my_LinkedList.remove_node("ttt")

print(my_LinkedList)

my_LinkedList.get_len()
my_LinkedList.get(1)
my_LinkedList.get(9)

my_LinkedList.reverse()

print(my_LinkedList)
