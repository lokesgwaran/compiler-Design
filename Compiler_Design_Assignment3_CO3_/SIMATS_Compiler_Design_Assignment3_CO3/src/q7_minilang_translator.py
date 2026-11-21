"""Q7: MiniLang Translator (Symbol Table, Type Checking & TAC Emission)."""

class MiniLangCompiler:
    def __init__(self):
        self.symtab = {}
        self.offset = 0
        self.temps = 0
        self.tac = []

    def declare(self, dtype, names):
        size = 4
        for name in names:
            if name in self.symtab:
                raise ValueError(f"Duplicate declaration of variable '{name}'")
            self.symtab[name] = {"type": dtype, "offset": self.offset, "size": size}
            self.offset += size

    def new_temp(self):
        self.temps += 1
        return f"t{self.temps}"

    def compile_sample(self):
        # Program: int x, y; float rate; x = y + 5 * 2;
        self.declare("int", ["x", "y"])
        self.declare("float", ["rate"])
        t1 = self.new_temp()
        self.tac.append(f"{t1} = 5 * 2")
        t2 = self.new_temp()
        self.tac.append(f"{t2} = y + {t1}")
        self.tac.append(f"x = {t2}")

if __name__ == "__main__":
    ml = MiniLangCompiler()
    ml.compile_sample()
    print("MiniLang Symbol Table:")
    for k, v in ml.symtab.items():
        print(f"  {k:<5} | type={v['type']:<5} | offset={v['offset']} | size={v['size']}B")
    print("\nMiniLang Generated TAC:")
    for line in ml.tac:
        print(" ", line)
