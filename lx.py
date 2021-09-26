import ply.lex as lex

tokens = (
    'NUMBER',
    'PLUS',
    'MINUS',
    'TIMES',
    'DIVIDE',
    'LPAREN',
    'RPAREN',
    'TEXT', # * Inclua regras para identificadores
    'EQUALS', # * Inclua regras para atribuição e final de linha (;)
    'SEMICOLON' # * Inclua regras para atribuição e final de linha (;)
)

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_TEXT = r'\w+' # * Inclua regras para identificadores
t_EQUALS = r'=' # * Inclua regras para atribuição e final de linha (;)
t_SEMICOLON = r';' # * Inclua regras para atribuição e final de linha (;)


def t_NUMBER(t): # * Os tokens de números devem incluir números decimais
    r'\d+(\.\d+)?'
    t.value = float(t.value)
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
