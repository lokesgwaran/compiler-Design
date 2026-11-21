"""Task 2: Three-Address Code Generator (Quadruples, Triples, Indirect Triples + DAG)."""

class TACGenerator:
    def __init__(self):
        self.quads = []
        self.temp_count = 0
        self.dag = {}

    def new_temp(self):
        self.temp_count += 1
        return f"t{self.temp_count}"

    def emit(self, op, arg1, arg2="-", result=None, use_dag=False):
        if use_dag and op not in ("=", "=[]", "=*"):
            key = (op, arg1, arg2)
            if key in self.dag:
                return self.dag[key]
        if result is None:
            result = self.new_temp()
        self.quads.append((op, arg1, arg2, result))
        if use_dag and op not in ("=", "=[]", "=*"):
            self.dag[(op, arg1, arg2)] = result
        return result

    def display_all_forms(self):
        print("Idx | Quadruple                 | Triple               | Indirect")
        for idx, (op, a1, a2, res) in enumerate(self.quads):
            q_str = f"({op}, {a1}, {a2}, {res})"
            t_str = f"({op}, {a1}, {a2})"
            print(f"{idx:<3} | {q_str:<25} | {t_str:<20} | Ptr[{idx}] -> ({idx})")

if __name__ == "__main__":
    gen = TACGenerator()
    t1 = gen.emit("uminus", "a")
    t2 = gen.emit("*", "b", "c")
    t3 = gen.emit("inttofloat", t2)
    t4 = gen.emit("+", t1, t3)
    t5 = gen.emit("*", "i", "16")
    t6 = gen.emit("+", t5, "4")
    t7 = gen.emit("=[]", "A", t6)
    t8 = gen.emit("inttofloat", t7)
    t9 = gen.emit("+", t4, t8)
    t10 = gen.emit("=*", "p")
    t11 = gen.emit("inttofloat", t10)
    gen.emit("+", t9, t11, result="res")
    gen.display_all_forms()
