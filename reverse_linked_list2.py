class Node:
    def __init__(self,x):
        self.val = x
        self.next = None

node1 = Node(1)
node2 = Node(3)
node3 = Node(5)

node1.next = node2
node2.next = node3

def reverse(head):
    curr, prev = head, None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    head = prev
    while head:

        print(head.val)
        head = head.next


def reverse2(head):
    curr, prev = head, None
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    head = prev    
    while head:

        print(head.val)
        head = head.next    

def reverse3(head):
    curr, prev = head, None

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    head = prev
    while head:

        print(head.val)
        head = head.next  


def merge(l1, l2):
    

    
reverse3(node1)
        