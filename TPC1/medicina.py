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
import json
texto = open('medicina.xml', 'r').read()

def remove_header_footer(texto):
    texto = re.sub(r'<text.* font="1">ocabulario.*</text>', r'###', texto)
    texto = re.sub(r'.*\n###\n.*\n', r'', texto)
    texto = re.sub(r'<page.*\n|</page>\n', r'', texto)
    
    return texto

texto = remove_header_footer(texto)

def marcaE(texto):
    texto = re.sub(r'<text.* font="3"><b>\s*(\d+\s+.*)</b></text>', r'###C \1', texto)
    texto = re.sub(r'<text.* font="8"><b>\s*(.*)\s*</b></text>', r'###R \1', texto)
    texto = re.sub(r'<text.* font="3"><b>\s*(\S.*)</b></text>', r'###R \1', texto)
    texto = re.sub(r'<text.* font="11"><b>\s*(\S.*)</b></text>', r'###R \1', texto)
    return texto

texto = marcaE(texto)

def limpeza(texto):
    texto = re.sub(r'<text.* font="4">.*</text>', r'', texto)
    texto = re.sub(r'<text.* font="3">.*</text>', r'', texto)
    texto = re.sub(r'<text.* font="\d*">\s*</text>\n', r'', texto)
    texto = re.sub(r'<text.* font="\d*"><b>\s*</b></text>\n', r'', texto)
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
    texto = re.sub(r'<fontspec.*\n', r'', texto)
    return texto

texto = limpaFontSpec(texto)

def marcaNota(texto):
    texto = re.sub(r'<text.* font="9">(.*)</text>', r'...\1', texto)
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
    texto = re.sub(r'</pdf2xml>\s*', r'', texto)
    return texto

texto = ultimoCaso(texto)

def troca_C_para_R(texto):
    texto1 = ""
    
    texto = re.sub(r'###C (\d+)\s*\n(.*)', r'###C \1 \2', texto)

    while texto != texto1:
        texto1 = texto
        texto = re.sub(r'###C (.*)\s*###R (.*)', r'###C \1\2', texto)
        if texto == texto1:
            texto = re.sub(r'###C (\d+)\s*\n(.*)', r'###C \1 \2', texto)
    

    texto = re.sub(r'###C (.*)\n([^&@]*\n)###R', r'###C \1\2', texto)
    texto = re.sub(r'###C (.*)\n[^&]([fm])',r'###C \1 \2', texto)

    texto = re.sub(r'###C (.*)\n([^&]*)?\n@', r'###C \1\n& \2\n@', texto)
    #texto = re.sub(r'###C \d+\s*\n', r'###C \1\2', texto)
    return texto

texto = troca_C_para_R(texto)

def generoDic(lista):
    aux = [x.strip() for x in lista]
    lista = []
    for elem in aux:
        if len(elem) != 0:
            lista.append(elem)

    return lista

def trataLinguas(lista):
    aux = [x.strip() for x in lista]
    lista = [[],{}] # lista[0] = SIN e VAR, lista[1] = resto
    for elem in aux:
        if len(elem) != 0:
            if elem[:3] == 'SIN' or elem[:3] == 'VAR':
                lista[0].append(elem)
            elif elem[2] == '\n':
                elem = elem.split('\n')
                leng = elem[0]
                resto = "".join(elem[1:])

                lista[1][leng] = [retiraEspacos(elem) for elem in resto.split(';')]  
            lista.append(elem)

    return lista

def retiraEspacos(texto):
    texto = re.sub(r' {2,}',r' ',texto)
    return texto

# dicionario
lista_texto = texto.split('###')[1:]

dic = {"R": {}, "C": {}}

for entrada in lista_texto:
    if entrada[0] == 'R':
        entrada = entrada.split('\n')
        aux = "".join(entrada[1:])
        aux = re.sub(r"Vid.- (.*)",r"\1",aux)
        dic['R'][entrada[0][2:].strip()] = re.sub(r" {2,}",r" ",aux)
    else:
        nota = entrada.split('...')
        linguas = nota[0].split('@')
        if len(nota) == 1:
            nota = ""
        else:
            nota = nota[1].split("Nota.-")[1].strip()
        areas = [elem.strip() for elem in linguas[0].split('&')[1:]]
        titulo = linguas[0].split('&')[0]
        linguas = trataLinguas(linguas[1:])
        info = linguas[0]
        numero = titulo.split(' ')[1]
        nome = "".join(titulo.split(' ')[2:-1])
        genero = generoDic("".join(titulo.split(' ')[-1]))

        nome = retiraEspacos(nome)
        genero = [retiraEspacos(elem) for elem in genero]
        areas = [retiraEspacos(elem) for elem in areas]
    
        dic['C'][numero] = {'nome': nome, 'info': info,'genero' : genero ,'areas': areas, 'linguas': linguas[1], 'nota': nota}


print("R: "+str(len(dic['R'])),"C:"+ str(len(dic['C'])))

file = open('medicina.txt', 'w')

file.write(texto)

file2 = open('medicina.json', 'w',encoding='utf8')
json.dump(dic, file2,ensure_ascii=False)