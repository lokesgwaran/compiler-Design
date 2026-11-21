/* Task 12C: Adapted ThreatRule v2.0 LEX Specification with IOCs & Continuous Error Recovery */
%option noyywrap
%option yylineno

HEX         [0-9a-fA-F]
HASH_MD5    {HEX}{32}
HASH_SHA1   {HEX}{40}
HASH_SHA256 {HEX}{64}
CVE_ID      CVE-[0-9]{4}-[0-9]{4,7}
URL_IOC     https?:\/\/[a-zA-Z0-9._~:/?#\[\]@!\$&'()*+,;=%-]+

%%
{URL_IOC}       { return 301; /* TOK_URL: Prioritized above '//' comments */ }
"//".*          { /* Strip single-line comment */ }
{CVE_ID}        { return 302; /* TOK_CVE: Prioritized above generic ID */ }
{HASH_SHA256}   { return 303; /* TOK_SHA256 */ }
{HASH_SHA1}     { return 304; /* TOK_SHA1 */ }
{HASH_MD5}      { return 305; /* TOK_MD5 */ }
[^ \t\r\n;()]+ { fprintf(stderr, "[Line %d] Malformed IOC/token: %s\n", yylineno, yytext); }
%%
