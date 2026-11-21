# SIMATS Engineering – Compiler Design (Unit 3: Syntax-Directed Translation)

**Assignment – 3 (CO3)**  
**Student Name:** B. Lokeshwaran  
**Register Number:** 192424305  

## Repository Structure

```text
SIMATS_Compiler_Design_Assignment3_CO3/
├── README.md
├── docs/
│   └── Compiler_Design_Assignment3_CO3.pdf
├── figures/
│   ├── fig1_1_annotated_parse_tree.png
│   ├── fig2_1_inherited_declaration.png
│   ├── fig3_1_dependency_graph.png
│   ├── fig5_1_ast_assignment.png
│   └── fig7_1_minilang_ast.png
├── outputs/
│   ├── q1_s_attributed_eval_output.txt
│   ├── q2_inherited_declarations_output.txt
│   ├── q3_dependency_graph_output.txt
│   ├── q4_infix_to_postfix_sdt_output.txt
│   ├── q5_q6_ast_and_tac_output.txt
│   └── q7_minilang_translator_output.txt
└── src/
    ├── q1_s_attributed_eval.py
    ├── q2_inherited_declarations.py
    ├── q3_dependency_graph.py
    ├── q4_infix_to_postfix_sdt.py
    ├── q5_q6_ast_and_tac.py
    └── q7_minilang_translator.py
```

## Questions Covered
- **Q1. Synthesized Attributes:** SDD definition, arithmetic rules, annotated parse tree (`3 * (4 + 5) - 6 / 2 = 24`), post-order evaluation, and parse tree height (`5`).
- **Q2. Inherited Attributes:** Variable declaration SDD (`float a, b, c`), `T.type` and `L.in` propagation, and duplicate/undeclared identifier detection.
- **Q3. Dependency Graphs:** Dependency graph construction (`2 + 3 * 4 = 14`), topological sorting, S-attributed vs. L-attributed definitions, and cycle detection.
- **Q4. Syntax-Directed Translation Schemes (SDT):** Infix-to-postfix translation (`3 4 5 + * 6 2 / -`), semantic action placement, bottom-up LR reduction actions, and on-the-fly translation.
- **Q5. Parse Tree & Abstract Syntax Tree (AST):** `mkNode()` / `mkLeaf()` AST construction (`a = b + c * d`) and structural comparison.
- **Q6. Advanced Attribute Evaluation:** Marker-nonterminal technique in LR parsing, Three-Address Code (`x = a + b * c - d`), `newTemp()`, and inherited control-flow labels.
- **Q7. MiniLang Translator Design:** Complete MiniLang grammar, static type checking, symbol table layout, annotated AST (`int x, y; x = y + 5 * 2;`), TAC generation, and $O(N)$ complexity analysis.
