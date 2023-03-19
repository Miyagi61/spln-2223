import ply.lex as lex
import sys

literals = []

tokens = ( 'ID' , 'ID2', 'ID_LING' , 'VAL', 'LINHA_B' ,
           'PONTO' , 'DOIS_PONTOS' )

def t_BARRA_N(t): 
    r"\n"
    t.lexer.lineno += len(t.value)

def t_ID_LING(t): 
    r"'\w{2}'"
    t.value = str(t.value)[1:-1]
    return t

def t_ID(t): 
    r'\+\s\w+'
    t.value = str(t.value)
    return t

def t_ID2(t): 
    r'-\s\w+'
    t.value = str(t.value)
    return t

def t_PONTO(t):
    r'\.'
    t.value = str(t.value)
    return t

def t_DOIS_PONTOS(t):
    r':'
    t.value = str(t.value)
    return t

def t_LINHA_B(t): 
    r'\n*-+\n*'
    return t

def t_VAL(t): 
    r'[^:\n@.]+'
    t.value = str(t.value).strip()
    return t

t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()
 