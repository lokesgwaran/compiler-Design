"""Q1 & Q2: Left-Recursion-Free Expression Recursive-Descent & LL(1) Table Parser."""

class RecursiveDescentParser:
    def __init__(self, expr):
        self.tokens = [ch for ch in expr if not ch.isspace()]
        self.pos = 0
        self.trace = []

    def peek(self):
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def match(self, expected):
        if self.peek() == expected:
            self.trace.append(f"Match '{expected}'")
            self.pos += 1
        else:
            raise SyntaxError(f"Syntax Error at index {self.pos}: expected '{expected}', found '{self.peek()}'")

    def parse_E(self):
        self.trace.append("E -> T E'")
        self.parse_T()
        self.parse_E_prime()

    def parse_E_prime(self):
        if self.peek() in ('+', '-'):
            op = self.peek()
            self.trace.append(f"E' -> {op} T E'")
            self.match(op)
            self.parse_T()
            self.parse_E_prime()
        else:
            self.trace.append("E' -> epsilon")

    def parse_T(self):
        self.trace.append("T -> F T'")
        self.parse_F()
        self.parse_T_prime()

    def parse_T_prime(self):
        if self.peek() in ('*', '/'):
            op = self.peek()
            self.trace.append(f"T' -> {op} F T'")
            self.match(op)
            self.parse_F()
            self.parse_T_prime()
        else:
            self.trace.append("T' -> epsilon")

    def parse_F(self):
        tok = self.peek()
        if tok == '(':
            self.trace.append("F -> ( E )")
            self.match('(')
            self.parse_E()
            self.match(')')
        elif tok and tok.isalpha():
            self.trace.append(f"F -> id ({tok})")
            self.match(tok)
        else:
            raise SyntaxError(f"Syntax Error at index {self.pos}: unexpected '{tok}'")

if __name__ == "__main__":
    valid_input = "r * ( p + f ) - d $"
    parser = RecursiveDescentParser(valid_input)
    parser.parse_E()
    parser.match('$')
    print(f"Input: {valid_input} -> Parsing succeeded! ({len(parser.trace)} steps)")
    for step in parser.trace:
        print(" ", step)

    invalid_input = "r * + f $"
    try:
        bad_parser = RecursiveDescentParser(invalid_input)
        bad_parser.parse_E()
    except SyntaxError as err:
        print(f"\nInvalid Input '{invalid_input}' -> {err}")
