import ply.yacc as yacc
from lex import tokens,literals
import sys

def p_1(p): 
    r"dic : es"
    p.parser.out = p[1]

def p_2(p): 
    r"es : es LINHA_B e"
    p[1].append(p[3])
    p[0] = p[1]

def p_3(p): 
    r"es : e"
    p[0] = [p[1]]

def p_4(p): 
    r"e : items"
    p[0] = p[1]

def p_5(p): 
    r"items : items item"
    p[1].update(p[2])
    p[0] = p[1]

def p_6(p): 
    r"items : item"
    p[0] = p[1]

def p_7(p): 
    r"item : at_conc"
    p[0] = p[1] 

def p_8(p): 
    r"item : lings"
    p[0] = {"traducoes" : p[1]}

def p_10(p):
    r"lings : lings ling"
    p[1].update(p[2])
    p[0] = p[1]

def p_11(p):
    r"lings : ling"
    p[0] = p[1]

def p_12(p): 
    r"ling : ID_LING DOIS_PONTOS ts"
    p[0] = {f"{p[1]}": p[3]}

def p_13(p): 
    r"at_conc : ID2 DOIS_PONTOS VAL"
    p[0] = {f"{p[1][2:]}":  p[3]}

def p_14(p): 
    r"ts : ts t"
    p[0] = p[1].update(p[3])

def p_15(p): 
    r"ts : t" 
    p[0] = p[1]

def p_16(p): 
    r"t : PONTO VAL at_ts"
    if(p[3] == {}):            
        p[0] = (p[2],)
    else:
        p[0] = (p[2], p[3])

def p_17(p): 
    r"at_ts : at_ts at_t"
    p[1].update(p[2])
    p[0] = p[1]

def p_18(p): 
    r"at_ts : "
    p[0] = {}

def p_19(p): 
    r"at_t : ID DOIS_PONTOS VAL"
    p[0] = {f"{p[1][2:]}": p[3]}


# Syntatic Error handling rule
def p_error(p):
    print('Syntax error: ', p)


# Build the parser
parser = yacc.yacc(debug=True)

parser.out = []
parser.parse(open("exemplo.txt").read())


html = ""
with open("saida.html", "w") as f:
    for elem in parser.out:
        for k, v in elem.items():
            if k == "traducoes":
                for trad in v:
                    if len(v[trad]) > 1:
                        html += f"<h3>- {trad.upper()}</h3>\n"
                        html += f"<i>{v[trad][0]}</i><ul>\n"
                        for i in v[trad][1]:
                            html += f"<li><u>{i}</u> : "
                            for j in v[trad][1][i]:
                                html += f"{j}"
                            html += "</li>\n"
                        html += "</ul>\n"
                    else:
                        html += f"<h3>- {trad.upper()}</h3>\n<i>{v[trad][0]}</i>"
            else:
                html += f"<h2>{k.upper()}</h2>\n{v}"

        html += "<h1><hr></h1>\n"

    f.write(html)

