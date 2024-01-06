import sys

to_Sum = [4,3,6,77,22,1]

s = "WhoGIVES a Shit"
r = ""
stack = []
for ch in s:
    stack.append(ch)

while stack:
    r += stack.pop()

print(r)