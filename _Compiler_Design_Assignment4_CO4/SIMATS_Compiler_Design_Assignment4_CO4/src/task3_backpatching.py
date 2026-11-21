"""Task 3: Boolean Expressions, Backpatching & Jump Consistency Checker."""

class BackpatchEngine:
    def __init__(self, start_addr=100):
        self.start_addr = start_addr
        self.code = []

    def nextquad(self):
        return self.start_addr + len(self.code)

    def emit(self, instr):
        idx = self.nextquad()
        self.code.append([idx, instr, None])
        return idx

    def makelist(self, i):
        return [i]

    def merge(self, p1, p2):
        return list(dict.fromkeys(p1 + p2))

    def backpatch(self, plist, target):
        for i in plist:
            self.code[i - self.start_addr][2] = target

    def check_consistency(self):
        max_addr = self.nextquad()
        errors = []
        for idx, instr, target in self.code:
            if "goto" in instr:
                if target is None:
                    errors.append(f"ERR_UNRESOLVED_JUMP at Quad {idx}: target is None")
                elif not (self.start_addr <= target <= max_addr):
                    errors.append(f"ERR_OUT_OF_RANGE at Quad {idx}: target {target} outside [{self.start_addr}..{max_addr}]")
        return errors

if __name__ == "__main__":
    bp = BackpatchEngine(100)
    m_start = bp.nextquad()
    q100 = bp.emit("if a < b goto")
    q101 = bp.emit("goto")
    m1 = bp.nextquad()
    q102 = bp.emit("if c == d goto")
    q103 = bp.emit("goto")
    m2 = bp.nextquad()
    q104 = bp.emit("if e > f goto")
    q105 = bp.emit("goto")
    m3 = bp.nextquad()
    bp.emit("t1 = x + 1")
    bp.emit("x = t1")
    q108 = bp.emit("goto")
    exit_q = bp.nextquad()

    bp.backpatch([q100], m1)
    bp.backpatch([q103], m2)
    bp.backpatch([q105], m3)
    bp.backpatch([q101, q102, q104], exit_q)
    bp.backpatch([q108], m_start)

    for idx, instr, tgt in bp.code:
        print(f"{idx}: {instr} {tgt if tgt is not None else ''}")
    print("Consistency Check:", bp.check_consistency())
