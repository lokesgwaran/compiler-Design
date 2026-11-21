"""Q5: Panic-Mode Error Recovery Simulation for Smart-Irrigation Rules."""

SYNC_COND = {"THEN", "ELSE", ";", ")"}

def panic_recover_irrigation(tokens):
    print("Input Tokens:", " ".join(tokens))
    i = 0
    if tokens[i] == "IF":
        i += 1
    # Parse Cond: expect id RelOp num
    if tokens[i] == "moisture" and tokens[i+1] == "<":
        i += 2
        if not tokens[i].isdigit():
            print(f"[Syntax Error] Expected numeric threshold after '<', found '{tokens[i]}'")
            while i < len(tokens) and tokens[i] not in SYNC_COND:
                print(f"  -> Panic-mode discarding token: '{tokens[i]}'")
                i += 1
            print(f"  -> Synchronized at token: '{tokens[i]}' (Popped Cond, resuming Action)")
    if tokens[i] == "THEN":
        i += 1
        print(f"Resumed parsing Action cleanly: {' '.join(tokens[i:])}")

if __name__ == "__main__":
    malformed = ["IF", "moisture", "<", "AND", "temp", ">", "25", "THEN", "irrigate(10);"]
    panic_recover_irrigation(malformed)
