"""Q4: Syntax-Directed Translation Scheme (Infix to Postfix)."""
import re

class InfixToPostfixSDT:
    def __init__(self, expr):
        self.tokens = re.findall(r'\d+|[+\-*/()]', expr)
        self.pos = 0
        self.out = []

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consume(self):
        tok = self.tokens[self.pos]
        self.pos += 1
        return tok

    def parse_E(self):
        self.parse_T()
        while self.peek() in ('+', '-'):
            op = self.consume()
            self.parse_T()
            self.out.append(op)

    def parse_T(self):
        self.parse_F()
        while self.peek() in ('*', '/'):
            op = self.consume()
            self.parse_F()
            self.out.append(op)

    def parse_F(self):
        tok = self.peek()
        if tok == '(':
            self.consume()
            self.parse_E()
            self.consume()
        else:
            self.out.append(self.consume())

if __name__ == "__main__":
    expr = "3 * (4 + 5) - 6 / 2"
    sdt = InfixToPostfixSDT(expr)
    sdt.parse_E()
    print("Infix Input   :", expr)
    print("Postfix Output:", " ".join(sdt.out))
