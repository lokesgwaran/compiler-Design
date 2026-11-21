"""Task 4: Case (Switch) Statement Translation Strategies."""

def translate_switch(cases, default_label="L_default"):
    seen = set()
    for val, _ in cases:
        if val in seen:
            raise ValueError(f"CompileError: Duplicate case label {val}")
        seen.add(val)

    if not cases:
        return {"strategy": "empty", "instructions": 1, "memory_bytes": 4}

    vals = sorted(v for v, _ in cases)
    span = vals[-1] - vals[0] + 1
    density = len(vals) / span

    seq_mem = len(vals) * 12
    bin_mem = len(vals) * 16 + 4
    jmp_mem = 40 + span * 4

    return {
        "cases": len(vals),
        "span": span,
        "density": round(density, 3),
        "sequential_bytes": seq_mem,
        "binary_search_bytes": bin_mem,
        "jump_table_bytes": jmp_mem,
        "recommended": "Jump Table" if density >= 0.5 else "Binary Search Tree"
    }

if __name__ == "__main__":
    print("3-Case:", translate_switch([(1, "L1"), (2, "L2"), (3, "L3")]))
    print("Dense 10-Case:", translate_switch([(i, f"L{i}") for i in range(1, 11)]))
    print("Sparse 5-Case:", translate_switch([(1, "L1"), (250, "L2"), (500, "L3"), (750, "L4"), (1001, "L5")]))
