import ply.yacc as yacc
from lex import tokens,literals
import sys

def p_1(p): 
    r"dic : es"
    p[0] = p[1]
    print(1)
    print(p[0])

def p_2(p): 
    r"es : es LINHA_B e"
    p[0] = p[1].update(p[3])
    print(2)

def p_3(p): 
    r"es : e"
    p[0] = p[1]
    print(3)

def p_4(p): 
    r"e : items"
    p[0] = p[1]
    print(4)

def p_5(p): 
    r"items : items '\n' item"
    p[0] = p[1].update(p[3])
    print(5)

def p_6(p): 
    r"items : item"
    p[0] = p[1]
    print(6)

def p_7(p): 
    r"item : ling"
    p[0] = p[1]
    print(7)

def p_8(p): 
    r"item : at_conc"
    p[0] = p[1] 
    print(8)

def p_9(p): 
    r"ling : ID_LING DOIS_PONTOS ts"
    p[0] = {f"{p[1]}": p[3]}
    print(9)

def p_10(p): 
    r"at_conc : ID ':' VAL"
    p[0] = {f"{p[1]}":  p[3]}
    print(10)


def p_11(p): 
    r"ts : ts t"
    p[0] = p[1].update(p[3])
    print(11)

def p_12(p): 
    r"ts : PONTO t" 
    p[0] = p[2]
    print(12)

def p_13(p): 
    r"t : VAL at_ts"
    if(p[2] == {}):            
        p[0] = p[1]
    else:
        p[0] = {f"{p[1]}": p[2]}
    print(13)

def p_14(p): 
    r"at_ts : at_ts at_t"
    p[0] = p[1].update(p[2]) 
    print(14)

def p_15(p): 
    r"at_ts : "
    p[0] = {}
    print(15)

def p_16(p): 
    r"at_t : PLUS ID DOIS_PONTOS VAL"
    p[0] = {f"{p[2]}": p[4]}
    print(16)


# Syntatic Error handling rule
def p_error(p):
    print('Syntax error: ', p)


# Build the parser
parser = yacc.yacc(debug=True)


txt = """'ga' : 
. a"""

import logging

#log = logging.getLogger()
parser.parse(txt)