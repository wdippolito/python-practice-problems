#input is string, valid ips will have 4 elements between 0 255
#return True or false

#split input on char . list of 4 elements if valid

#iterate trhough list checkin each element between 0 255, return false if any arent
#return true

#important thing here is getting

#-----------------------------------------------------------
#word = "dnotq"
#result = "crime"

#Goal: decrypt the the receiving word 

#our result should be character in the word minus 1 and check if it is in the range of a-z
#if it is return it
#else keep on adding 26 to its ascii value till it comes in the range of a-z ascii value

# #a = 97 and z = 122
# #n = 110 + 101
# a:0 ....z:25

# 56%26

# 4+97
# #-----------------------------------------------------------

# node traverse to find the lowest cost path

#return interger which the sum of one branch.

class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    


def traverse(root, sum):
    if len(root.children) > 0:
        for i in range(len(root.children)):
            sum = root.data + traverse(root.children[i], sum)
            min_cost = min(tempCost, min_cost)
    else:
        return root.data
    return sum





