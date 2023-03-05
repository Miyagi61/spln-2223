import re
import json


file = open('medicina.json', 'r',encoding='utf8')
out = json.load(file)

new_dic = {}

def resolve_traducoes(dic):
    traducoes = {}
    for lingua in dic['linguas'].keys():
        traducoes[lingua] = dic['linguas'][lingua]

    traducoes['ga'] = {}
    traducoes['ga']['nome'] = dic['nome']
    traducoes['ga']['nota'] = dic['nota']
    traducoes['ga']['genero'] = dic['genero']
    traducoes['ga']['areas'] = dic['areas']
    traducoes['ga']['info'] = dic['info']

    return traducoes

for ent_c in out['C'].keys():
    new_dic[ent_c] = {'area' : out['C'][ent_c]['areas'], 'traducoes' : resolve_traducoes(out['C'][ent_c])}

file2 = open('medicina2.json', 'w',encoding='utf8')
json.dump(new_dic, file2,ensure_ascii=False)