import ply.yacc as yacc
from lx import tokens

precedence = (
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE')
)

def p_e(p):
    """expression : expression PLUS expression"""
    p[0] = (p[1], p[3], "ADD")

def p_expression_minus(p):
    'expression : expression MINUS expression'
    p[0] = (p[1], p[3], "SUB")

def p_expression_term(p):
    'expression : term'
    p[0] = p[1]

def p_term_times(p):
    'term : term TIMES term'
    p[0] = (p[1], p[3], "MULT")

def p_term_divide(p): #Implementação da divisão
    'term : term DIVIDE term'
    p[0] = (p[1], p[3], "DIV")

def p_term_number(p):
    'term : NUMBER'
    p[0] = p[1]

def p_paren(p):
    'term : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    print('erro')

parser = yacc.yacc()
