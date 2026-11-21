"""Q3: Bottom-Up Shift-Reduce & Operator-Precedence Parser Trace."""

def shift_reduce_trace(tokens):
    stack = ["$"]
    buf = list(tokens) + ["$"]
    steps = []
    while True:
        # Check reductions
        if stack[-1] == "id":
            stack[-1] = "F"
            steps.append((list(stack), list(buf), "Reduce F -> id"))
        elif stack[-1] == "F":
            stack[-1] = "T"
            steps.append((list(stack), list(buf), "Reduce T -> F"))
        elif len(stack) >= 3 and stack[-3:] == ["T", "*", "F"]:
            stack[-3:] = ["T"]
            steps.append((list(stack), list(buf), "Reduce T -> T * F"))
        elif stack[-1] == "T" and buf[0] in ("+", "$"):
            stack[-1] = "E"
            steps.append((list(stack), list(buf), "Reduce E -> T"))
        elif len(stack) >= 3 and stack[-3:] == ["E", "+", "T"] and buf[0] == "$":
            stack[-3:] = ["E"]
            steps.append((list(stack), list(buf), "Reduce E -> E + T"))
        elif stack == ["$", "E"] and buf == ["$"]:
            steps.append((list(stack), list(buf), "ACCEPT"))
            break
        else:
            tok = buf.pop(0)
            stack.append(tok)
            steps.append((list(stack), list(buf), f"Shift {tok}"))
    return steps

if __name__ == "__main__":
    print("Shift-Reduce Parsing Trace for: id + id * id")
    for st, bf, act in shift_reduce_trace(["id", "+", "id", "*", "id"]):
        print(f"{''.join(st):<12} | {' '.join(bf):<15} | {act}")
