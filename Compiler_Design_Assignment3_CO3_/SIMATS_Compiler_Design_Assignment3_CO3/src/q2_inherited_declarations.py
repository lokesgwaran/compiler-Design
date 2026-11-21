"""Q2: Inherited Attributes (L.in = T.type) & Symbol Table Declaration Checking."""

class SymbolTable:
    def __init__(self):
        self.symbols = {}

    def add_type(self, name, dtype):
        if name in self.symbols:
            raise ValueError(f"Error: Redeclaration of variable '{name}' in the same scope")
        self.symbols[name] = dtype

    def lookup(self, name):
        if name not in self.symbols:
            raise NameError(f"Error: Identifier '{name}' used before declaration")
        return self.symbols[name]

if __name__ == "__main__":
    st = SymbolTable()
    t_type = "float"
    for var in ["a", "b", "c"]:
        st.add_type(var, t_type)
    print("Symbol Table after 'float a, b, c;':", st.symbols)
    try:
        st.add_type("b", "int")
    except ValueError as e:
        print("Duplicate Check ->", e)
    try:
        st.lookup("z")
    except NameError as e:
        print("Undeclared Check ->", e)
