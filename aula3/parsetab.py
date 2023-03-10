
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'AREAS CATEGORIA FORMA IDENTIDADELINGUA INDEX LINGUAS NOME PAIS SEPARADOR1 SEPARADOR2 SEPARADOR3 SEPARADOR4 SEPARADOR5 SEPARADOR6 SIGLAdicionario : conceitosconceitos : conceito SEPARADOR1 conceitosconceitos : conceitoconceito : identidadeconceito SEPARADOR2 AREAS SEPARADOR3 areas SEPARADOR2 LINGUAS SEPARADOR3 linguasidentidadeconceito :  INDEXareas : area SEPARADOR3 areasareas : areaarea : NOMElinguas : lingua SEPARADOR3 linguaslinguas : lingualingua : identidadelingua SEPARADOR4 sinonimosidentidadelingua : IDENTIDADELINGUAsinonimos : sinonimo SEPARADOR4 sinonimossinonimos : sinonimosinonimo : NOME SEPARADOR5 atributossinonimo : NOMEatributos : atributo SEPARADOR5 atributosatributos : atributoatributo : idatrib SEPARADOR6 NOMEidatrib : CATEGORIAidatrib : SIGLAidatrib : FORMAidatrib : PAIS'
    
_lr_action_items = {'INDEX':([0,6,],[5,5,]),'$end':([1,2,3,8,19,20,25,26,27,28,31,32,33,41,42,],[0,-1,-3,-2,-4,-10,-9,-11,-14,-16,-13,-15,-18,-17,-19,]),'SEPARADOR1':([3,19,20,25,26,27,28,31,32,33,41,42,],[6,-4,-10,-9,-11,-14,-16,-13,-15,-18,-17,-19,]),'SEPARADOR2':([4,5,11,12,13,17,],[7,-5,14,-7,-8,-6,]),'AREAS':([7,],[9,]),'SEPARADOR3':([9,12,13,16,20,26,27,28,31,32,33,41,42,],[10,15,-8,18,23,-11,-14,-16,-13,-15,-18,-17,-19,]),'NOME':([10,15,24,29,40,],[13,13,28,28,42,]),'LINGUAS':([14,],[16,]),'IDENTIDADELINGUA':([18,23,],[22,22,]),'SEPARADOR4':([21,22,27,28,32,33,41,42,],[24,-12,29,-16,-15,-18,-17,-19,]),'SEPARADOR5':([28,33,42,],[30,39,-19,]),'CATEGORIA':([30,39,],[35,35,]),'SIGLA':([30,39,],[36,36,]),'FORMA':([30,39,],[37,37,]),'PAIS':([30,39,],[38,38,]),'SEPARADOR6':([34,35,36,37,38,],[40,-20,-21,-22,-23,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'dicionario':([0,],[1,]),'conceitos':([0,6,],[2,8,]),'conceito':([0,6,],[3,3,]),'identidadeconceito':([0,6,],[4,4,]),'areas':([10,15,],[11,17,]),'area':([10,15,],[12,12,]),'linguas':([18,23,],[19,25,]),'lingua':([18,23,],[20,20,]),'identidadelingua':([18,23,],[21,21,]),'sinonimos':([24,29,],[26,31,]),'sinonimo':([24,29,],[27,27,]),'atributos':([30,39,],[32,41,]),'atributo':([30,39,],[33,33,]),'idatrib':([30,39,],[34,34,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> dicionario","S'",1,None,None,None),
  ('dicionario -> conceitos','dicionario',1,'p_dicionario','yacc.py',6),
  ('conceitos -> conceito SEPARADOR1 conceitos','conceitos',3,'p_conceitos','yacc.py',10),
  ('conceitos -> conceito','conceitos',1,'p_conceitos_single','yacc.py',14),
  ('conceito -> identidadeconceito SEPARADOR2 AREAS SEPARADOR3 areas SEPARADOR2 LINGUAS SEPARADOR3 linguas','conceito',9,'p_conceito','yacc.py',18),
  ('identidadeconceito -> INDEX','identidadeconceito',1,'p_identidadeconceito','yacc.py',22),
  ('areas -> area SEPARADOR3 areas','areas',3,'p_areas','yacc.py',26),
  ('areas -> area','areas',1,'p_areas_one','yacc.py',30),
  ('area -> NOME','area',1,'p_area','yacc.py',34),
  ('linguas -> lingua SEPARADOR3 linguas','linguas',3,'p_linguas','yacc.py',38),
  ('linguas -> lingua','linguas',1,'p_linguas_single','yacc.py',42),
  ('lingua -> identidadelingua SEPARADOR4 sinonimos','lingua',3,'p_lingua','yacc.py',46),
  ('identidadelingua -> IDENTIDADELINGUA','identidadelingua',1,'p_identidadelingua','yacc.py',50),
  ('sinonimos -> sinonimo SEPARADOR4 sinonimos','sinonimos',3,'p_sinonimos','yacc.py',54),
  ('sinonimos -> sinonimo','sinonimos',1,'p_sinonimos_single','yacc.py',58),
  ('sinonimo -> NOME SEPARADOR5 atributos','sinonimo',3,'p_sinonimo','yacc.py',62),
  ('sinonimo -> NOME','sinonimo',1,'p_sinonimo_single','yacc.py',66),
  ('atributos -> atributo SEPARADOR5 atributos','atributos',3,'p_atributos','yacc.py',70),
  ('atributos -> atributo','atributos',1,'p_atributos_single','yacc.py',74),
  ('atributo -> idatrib SEPARADOR6 NOME','atributo',3,'p_atributo','yacc.py',78),
  ('idatrib -> CATEGORIA','idatrib',1,'p_idatrib_categoria','yacc.py',82),
  ('idatrib -> SIGLA','idatrib',1,'p_idatrib_sigla','yacc.py',86),
  ('idatrib -> FORMA','idatrib',1,'p_idatrib_forma','yacc.py',90),
  ('idatrib -> PAIS','idatrib',1,'p_idatrib_pais','yacc.py',94),
]
