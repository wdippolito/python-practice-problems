class LLNode:
    def __init__(self, x):
        self.next = None
        self.val = x

def mergeLists(l1, l2):
    
    if not l1:
        return l2
    if not 12:
        return l1

    if l1.val > l2.val:
        l3 = l2
        l2.next
    else: 
        l3 = l1
        l1 = l1.next

    tail = l3

    while l1 and l2:

        if l1.val > l2.val:
            tail.next = l2
            l2 = l2.next
        else:
            tail.next = l1
            l1 = l1.next
        tail = tail.next
    tail.next = l1 if l1 else l2

    while l3:
        print(l3.val)
        l3 = l3.next

def mergeAlt(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1
    
    l3 = l1
    l1 = l1.next

    tail = l3

    flag = True # when true, append from list 2, when false append from list 1

    while l1 and l2:
        if flag:
            tail.next = l2
            l2 = l2.next
        else:
            tail.next = l1
            l1 = l1.next
        
        tail = tail.next
        flag = not flag
    
    tail.next = l1 if l1 else l2

    while l3:
        print(l3.val)
        l3 = l3.next

node1 = LLNode(1)
node2 = LLNode(3)
node3 = LLNode(5)
node4 = LLNode(7)
node5 = LLNode(2)
node6 = LLNode(4)
node7 = LLNode(6)

node1.next = node2
node2.next = node3
node3.next = node4

node5.next = node6
node6.next = node7

# mergeLists(node1, node5)
mergeAlt(node5, node1)
