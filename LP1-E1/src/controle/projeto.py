from scr.util.gerais import imprimir_objetos
from scr.entidades.seguradora import (inserir_seguradora, Seguradora, get_seguradoras, selecionar_seguradoras)
from scr.entidades.peças import inserir_peça, Peça, get_peças, selecionar_peças


def cadastrar_seguradoras():
    inserir_seguradora(Seguradora(nome='Porto Seguro', cidade='Dourados', cobertura_percentual=90))
    inserir_seguradora(Seguradora(nome='Bradesco Seguros', cidade='Campo Grande', cobertura_percentual=80))
    inserir_seguradora(Seguradora(nome='SulAmérica', cidade='Ponta porã', cobertura_percentual=70))
    inserir_seguradora(Seguradora(nome='Mapfre', cidade='Dourados', cobertura_percentual=85))
    inserir_seguradora(Seguradora(nome='Allianz', cidade='Campo Grande', cobertura_percentual=75))

def cadastrar_peças():
    inserir_peça(Peça(nome='bandeja', categoria='OEM', preço=255, mecânico_próprio=False))
    inserir_peça(Peça(nome='amortecedor', categoria='original', preço=310, mecânico_próprio=False))
    inserir_peça(Peça(nome='rolamento', categoria='original', preço=180, mecânico_próprio=True))
    inserir_peça(Peça(nome='terminal', categoria='original', preço=90, mecânico_próprio=True))
    inserir_peça(Peça(nome='pivo', categoria='genuína', preço=150, mecânico_próprio=True))

if __name__ == '__main__':
    print('Orçamento de peças de um sinistro para uma seguradora')
    
    cadastrar_seguradoras()

    cabeçalho = 'Seguradora : nome - cidade - cobertural Percentual Máxima'
    imprimir_objetos(cabeçalho='\n' + cabeçalho, objetos=get_seguradoras())

    filtros, seguradoras_selecionadas = selecionar_seguradoras()
    imprimir_objetos(cabeçalho, seguradoras_selecionadas, filtros)

    filtros, seguradoras_selecionadas = selecionar_seguradoras(cobertura_percentual=75)
    imprimir_objetos(cabeçalho, seguradoras_selecionadas, filtros)

    filtros, seguradoras_selecionadas = selecionar_seguradoras(75, cidade='Dourados')
    imprimir_objetos(cabeçalho, seguradoras_selecionadas, filtros)

    filtros, seguradoras_selecionadas = selecionar_seguradoras(75, 'Dourados', prefixo_nome='P')
    imprimir_objetos(cabeçalho, seguradoras_selecionadas, filtros)

    cadastrar_peças()

    cabeçalho = 'peças : nome - categoria - menor_preco - Mecânico Próprio'
    imprimir_objetos('\n' + cabeçalho, get_peças())

    filtros, peças_selecionados = selecionar_peças()
    imprimir_objetos(cabeçalho, peças_selecionados, filtros)

    filtros, peças_selecionados = selecionar_peças(mecânico_próprio=True)
    imprimir_objetos(cabeçalho, peças_selecionados, filtros)

    filtros, peças_selecionados = selecionar_peças(True, categoria='original')
    imprimir_objetos(cabeçalho, peças_selecionados, filtros)

    filtros, peças_selecionados = selecionar_peças(True, 'original', preço=100)
    imprimir_objetos(cabeçalho, peças_selecionados, filtros)

