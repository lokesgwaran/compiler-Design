"""Q7: Hybrid Iterative LL(1) + Shunting-Yard Operator-Precedence Parser."""

PREC = {"OR": 1, "AND": 2, "<": 3, ">": 3, "==": 3}

def shunting_yard_ast(expr_tokens):
    op_stack = []
    val_stack = []
    ops_count = 0
    for tok in expr_tokens:
        ops_count += 1
        if tok == "(":
            op_stack.append(tok)
        elif tok == ")":
            while op_stack and op_stack[-1] != "(":
                op = op_stack.pop()
                r, l = val_stack.pop(), val_stack.pop()
                val_stack.append((op, l, r))
            op_stack.pop()
        elif tok in PREC:
            while op_stack and op_stack[-1] in PREC and PREC[op_stack[-1]] >= PREC[tok]:
                op = op_stack.pop()
                r, l = val_stack.pop(), val_stack.pop()
                val_stack.append((op, l, r))
            op_stack.append(tok)
        else:
            val_stack.append(tok)
    while op_stack:
        op = op_stack.pop()
        r, l = val_stack.pop(), val_stack.pop()
        val_stack.append((op, l, r))
    return val_stack[0], ops_count

if __name__ == "__main__":
    tokens = ["(", "moisture", "<", "30", "AND", "temp", ">", "25", ")", "OR", "rain", "==", "0"]
    ast, steps = shunting_yard_ast(tokens)
    print("Hybrid Operator-Precedence AST:", ast)
    print(f"Iterative Operations Count: {steps} (C Call-Stack Depth = O(1) constant)")
