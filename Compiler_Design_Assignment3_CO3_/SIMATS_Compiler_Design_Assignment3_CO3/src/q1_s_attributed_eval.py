"""Q1: S-Attributed Arithmetic Expression Evaluator & Parse Tree Height."""

class Node:
    def __init__(self, label, val, children=None):
        self.label = label
        self.val = val
        self.children = children or []

    def height(self):
        if not self.children:
            return 0
        return 1 + max(c.height() for c in self.children)

def build_expr_tree():
    # Expression: 3 * (4 + 5) - 6 / 2
    n3 = Node("F", 3, [Node("num", 3)])
    n4 = Node("E", 4, [Node("T", 4, [Node("F", 4, [Node("num", 4)])])])
    n5 = Node("T", 5, [Node("F", 5, [Node("num", 5)])])
    e9 = Node("E", n4.val + n5.val, [n4, Node("+", 0), n5])
    f9 = Node("F", e9.val, [Node("(", 0), e9, Node(")", 0)])
    t27 = Node("T", n3.val * f9.val, [Node("T", 3, [n3]), Node("*", 0), f9])
    e27 = Node("E", t27.val, [t27])

    n6 = Node("T", 6, [Node("F", 6, [Node("num", 6)])])
    n2 = Node("F", 2, [Node("num", 2)])
    t3 = Node("T", n6.val // n2.val, [n6, Node("/", 0), n2])

    root = Node("E", e27.val - t3.val, [e27, Node("-", 0), t3])
    return root

if __name__ == "__main__":
    tree = build_expr_tree()
    print("Expression: 3 * (4 + 5) - 6 / 2")
    print(f"Root Synthesized E.val = {tree.val}")
    print(f"Parse Tree Height      = {tree.height()}")
