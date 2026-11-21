# SIMATS Engineering – Compiler Design (Unit II: Syntax Analysis & Parsing)

**Assignment – 2 (CO2)**  
**Student Name:** B. Lokeshwaran  
**Register Number:** 192424305  

## Repository Structure

```text
SIMATS_Compiler_Design_Assignment2_CO2/
├── README.md
├── docs/
│   └── Compiler_Design_Assignment2_CO2.pdf
├── figures/
│   ├── fig1_1_irrigation_parse_tree.png
│   ├── fig1_2_dangling_else_ambiguity.png
│   ├── fig4_1_lr0_dfa.png
│   └── fig7_1_hybrid_parser_arch.png
├── outputs/
│   ├── q1_q2_ll1_recursive_descent_output.txt
│   ├── q3_shift_reduce_and_op_prec_output.txt
│   ├── q4_slr1_parser_output.txt
│   ├── q5_panic_mode_recovery_output.txt
│   └── q7_hybrid_parser_benchmark_output.txt
└── src/
    ├── q1_q2_ll1_recursive_descent.py
    ├── q3_shift_reduce_and_op_prec.py
    ├── q4_slr1_parser.py
    ├── q5_panic_mode_recovery.py
    └── q7_hybrid_parser_benchmark.py
```

## Questions Covered
- **Q1. Grammar Design & Ambiguity:** Smart-irrigation CFG, leftmost/rightmost derivations, parse trees, dangling-else disambiguation, and AST justification.
- **Q2. Top-Down Parsing:** Left recursion elimination, left factoring, FIRST/FOLLOW sets, recursive-descent parser, and $LL(1)$ predictive parsing table.
- **Q3. Bottom-Up Parsing:** Shift-reduce parsing trace (`id + id * id`), handle pruning, Shift/Reduce & Reduce/Reduce conflicts, and operator-precedence parsing.
- **Q4. LR Parsing & SLR Parser:** Canonical $LR(0)$ item collection, closure/goto DFA, SLR(1) ACTION/GOTO tables, and stack-based parsing trace (`c d d $`).
- **Q5. Error Handling & Recovery:** Viable-prefix error detection, panic-mode synchronizing sets, phrase-level recovery, and YACC error productions.
- **Q6. YACC Parser Generator:** Complete `.y` specification with `%union`, `%token`, `%type`, precedence directives (`%left`, `%right`, `%nonassoc`, `%prec`), and AST construction.
- **Q7. Design Challenge:** Hybrid Iterative $LL(1)$ + Operator-Precedence (Shunting-Yard) parser reducing parsing steps by 51.9% and bounding call-stack depth to $O(1)$.
