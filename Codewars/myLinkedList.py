#!usr/bin/env python

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


class LinkedList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def add_last(self, node):
        if self.head is None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.next = node

    def add_after(self, target_node_data, new_data):
        if self.head is None:
            raise Exception("List is empty!")

        for node in self:
            if node.data == target_node_data:
                new_data.next = node.next
                node.next = new_data
                return

        raise Exception("Node with data '%s' not found" % target_node_data)

    def add_before(self, target_node_data, new_node):
        if self.head is None:
            raise Exception("List is empty!")

        if self.head.data == target_node_data:
            return self.add_first(new_node)

        prev_node = self.head

        for node in self:
            if node.data == target_node_data:
                prev_node.next = new_node
                new_node.next = node
                return
            prev_node = node

        raise Exception("Node with data '%s' not found" % target_node_data)

    def remove_node(self, target_node_data):
        if self.head is None:
            raise Exception("List is empty!")

        if self.head.data == target_node_data:
            self.head = self.head.next
            return

        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node
        raise Exception("Node with data '%s' not found" % target_node_data)

    def get(self, target_position):
        if self.head is None:
            raise Exception("List is empty!")

        node = self.head
        nlist = []

        while node is not None:
            nlist.append(node.data)
            node = node.next

        if target_position > len(nlist):
            raise Exception("List is out of range!")

        else:
            print(nlist[target_position - 1])

    def get_len(self):
        if self.head is None:
            raise Exception("List is empty!")

        node = self.head
        nlist = []

        while node is not None:
            nlist.append(node.data)
            node = node.next

        print(len(nlist))

    def reverse(self):
        if self.head is None:
            raise Exception("List is empty!")

        for node in self:
            if node.data == 'None':
                return
            else:
                self.head = self.head.next
