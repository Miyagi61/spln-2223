# ZEP -> E*
# E -> EC
#    | ER
# EC -> num pals pos CORPO
# CORPO -> area LINGUAS
# LINGUAS -> pt pals
#          | en pals
#          | es pals
# ER -> pals VID
# VID -> Vid.- pals

import re

texto = open('medicina.xml', 'r').read()

def remove_header_footer(texto):
    texto = re.sub(r'<text.* font="1">ocabulario.*</text>', r'###', texto)
    texto = re.sub(r'.*\n###\n.*\n', r'___', texto)
    texto = re.sub(r'<page.*\n|</page>\n', r'', texto)
    
    return texto

texto = remove_header_footer(texto)

def marcaE(texto):
    texto = re.sub(r'<text.* font="3"><b>\s*(\d+.*)</b></text>', r'###C \1', texto)
    texto = re.sub(r'<text.* font="3"><b>\s*(\S.*)</b></text>', r'###R \1', texto)
  
    return texto

texto = marcaE(texto)

def marcaLinguas(texto):
    # @
    pass

# dicionario

def marcaEC(texto):
    pass

def marcaER(texto):
    pass


file = open('medicina2.txt', 'w')

file.write(texto)

