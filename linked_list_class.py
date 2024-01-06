#!/usr/bin/python
# -*- coding: utf-8 -*-


class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def delete(self, key):
        curr = self.head

        if curr and curr.data == key:
            self.head = curr.next
            curr = None
            return

        prev = None

        while curr and curr.data != key:
            prev = curr
            curr = curr.next

        prev.next = curr.next
        curr = None

    def delete_by_pos(self, pos):
        curr = self.head

        if self.head:
            curr    

    def reverse_iter(self):
        prev = None
        curr = self.head

        while curr:
            next_Node = curr.next
            curr.next = prev
            prev = curr
            curr = next_Node
        self.head = prev


    def merge(self, llist_1):
        c1 = llist_1.head
        c2 = self.head
        result = None
        new_head = c2
        if not c1:
            return c2
        if not c2:
            return c1
        if c1 and c2:
            if c1.data <= c2.data:
                result = c1
                c1 = c1.next
                new_head = result
            else:
                result = c2
                c2 = c2.next
                new_head = result
    
    def merge2(self, llist_1):
        c1 = llist_1.head
        c2 = self.head
        result = None

        if c1.data > c2.data:
            result = c1
        else:
            result = c2

        tail = result

        while c1 and c2:
            

llist = LinkedList()
llist.append(1)
llist.append(4)
llist.append(7)
llist.append(9)

llist.print_list()

llist2 = LinkedList()
llist2.append(3)
llist2.append(5)
llist2.append(8)
llist2.append(9)

llist2.print_list()

