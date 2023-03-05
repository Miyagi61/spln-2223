import ply.lex as lex
import sys

literals = [':', '-', '+', '\n', r'@']

tokens = ( 'ID' , 'ID_LING' , 'VAL', 'LINHA_B')

def t_ID(t): 
    r'\w+'
    t.value = str(t.value)
    return t

def t_ID_LING(t): 
    r'\w{2}'
    t.value = str(t.value)
    return t

def t_VAL(t): 
    r'[^:\n]+'
    t.value = str(t.value)
    return t

def t_LINHA_B(t): 
    r'\n+'
    t.lexer.lineno += len(t.value)

t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
 