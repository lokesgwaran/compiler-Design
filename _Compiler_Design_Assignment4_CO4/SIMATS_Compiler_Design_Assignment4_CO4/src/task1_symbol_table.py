"""Task 1: Symbol Table & L-Attributed Declaration Processor."""
import math

class SymbolEntry:
    def __init__(self, name, dtype, width, offset, scope):
        self.name = name
        self.dtype = dtype
        self.width = width
        self.offset = offset
        self.scope = scope

class Env:
    def __init__(self, scope_name, level=0, prev=None):
        self.scope_name = scope_name
        self.level = level
        self.prev = prev
        self.table = {}
        self.offset = 0

    def align(self, rule):
        if rule == "4byte":
            self.offset = math.ceil(self.offset / 4) * 4
        elif rule == "8byte":
            self.offset = math.ceil(self.offset / 8) * 8

    def enter(self, name, dtype, width, rule="packed"):
        if name in self.table:
            raise ValueError(f"SemanticError: Duplicate declaration '{name}' in scope '{self.scope_name}'")
        self.align(rule)
        entry = SymbolEntry(name, dtype, width, self.offset, f"{self.scope_name} (level {self.level})")
        self.table[name] = entry
        self.offset += width
        return entry

def run_task1():
    decls = [
        ("count", "int", 4),
        ("ratio", "float", 8),
        ("flag", "boolean", 1),
        ("grade", "char", 1),
        ("ptr", "pointer(int)", 4),
        ("matrix", "array(3, array(4, int))", 48),
    ]
    for rule in ["packed", "4byte", "8byte"]:
        env = Env("global", 0)
        print(f"=== Alignment Rule: {rule} ===")
        for name, dtype, width in decls:
            e = env.enter(name, dtype, width, rule)
            print(f"{e.name:<10} | {e.dtype:<25} | Width: {e.width:<3} | Offset: {e.offset:<3} | {e.scope}")
        print(f"Total Storage Footprint: {env.offset} Bytes\n")

if __name__ == "__main__":
    run_task1()
