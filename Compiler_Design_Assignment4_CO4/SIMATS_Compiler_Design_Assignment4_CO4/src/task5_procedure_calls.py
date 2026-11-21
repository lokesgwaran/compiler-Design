"""Task 5: Procedure Calls, Calling Sequences & Evaluation Order."""

def evaluate_call(func_name, args, order="LTR"):
    eval_seq = args if order == "LTR" else list(reversed(args))
    state = {"x": 5}
    evaluated = []
    for name, fn in eval_seq:
        val = fn(state)
        evaluated.append((name, val))
    if order == "RTL":
        evaluated.reverse()
    return [v for _, v in evaluated]

if __name__ == "__main__":
    def read_x(s): return s["x"]
    def inc_x(s):
        s["x"] += 1
        return s["x"]
    args = [("x", read_x), ("inc()", inc_x)]
    print("Left-to-Right pair(x, inc()):", evaluate_call("pair", args, "LTR"))
    print("Right-to-Left pair(x, inc()):", evaluate_call("pair", args, "RTL"))
