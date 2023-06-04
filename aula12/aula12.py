from bs4 import BeautifulSoup
import requests
import json
import re

def limpa(text):
    text = re.sub(r' ', ' ', text.strip())
    text = re.sub(r'–', '-', text)
    return text


def get_dic_doencas():
    dic = {}    
    base = 'https://www.atlasdasaude.pt'
    # for letters in the alphabet
    for letter in range(97, 123):
        letter = chr(letter)
        
        url = base + '/doencasaaz/'+ letter
        letter = letter.upper()

        html = requests.get(url).text

        soup = BeautifulSoup(html, 'html.parser')

        row = soup.find_all('div', class_='views-row')
        dic[letter] = {}


        #dic[letter.upper()] =  {r.find('h3').text : 
        #                        limpa(r.find('div',class_='field-content').text)
        #                                                                                        for r in row}


        for r in row:
            if r:
                # r.div.h3.text
                doenca_a = r.find('h3').a
                doenca_url = base + doenca_a['href']
                print(doenca_url) 
                titulo = doenca_a.text
                definicao = limpa(r.find('div',class_='field-content').text)
                dic[letter][titulo] = definicao

        with open('aula12/doencas.json', 'w') as f:
            json.dump(dic, f, indent=4, ensure_ascii=False)
        
    return dic

def print_dic():
    dic = get_dic_doencas()
    for letter in dic:
        print(f'<><><><><><>  {letter.upper()}  <><><><><><>')
        for d in dic[letter]:
            print(f'{d}:\n{dic[letter][d]}\n')


get_dic_doencas()
    