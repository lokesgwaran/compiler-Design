"""Task 6: Mini-Compiler Prototype (Optimizer & TAC Interpreter)."""

def constant_fold_and_cse(tac):
    env_const = {}
    expr_table = {}
    optimized = []
    for op, a1, a2, res in tac:
        v1 = env_const.get(a1, a1)
        v2 = env_const.get(a2, a2)
        if op in ("+", "-", "*", "/") and isinstance(v1, (int, float)) and isinstance(v2, (int, float)):
            val = eval(f"{v1}{op}{v2}")
            env_const[res] = val
            optimized.append(("=", val, "-", res))
        elif op == "=" and isinstance(v1, (int, float)):
            env_const[res] = v1
            optimized.append(("=", v1, "-", res))
        else:
            key = (op, v1, v2)
            if op in ("+", "-", "*", "/") and key in expr_table:
                optimized.append(("=", expr_table[key], "-", res))
            else:
                if op in ("+", "-", "*", "/"):
                    expr_table[key] = res
                optimized.append((op, v1, v2, res))
    return optimized

if __name__ == "__main__":
    sample_tac = [
        ("*", 4, 8, "t1"),
        ("+", "t1", "x", "t2"),
        ("*", 4, 8, "t3"),
        ("+", "t3", "x", "t4"),
        ("+", "t2", "t4", "y"),
    ]
    opt = constant_fold_and_cse(sample_tac)
    print(f"Before Optimization ({len(sample_tac)} instrs):", sample_tac)
    print(f"After Optimization  ({len(opt)} instrs):", opt)
