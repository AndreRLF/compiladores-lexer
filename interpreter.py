import operator


class Interpreter:

    def __init__(self, code):
        self.stack = []
        self.code = code
        self.functions = {
            'ADD': (operator.add, 2),
            'SUB': (operator.sub, 2),
            'MUL': (operator.mul, 2),
            'DIV': (operator.truediv, 2)
        }

    def start(self):
        for token in self.code:
            if type(token) is float:
                self.stack.append(token)
            else:
                params = []
                for _ in range(self.functions[token][1]):
                    params.insert(0, self.stack.pop())
                self.stack.append(self.functions[token][0](*params))