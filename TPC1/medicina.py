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
    texto = re.sub(r'.*\n###\n.*\n', r'', texto)
    texto = re.sub(r'<page.*\n|</page>\n', r'', texto)
    
    return texto

texto = remove_header_footer(texto)

def marcaE(texto):
    texto = re.sub(r'<text.* font="3"><b>\s*(\d+.*)</b></text>', r'###C \1', texto)
    texto = re.sub(r'<text.* font="8"><b>\s*(.*)\s*</b></text>', r'###R \1', texto)
    texto = re.sub(r'<text.* font="3"><b>\s*(\S.*)</b></text>', r'###R \1', texto)
    texto = re.sub(r'<text.* font="11"><b>\s*(\S.*)</b></text>', r'###R \1', texto)
    return texto

texto = marcaE(texto)

def limpeza(texto):
    texto = re.sub(r'<text.* font="4">.*</text>', r'', texto)
    texto = re.sub(r'<text.* font="3">.*</text>', r'', texto)
    texto = re.sub(r'<text.* font="\d*">\s*</text>', r'', texto)
    texto = re.sub(r'<text.* font="\d*"><b>\s*</b></text>', r'', texto)
    return texto

texto = limpeza(texto)

def marcaLinguas(texto):
    texto = re.sub(r'<text.* font="0">\s*(\S+)\s*</text>', r'@ \1', texto)
    texto = re.sub(r'@ ;', r';', texto)
    texto = re.sub(r'<text.* font="7"><i>(.*)</i></text>', r'\1', texto)
    return texto

texto = marcaLinguas(texto)

def marcaSIN_VAR(texto):
    texto = re.sub(r'<text.* font="5">\s*(SIN.*)</text>', r'@\1', texto)
    texto = re.sub(r'<text.* font="0">\s*(SIN.*)</text>', r'@\1', texto)
    texto = re.sub(r'<text.* font="5">\s*(VAR.*)</text>', r'@\1', texto)
    texto = re.sub(r'<text.* font="0">\s*(VAR.*)</text>', r'@\1', texto)
    return texto

texto = marcaSIN_VAR(texto)

def marcaArea(texto):
    texto = re.sub(r'<text.* font="6"><i>\s*(.*)\s*</i></text>', r'& \1', texto)
    return texto

texto = marcaArea(texto)

def marcaVid(texto):
    texto = re.sub(r'<text.* font="\d*">\s*(Vid\..*)</text>', r'\1', texto)
    return texto

texto = marcaVid(texto)

def limpaFontSpec(texto):
    texto = re.sub(r'<fontspec.*', r'', texto)
    return texto

texto = limpaFontSpec(texto)

def marcaNota(texto):
    texto = re.sub(r'<text.* font="9">(.*)</text>', r'.\1', texto)
    return texto

texto = marcaNota(texto)

def limpaParagrafo(texto):
    texto = re.sub(r'<text.* font="5">(.*)</text>', r'\1', texto)
    return texto

texto = limpaParagrafo(texto)

def font10(texto):
    texto = re.sub(r'<text.* font="10"><i><b>(.*)</b></i></text>', r'\1', texto)
    return texto

texto = font10(texto)

def numeracaoDesformatada(texto):
    texto = re.sub(r'<text.* font="\d+">\s*(\d+)\s*</text>\n###R(.*)', r'###C \1 \2', texto)
    return texto

texto = numeracaoDesformatada(texto)

def elementosQuimicos(texto):
    texto = re.sub(r'<text.* font="13"><b>\s*(\d+)\s*</b></text>', r'_\1', texto)
    texto = re.sub(r'<text.* font="15"><i>\s*(\d+)\s*</i></text>', r'_\1', texto)
    texto = re.sub(r'<text.* font="14">\s*(\d+)\s*</text>', r'_\1', texto)
    return texto

texto = elementosQuimicos(texto)

def ultimoCaso(texto):
    texto = re.sub(r'<text.* font="0">\s*(\S.*)</text>', r'\1', texto)
    texto = re.sub(r'###R\s*\n', r'', texto)
    texto = re.sub(r'</pdf2xml>', r'', texto)
    return texto

texto = ultimoCaso(texto)

# dicionario
lista_texto = texto.split('###')[1:]

dic = {"R": {}, "C": {}}

for entrada in lista_texto:
    if entrada[0] == 'R':
        entrada = entrada.split('\n')
        dic['R'][entrada[0][2:]] = entrada[1:]
    else:
        linguas = entrada.split('@')
        areas = linguas[0].split('&')[1:]
        titulo = linguas[0].split('&')[0]
        linguas = linguas[1:]
        numero = titulo.split(' ')[0]
        nome = titulo.split(' ')[1:-1]
        genero = titulo.split(' ')[-1]
        dic['C'][numero] = {'nome': nome,'genero' : genero,'areas': areas, 'linguas': linguas}

file = open('medicina.txt', 'w')

file.write(texto)

print(dic)