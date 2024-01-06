class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

node1 = ListNode(1)
node2 = ListNode(3)
node3 = ListNode(5)

node1.next = node2
node2.next = node3

def reverseList(head):
    if head is None or head.next is None:
        return head
    new_head = reverseList(head.next)
    new_head.next = head
    head.next = None
    return new_head

class MyQueue:
    
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        return self.head is None
    
    def enque(self, value):
        new_node = ListNode(value)
        if self.isEmpty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
    
    def deque(self):
        if self.isEmpty():
            raise Exception("Empty")
        value = self.head.val
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return value

class MyStack:
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, value):
        new_node = ListNode(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.isEmpty():
            raise Exception("empty")
        value = self.top.val
        self.top = self.top.next
        return value


q = MyQueue()

q.enque(1)
q.enque(3)
q.enque(5)
q.enque(7)
print(q.deque())
print(q.deque())
print(q.deque())
print(q.deque())

s = MyStack()

s.push(1)
s.push(3)
s.push(5)
s.push(7)
print(s.pop())
print(s.pop())
print(s.pop())
print(s.pop())

# reverseList(node1)
# print(node3.next.next.val)
