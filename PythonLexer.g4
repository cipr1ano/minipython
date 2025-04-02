lexer grammar PythonLexer;

// 1. Definições de Tokens - Palavras-chave (keywords)
DEF     : 'def';
CLASS   : 'class';
IF      : 'if';
ELSE    : 'else';
ELIF    : 'elif';
FOR     : 'for';
WHILE   : 'while';
IN      : 'in';
RETURN  : 'return';
PRINT   : 'print';
AND     : 'and';
OR      : 'or';
NOT     : 'not';
TRUE    : 'True';
FALSE   : 'False';
NONE    : 'None';

// 2. Definições de Tokens - Operadores
PLUS    : '+';
MINUS   : '-';
TIMES   : '*';
DIVIDE  : '/';
MOD     : '%';
AND_OP  : 'and';
OR_OP   : 'or';
NOT_OP  : 'not';
EQUAL   : '==';
ASSIGN  : '=';
LT      : '<';
GT      : '>';
LE      : '<=';
GE      : '>=';
NE      : '!=';

// 3. Definições de Tokens - Literais e identificadores
NUMBER  : [0-9]+;
STRING  : '"' ( ESC_SEQ | . )*? '"'
        | '\'' ( ESC_SEQ | . )*? '\'';
ID      : [a-zA-Z_][a-zA-Z_0-9]*;

// 4. Definições de Tokens - Outros caracteres
LPAREN  : '(';
RPAREN  : ')';
LBRACE  : '{';
RBRACE  : '}';
LBRACKET: '[';
RBRACKET: ']';
COMMA   : ',';
DOT     : '.';
COLON   : ':';
SEMI    : ';';
NEWLINE : '\r'? '\n' { skip(); };

// 5. Definições de Tokens - Espaços em branco (WS) e Comentários
WS      : [ \t]+ -> skip;  // Ignora espaços em branco
COMMENT : '#' ~[\r\n]* -> skip;  // Ignora comentários
LINE_JOIN : '\\\r'? '\n' -> skip;  // Para quebra de linha com continuação

// 6. Definições de Tokens - Letras e Dígitos (para outros casos)
DIGIT   : [0-9];
LETTER  : [a-zA-Z_];
