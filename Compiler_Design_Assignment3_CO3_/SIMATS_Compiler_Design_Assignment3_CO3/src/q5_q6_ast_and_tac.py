"""Q5 & Q6: AST Constructor (mkNode / mkLeaf) & Three-Address Code Generator."""

class ASTNode:
    def __init__(self, op, left=None, right=None):
        self.op = op
        self.left = left
        self.right = right

def mk_node(op, left, right):
    return ASTNode(op, left, right)

def mk_leaf(val):
    return ASTNode(val)

class TACGen:
    def __init__(self):
        self.temp_id = 0
        self.code = []

    def new_temp(self):
        self.temp_id += 1
        return f"t{self.temp_id}"

    def gen(self, node):
        if node.left is None and node.right is None:
            return node.op
        if node.op == "=":
            rhs = self.gen(node.right)
            self.code.append(f"{node.left.op} = {rhs}")
            return node.left.op
        l_addr = self.gen(node.left)
        r_addr = self.gen(node.right)
        t = self.new_temp()
        self.code.append(f"{t} = {l_addr} {node.op} {r_addr}")
        return t

if __name__ == "__main__":
    # AST & TAC for x = a + b * c - d
    ast = mk_node("=", mk_leaf("x"),
                  mk_node("-",
                          mk_node("+", mk_leaf("a"), mk_node("*", mk_leaf("b"), mk_leaf("c"))),
                          mk_leaf("d")))
    tac = TACGen()
    tac.gen(ast)
    print("Three-Address Code for x = a + b * c - d:")
    for line in tac.code:
        print(" ", line)
