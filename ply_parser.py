import ply.yacc as yacc
from lx import tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE')
)

def p_e(p):
    """expression : expression PLUS expression"""
    print('expression', p[1], p[2], p[3])
    p[0] = p[1] + p[3]

def p_expression_minus(p):
    'expression : expression MINUS expression'
    print('expression', p[1], p[2], p[3])
    p[0] = p[1] - p[3]

def p_expression_term(p):
    'expression : term'
    print('expression term', p[1])
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES term'
    print('term times', p[1], p[2], p[3])
    p[0] = p[1] * p[3]

def p_term_divide(p): #Implementação da divisão
    'term : term DIVIDE term'
    print('term divide', p[1], p[2], p[3])
    p[0] = p[1] / p[3]

def p_term_number(p):
    'term : NUMBER'
    print('term', p[1])
    p[0] = p[1]

def p_paren(p):
    'term : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    print('erro')

parser = yacc.yacc()
