%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_SYMBOLS 16384
typedef struct {
    char name[128];
    int first_line;
} SymbolEntry;

SymbolEntry sym_table[MAX_SYMBOLS];
int sym_count = 0;
int token_count = 0;
int error_count = 0;

typedef union {
    int ival;
    char *sval;
} YYSTYPE;
YYSTYPE yylval;

enum TokenType {
    TOK_RULE = 256, TOK_IF, TOK_AND, TOK_OR, TOK_NOT, TOK_THEN,
    TOK_ALERT, TOK_DROP, TOK_LOG, TOK_ID, TOK_IPV4, TOK_PORT,
    TOK_INT, TOK_STRING, TOK_RELOP, TOK_SEMI, TOK_LPAREN, TOK_RPAREN
};

int install_id(const char *lexeme, int line) {
    for (int i = 0; i < sym_count; i++) {
        if (strcmp(sym_table[i].name, lexeme) == 0) return i;
    }
    if (sym_count < MAX_SYMBOLS) {
        strncpy(sym_table[sym_count].name, lexeme, 127);
        sym_table[sym_count].name[127] = '\0';
        sym_table[sym_count].first_line = line;
        return sym_count++;
    }
    return -1;
}
%}

%option noyywrap
%option yylineno

DIGIT       [0-9]
LETTER      [a-zA-Z_]
ID          {LETTER}({LETTER}|{DIGIT})*
OCTET       (25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])
IPV4        {OCTET}\.{OCTET}\.{OCTET}\.{OCTET}
BAD_IPV4    {DIGIT}+\.{DIGIT}+\.{DIGIT}+\.{DIGIT}+
INTEGER     {DIGIT}+
STRING      \"[^"\n]*\"
BAD_STRING  \"[^"\n]*
RELOP       (==|!=|<=|>=|<|>)

%%
"//".*                          { /* Strip single-line comments */ }
"/*"([^*]|\*+[^*/])*\*+"/"    { /* Strip multi-line comments */ }
[ \t\r\n]+                   { /* Ignore whitespace */ }

"RULE"      { token_count++; return TOK_RULE; }
"IF"        { token_count++; return TOK_IF; }
"AND"       { token_count++; return TOK_AND; }
"OR"        { token_count++; return TOK_OR; }
"NOT"       { token_count++; return TOK_NOT; }
"THEN"      { token_count++; return TOK_THEN; }
"ALERT"     { token_count++; return TOK_ALERT; }
"DROP"      { token_count++; return TOK_DROP; }
"LOG"       { token_count++; return TOK_LOG; }

{IPV4}      { token_count++; yylval.sval = strdup(yytext); return TOK_IPV4; }
{BAD_IPV4}  { error_count++; fprintf(stderr, "[Line %d] LEXICAL ERROR: Invalid IPv4 '%s'\n", yylineno, yytext); }
{INTEGER}   {
                token_count++;
                long val = strtol(yytext, NULL, 10);
                yylval.ival = (int)val;
                return (val >= 0 && val <= 65535) ? TOK_PORT : TOK_INT;
            }
{STRING}    { token_count++; yylval.sval = strdup(yytext); return TOK_STRING; }
{BAD_STRING}{ error_count++; fprintf(stderr, "[Line %d] LEXICAL ERROR: Unterminated string '%s'\n", yylineno, yytext); }
{RELOP}     { token_count++; yylval.sval = strdup(yytext); return TOK_RELOP; }
";"         { token_count++; return TOK_SEMI; }
"("         { token_count++; return TOK_LPAREN; }
")"         { token_count++; return TOK_RPAREN; }
{ID}        { token_count++; yylval.ival = install_id(yytext, yylineno); return TOK_ID; }
.           { error_count++; fprintf(stderr, "[Line %d] LEXICAL ERROR: Illegal symbol '%s'\n", yylineno, yytext); }
%%

int main(int argc, char **argv) {
    if (argc > 1) yyin = fopen(argv[1], "r");
    while (yylex() != 0) {}
    printf("Scan Complete | Lines: %d | Tokens: %d | Errors: %d | Symbols: %d\n",
           yylineno, token_count, error_count, sym_count);
    return 0;
}
