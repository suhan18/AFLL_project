import ply.lex as lex
import ply.yacc as yacc

 
# Define tokens
tokens = (
    'FOR',
    'IN',
    'RANGE',
    'LPAREN',
    'RPAREN',
    'COLON',
    'COMMA',
    'NUMBER',
    'ID',
)

reserved = {
   'if' : 'IF',
   'then' : 'THEN',
   'else' : 'ELSE',
   'while' : 'WHILE',
   'for' : 'FOR',
   'in' : 'IN',
   'range' : 'RANGE',
}

# Define regular expressions for tokens
t_FOR = r'for'
t_IN = r'in'
t_RANGE = r'range'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COLON = r':'
t_COMMA = r','
t_NUMBER = r'\d+'
t_ignore = ' \t'


# Define a regular expression for numbers
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

# Define the newline token
def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Define the error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
 
precedence = (
    ('left', 'FOR','IN','RANGE'),
    ('left', 'ID'),
    ('left', 'COMMA'),
    ('left', 'COLON'),
)

 
def p_for_loop(p):
    '''for_loop : FOR ID IN RANGE LPAREN NUMBER COMMA NUMBER RPAREN COLON'''
    
    p[0] = ('for_loop', p[2], p[6], p[8], p[10])

# Define error handling
def p_error(p):
    if(p==None):
        print("Syntax error after )")
    else:
        print("Syntax error at '%s'" % p.value)

lexer = lex.lex()
parser = yacc.yacc()


code = '''\
for i in range(1,10)
'''

# Give the lexer some input
lexer.input(code)

# Tokenize
while True:
    tok = lexer.token()
    if not tok: 
        break      # No more input
    print(tok)

result = parser.parse(code)

if(result!=None):
        print(result)