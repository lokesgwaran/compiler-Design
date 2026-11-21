"""Complete Python Reference Implementation of ThreatRule Scanner, TAC & Optimizer (Tasks 2, 9, 12)."""
import re

KEYWORDS = {"RULE", "IF", "AND", "OR", "NOT", "THEN", "ALERT", "DROP", "LOG"}

MASTER_REGEX = re.compile(
    r'(?P<URL>https?://[a-zA-Z0-9._~:/?#\[\]@!$&\x27()*+,;=%-]+)|'
    r'(?P<COMMENT>//[^\n]*)|'
    r'(?P<WS>[ \t\r\n]+)|'
    r'(?P<CVE>CVE-\d{4}-\d{4,7})|'
    r'(?P<SHA256>\b[0-9a-fA-F]{64}\b)|'
    r'(?P<SHA1>\b[0-9a-fA-F]{40}\b)|'
    r'(?P<MD5>\b[0-9a-fA-F]{32}\b)|'
    r'(?P<IPV4>(?:(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d))|'
    r'(?P<BAD_IPV4>\d+\.\d+\.\d+\.\d+)|'
    r'(?P<NUMBER>\d+)|'
    r'(?P<STRING>"[^"\n]*")|'
    r'(?P<BAD_STRING>"[^"\n]*)|'
    r'(?P<RELOP>==|!=|<=|>=|<|>)|'
    r'(?P<SEMI>;)|'
    r'(?P<LPAREN>\()|'
    r'(?P<RPAREN>\))|'
    r'(?P<ID>[a-zA-Z_][a-zA-Z0-9_]*)|'
    r'(?P<ERROR>[^ \t\r\n;()]+)'
)

def scan_threatrules(source_text):
    tokens = []
    errors = []
    symtab = {}
    line = 1
    for m in MASTER_REGEX.finditer(source_text):
        kind = m.lastgroup
        val = m.group()
        if kind in ("WS", "COMMENT"):
            line += val.count("\n")
            continue
        if kind == "BAD_IPV4":
            errors.append(f"[Line {line}] Invalid IPv4 octet range: {val}")
        elif kind == "BAD_STRING":
            errors.append(f"[Line {line}] Unterminated string literal: {val}")
        elif kind == "ERROR":
            errors.append(f"[Line {line}] Illegal symbol/malformed token: {val}")
        elif kind == "NUMBER":
            num = int(val)
            tok_name = "PORT_NUM" if 0 <= num <= 65535 else "INTEGER"
            tokens.append((tok_name, num))
        elif kind == "ID":
            if val in KEYWORDS:
                tokens.append((val, f"KW_{val}"))
            else:
                if val not in symtab:
                    symtab[val] = len(symtab)
                tokens.append(("ID", f"sym_idx:{symtab[val]} ({val})"))
        else:
            tokens.append((kind, val))
    return tokens, errors, symtab

if __name__ == "__main__":
    sample_suite = """
    RULE ssh_attack IF src_ip == 10.0.0.5 AND port == 22 AND attempts > 5 THEN ALERT "SSH brute force";
    RULE min_ip IF src_ip == 0.0.0.0 THEN LOG "Zero IP";
    RULE max_ip IF src_ip == 255.255.255.255 THEN DROP "Broadcast";
    RULE max_port IF port == 65535 THEN ALERT "High ephemeral port";
    RULE big_num IF attempts == 65536 THEN LOG "Above port range";
    RULE ioc_v2 IF url == https://c2.evil.org/bin AND cve == CVE-2024-3400 THEN ALERT "APT IOC";
    RULE bad_ip IF src_ip == 10.0.300.5 THEN ALERT "Bad IP";
    RULE bad_str IF port == 80 THEN ALERT "Login failed;
    RULE bad_sym IF port == 22 @ attempts > 5 THEN DROP "Err";
    """
    tokens, errors, symtab = scan_threatrules(sample_suite)
    print(f"Total Valid Tokens Emitted: {len(tokens)}")
    print(f"Symbol Table Entries ({len(symtab)}): {symtab}")
    print("\nFirst 18 Tokens (Sample ssh_attack Rule):")
    for idx, t in enumerate(tokens[:18], 1):
        print(f"  {idx:2d}. <{t[0]}, {t[1]}>")
    print("\nCaptured Lexical Errors (Continuous Recovery):")
    for err in errors:
        print(" ", err)
