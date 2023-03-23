#! /usr/bin/env python3
"""Module to tokenize books
"""

__version__ = '0.3'

import re
from .utils import *

list_poemas = []
abrev_list = []

def treat_page_break(procedure_dic,text):
    """If flagged or default removes page breaks"""
    regex_nl = r'([a-z.0-9,;\-–?!\(\)])(\n\n)+([a-zA-Z.0-9,;\-–?!\(\)])'
    return re.sub(regex_nl,r'\1\n\3',text)

def treat_punctuation(procedure_dic,text):
    """If flagged or default separates punctuation from words"""
    regex_punc = r'([.!,?;:' + r'\"\-\”\–\`()\[\]])?(\w+)([.!,?;:' + r'\"\-\”\–\`()\[\]])'
    return re.sub(regex_punc,r'\1 \2 \3',text)


def treat_chapters(procedure_dic,text):
    """If flagged or default tags chapters with the '#' delimeter\n
       Further subtitles or descriptions of the chapter will be delimeted between '[' and ']'
    """
    regex_cap = r'.*(CAPÍTULO +(\w+|\d+)).*\n((.+\n)*)'
    return re.sub(regex_cap,r'#\1\n[\3]\n',text)

def treat_paragraphs(procedure_dic,text):
    """If flagged or default separates paragraphs from simple sentences with the '/PAR/' delimiter"""
    regex_par = r'([.!?;])\n(([^.!?;]|[\u00C0-\u017F]))'
    return re.sub(regex_par,r'\1\n/PAR/ \2',text)

def treat_sentences_single_line(procedure_dic,text):
    """If flagged or default unifies sentences into a single line"""
    regex_sen = r'([^.!?])\n+([^.!?])'
    return re.sub(regex_sen,r'\1 \2',text)

def treat_sentences_per_line(procedure_dic,text,abrev_list):
    """If flagged or default seperates every sentence in differente lines"""
    regex_sen = r'([^.!?][.?!])(\s|[^.])'
    text = re.sub(regex_sen,r'\1\2\n',text)
    regex_abrv = r'((Sr)|(Sra)|(Prof)|(Profa)|(Srs)|(Srta)'
    for abrev in abrev_list[procedure_dic['lang']]:
        regex_abrv += fr'|({abrev})'

    regex_abrv += r')\.(\s*)\n'

    return re.sub(regex_abrv,r'\1.\4',text)

def save_poems(poema):
    """Saves a poem in a data structure"""
    list_poemas.append(poema[1])
    return f">>{len(list_poemas)}<<"

def treat_poems(procedure_dic,text):
    """If flagged removes poems from text and saves it on data structure\n
       Poems need to be marked between <poem> and </poem>
    """
    if procedure_dic['poems']:
        regex_poema = r'<poem>(.*?)</poem>'
        text = re.sub(regex_poema,save_poems,text,flags=re.S)
        print(list_poemas)
    return text

## TPC
## TER UMA VERSAO INSTALAVEL DO TOKENIZER 
## DICIONARIO DAS ABREVS A SEREM CARREGADOS DUM FICHEIRO ++
## OPCAO NA LINHA DE COMANDOS PRA ESCOLHER A LINGUA (-l pt) 

def get_abrev():
    file = open('conf/abrev.txt','r')
    txt = file.read()
    ln_list = txt.split("#")
    ln_list = [ln.strip() for ln in ln_list if ln.strip()]
    abrev_dic = {}
    for ln in ln_list:
        lista = ln.split("\n")
        idx = lista[0]
        abrevs = lista[1:]
        if abrevs:
            abrev_dic[idx] = abrevs
    return abrev_dic

def tokenizer():
    procedure_dic = process_arguments()
    if not have_errors():
        text = get_input()
        abrev_list = get_abrev()
        
        # 0. Quebra de pagina
        # 1. Separar pontuação das palavras
        # 2. Marcar capitulos
                # 2.1 - titulo de capitulo na linha seguinte
                # 2.2 - capitulos em multilingua
                # 2.3 - outras unidades de quebra (pe. prologo, introducao, anexo)
        # 3. Separar paragrafos de linhas pequenas
        # 4. Juntar linhas da mesma frase
        # 5. Uma frase por linha
        # 6. Tratar Poemas (tagged)

        # 6. Tratar Poemas (tagged)
        text = treat_poems(procedure_dic,text)

        # 2. Marcar capitulos
        text = treat_chapters(procedure_dic,text)

        # 0. Quebra de pagina
        text = treat_page_break(procedure_dic,text)
        
        # 3. Separar paragrafos de linhas pequenas
        text = treat_paragraphs(procedure_dic,text)

        # 4. Juntar linhas da mesma frase
        text = treat_sentences_single_line(procedure_dic,text)

        # 5. Uma frase por linha
        text = treat_sentences_per_line(procedure_dic,text,abrev_list)

        # 1. Separar pontuação das palavras
        text = treat_punctuation(procedure_dic,text)

        utils.write_output(text)

    utils.print_errors()
