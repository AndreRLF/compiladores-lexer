from interpreter import Interpreter
from ply_parser import parser

text = "3 + 2 - 6"

t = parser.parse(text)

q = []


def dps(tree, w):
    if type(tree) is not tuple:
        w.append(tree)
        return
    dps(tree[0], w)
    dps(tree[1], w)
    w.append(tree[2])


dps(t, q)

print(q)

interpreter = Interpreter(code=q)
interpreter.start()

print(interpreter.stack)