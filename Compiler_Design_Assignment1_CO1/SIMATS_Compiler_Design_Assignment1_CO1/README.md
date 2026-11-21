# SIMATS Engineering – Compiler Design (Unit I: Compiler Structure & Lexical Analysis)

**Assignment – 1 (CO1)**  
**Student Name:** B. Lokeshwaran  
**Register Number:** 192424305  
**Department / Semester:** CSE – Semester V (2026–2027)  

## Repository Structure

```text
SIMATS_Compiler_Design_Assignment1_CO1/
├── README.md
├── docs/
│   └── SIMATS_Compiler_Design_Assignment1_CO1.pdf
├── figures/
│   ├── fig1_1_language_processing_system.png
│   ├── fig2_1_threatrule_ast.png
│   ├── fig7_1_relop_dfa.png
│   └── fig10_1_scanner_benchmark.png
├── outputs/
│   └── scanner_verification_output.txt
├── src/
│   ├── threatrule.l
│   ├── threatrule_v2.l
│   └── threatrule_compiler_sim.py
└── tests/
    └── sample_test.tr
```

## Tasks Covered
- **Task 1 – Language Processors:** Compiler vs. Interpreter vs. Assembler vs. Hybrid JIT/eBPF comparison, Preprocessor/Linker/Loader roles, and system block diagram.
- **Task 2 – Phases of a Compiler:** Complete 6-phase compilation trace (`Lexical -> Syntax AST -> Semantic -> Unoptimized TAC -> Short-Circuit Optimization -> Target eBPF Assembly`) for `RULE ssh_attack ...`.
- **Task 3 – Grouping of Phases:** Front End vs. Back End ($1 + N$ federated SOC scalability) and 3-pass compiler architecture.
- **Task 4 – Compiler Construction Tools:** LEX/Flex, YACC/Bison, SDT engines, LLVM TableGen, and data-flow analyzers.
- **Task 5 & 6 – Lexical Analysis & Token Specification:** Sentinel double buffering, formal regular definitions (`OCTET`, `IPV4`, `PORT`, `RELOP`), and keyword vs. identifier disambiguation.
- **Task 7 & 8 – DFA Recognition & LEX Implementation:** Relational operator DFA with lookahead retraction and complete `threatrule.l` C scanner.
- **Task 9, 10 & 11 – Boundary Testing & Benchmarking:** Verification across edge IPv4/port values and throughput benchmarks up to 100,000 rules (~373,720 rules/sec).
- **Task 12 – Day-4 Design Challenge (v2.0):** Adapted `threatrule_v2.l` supporting URLs, CVE IDs, MD5/SHA-1/SHA-256 hashes, and continuous non-aborting error logging.
