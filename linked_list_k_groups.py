class LNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def reverseListK(head, k):
    print("test")



node1 = LNode(1)
node2 = LNode(2)
node3 = LNode(3)
node4 = LNode(4)
node5 = LNode(5)
node6 = LNode(6)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

reverseListK(node1, 2)

