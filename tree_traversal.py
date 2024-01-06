class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
    
    def insert(self,data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else: 
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def insert2(self, data):
        #if self has data, decide left or right new node based on value of self data vs new data

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert2(data)
            if data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert2(data)

        else:
            self.data = data    
    
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data),
        if self.right:
            self.right.print_tree()

    def inorder_traversal(self, root):
        res = []
        if root:
            res = self.inorder_traversal(root.left)
            res.append(root.data)
            res = res + self.inorder_traversal(root.right)
        return res
    
    def preorder_traversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorder_traversal(root.left)
            res = res + self.preorder_traversal(root.right)
        return res

    def post_order_traversal(self, root):
        res = []
        if root:
            res = self.post_order_traversal(root.left)
            res = res + self.post_order_traversal(root.right)
            res.append(root.data)
        return res

    def inorder2(self, root):
        res = []
        if root:
            res = res + self.inorder2(root.left)
            res.append(root.data)
            res = res + self.inorder2(root.right)
        return res

    def preorder2(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.preorder2(root.left)
            res = res + self.preorder2(root.right)
        return res

    def postorder2(self, root):
        res = []
        if root:
            res = res + self.postorder2(root.left)
            res = res + self.postorder2(root.right)
            res.append(root.data)
        return res


def find_bin(A, target):

    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (low+high) // 2

        if target == A[mid]:
            return True
        elif target < A[mid]:
            high = mid -1
        elif target > A[mid]:
            low = mid + 1 
    return False

def find_div(A, target): # find index of 2 side by side elements which are evenly divisible 22 % 11 = 0 and one = target
    low = 0
    high = len(A) - 1

    while low <= high:
        mid = (high + low) // 2 
        left = A[mid -1] if mid -1 >= 0 else float(0.1)
        if A[mid] == target:
            if A[mid] % left == 0 or left % A[mid] == 0:
                return [mid, (mid -1)]
            else: 
                return None
        elif A[mid] > target:
            high = mid - 1 
        elif A[mid] < target:
            low = mid + 1
    return False





    

root = Node(33)
root.insert2(22)
root.insert2(44)
root.insert2(55)
root.insert2(77)
root.insert2(11)
root.insert2(5)
root.insert2(7)
print(root.data)
root.print_tree()
print(root.inorder_traversal(root))
print(root.inorder2(root))
print(root.preorder_traversal(root))
print(root.preorder2(root))
print(root.post_order_traversal(root))
print(root.postorder2(root))

A1 = root.post_order_traversal(root)

A1.sort()
print(A1)
print(find_bin(A1, 33))
print(find_div(A1, 44))




