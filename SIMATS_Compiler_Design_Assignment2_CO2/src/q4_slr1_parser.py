"""Q4: SLR(1) Table-Driven Parser for S' -> S, S -> CC, C -> cC | d."""

ACTION = {
    (0, 'c'): ('s', 3), (0, 'd'): ('s', 4),
    (1, '$'): ('acc', None),
    (2, 'c'): ('s', 3), (2, 'd'): ('s', 4),
    (3, 'c'): ('s', 3), (3, 'd'): ('s', 4),
    (4, 'c'): ('r', 3), (4, 'd'): ('r', 3), (4, '$'): ('r', 3),
    (5, '$'): ('r', 1),
    (6, 'c'): ('r', 2), (6, 'd'): ('r', 2), (6, '$'): ('r', 2),
}
GOTO = {(0, 'S'): 1, (0, 'C'): 2, (2, 'C'): 5, (3, 'C'): 6}
PRODS = {1: ('S', 2, 'S -> CC'), 2: ('C', 2, 'C -> cC'), 3: ('C', 1, 'C -> d')}

def slr_parse(tokens):
    stack = [0]
    buf = list(tokens) + ['$']
    pos = 0
    while True:
        state = stack[-1]
        la = buf[pos]
        act = ACTION.get((state, la))
        if not act:
            raise SyntaxError(f"SLR(1) Syntax Error in state {state} on token '{la}'")
        kind, val = act
        if kind == 's':
            print(f"Stack: {stack} | Input: {''.join(buf[pos:]):<6} | Shift {val}")
            stack.extend([la, val])
            pos += 1
        elif kind == 'r':
            lhs, rhs_len, rule_str = PRODS[val]
            print(f"Stack: {stack} | Input: {''.join(buf[pos:]):<6} | Reduce {rule_str}")
            if rhs_len > 0:
                stack = stack[:-2 * rhs_len]
            top_state = stack[-1]
            stack.extend([lhs, GOTO[(top_state, lhs)]])
        elif kind == 'acc':
            print(f"Stack: {stack} | Input: $      | ACCEPT")
            return True

if __name__ == "__main__":
    print("=== Valid SLR(1) Trace: c d d $ ===")
    slr_parse(['c', 'd', 'd'])
    print("\n=== Invalid SLR(1) Trace: c c $ ===")
    try:
        slr_parse(['c', 'c'])
    except SyntaxError as e:
        print("Detected:", e)
