
from ply_parser import parser

"""
import operator

input = [12, 4, (operator.add, 2), 5, (operator.add, 2)]
stack = []

for t in input:
    if type(t) is int:
        stack.append(t)
    else:
        a = []
        for _ in range(t[1]):
            a.append(stack.pop())
        stack.insert(0, t[0](*a))

print(stack)
"""