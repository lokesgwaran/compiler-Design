# SIMATS Engineering – Compiler Design (Unit IV: Intermediate Code Generation)

**Assignment 4 – Part II – CO4:** *Compiler Engineering: Implement, Test, Debug & Optimise Intermediate Code Generators*

## Repository Structure

```text
SIMATS_Compiler_Design_Assignment4_CO4/
├── README.md
├── docs/
│   └── SIMATS_Compiler_Design_Assignment_4_Part_II_CO4.docx
├── figures/
│   ├── fig1_storage_alignment.png
│   ├── fig2_dag_comparison.png
│   ├── fig3_boolean_comparison.png
│   ├── fig4_switch_strategies.png
│   ├── fig5_activation_record.png
│   └── fig6_optimizer_benchmarks.png
├── outputs/
│   ├── task1_symbol_table_output.txt
│   ├── task2_tac_generator_output.txt
│   ├── task3_backpatching_output.txt
│   ├── task4_switch_translator_output.txt
│   ├── task5_procedure_calls_output.txt
│   └── task6_mini_compiler_output.txt
└── src/
    ├── task1_symbol_table.py
    ├── task2_tac_generator.py
    ├── task3_backpatching.py
    ├── task4_switch_translator.py
    ├── task5_procedure_calls.py
    └── task6_mini_compiler.py
```

## Tasks Covered
1. **Task 1 – Symbol Table & Declaration Processor:** Supports primitive types, pointers, multidimensional arrays, nested records, L-attributed inheritance, alignment rules (`packed`, `4-byte`, `8-byte`), and boundary error checks.
2. **Task 2 – Three-Address Code (TAC) Generation:** Generates Quadruples, Triples, and Indirect Triples, DAG value-numbering optimization, and array bounds checking.
3. **Task 3 – Boolean Expressions & Backpatching:** Implements `truelist`, `falselist`, and `nextlist` backpatching for short-circuit Boolean logic and control-flow constructs plus a jump consistency checker.
4. **Task 4 – Switch Statement Translation:** Compares Sequential Testing, Binary Search Trees, and Jump Tables across dense and sparse datasets.
5. **Task 5 – Procedure Calls & Calling Sequences:** Handles nested/recursive calls, argument evaluation orders (`LTR` vs `RTL`), activation record stack frame offsets, varargs, and multi-return extensions.
6. **Task 6 – Mini-Compiler Integration Prototype:** Modular compiler pipeline with Constant Folding, CSE, and Dead Code Elimination benchmarks.
