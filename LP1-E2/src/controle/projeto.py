from util.gerais import imprimir_objetos, imprimir_objeto, imprimir_objetos_internos, imprimir_objetos_associação_filtros
from util.data import Data
from entidades.seguradora import inserir_seguradora, Seguradora, get_seguradoras
from entidades.peça import Peça
from entidades.sinistro import inserir_sinistro, Sinistro, get_sinistros
from entidades.orçamento import criar_orçamento, get_orçamentos, selecionar_orçamento

def cadastrar_seguradoras():
    inserir_seguradora(Seguradora(nome='Porto Seguro', cidade='Dourados', cobertura_percentual=90))
    inserir_seguradora(Seguradora(nome='Bradesco Seguros', cidade='Campo Grande', cobertura_percentual=80))
    inserir_seguradora(Seguradora(nome='SulAmérica', cidade='Ponta porã', cobertura_percentual=70))
    inserir_seguradora(Seguradora(nome='Mapfre', cidade='Dourados', cobertura_percentual=85))
    inserir_seguradora(Seguradora(nome='Allianz', cidade='Campo Grande', cobertura_percentual=75))

def cadastrar_sinistros():
    sinistro = Sinistro(numero='1', cliente='Leon', telefone='99888-1100')
    inserir_sinistro(sinistro)
    sinistro.inserir_peça(Peça(nome='bandeja', categoria='OEM', preço=255, mecânico_próprio=False))

    sinistro = Sinistro(numero='6', cliente='Scott', telefone='98988-1101')
    inserir_sinistro(sinistro)
    sinistro.inserir_peça(Peça(nome='amortecedor', categoria='Original', preço=310, mecânico_próprio=False))

    sinistro = Sinistro(numero='11', cliente='Kennedy', telefone='96898-1000')
    inserir_sinistro(sinistro)
    sinistro.inserir_peça(Peça(nome='rolamento', categoria='Original', preço=180, mecânico_próprio=True))

    sinistro = Sinistro(numero='19', cliente='Chris', telefone='90898-0100')
    inserir_sinistro(sinistro)
    sinistro.inserir_peça(Peça(nome='terminal', categoria='Original', preço=90, mecânico_próprio=True))

    sinistro = Sinistro(numero='98', cliente='Redfield', telefone='91681-1198')
    inserir_sinistro(sinistro)
    sinistro.inserir_peça(Peça(nome='pivo', categoria='Genuína', preço=150, mecânico_próprio=True))

def cadastrar_orçamentos():
    criar_orçamento(numero_sinistro='1',nome_peça='bandeja', nome_seguradora='Porto Seguro', data=Data(dia=12, mês=6, ano=2026))
    criar_orçamento(numero_sinistro='6',nome_peça='amortecedor', nome_seguradora='Bradesco Seguros', data=Data(dia=10, mês=10, ano=2026))
    criar_orçamento(numero_sinistro='11',nome_peça='rolamento', nome_seguradora='SulAmérica', data=Data(dia=3, mês=8, ano=2026))
    criar_orçamento(numero_sinistro='19',nome_peça='terminal', nome_seguradora='Mapfre', data=Data(dia=2, mês=5, ano=2026))
    criar_orçamento(numero_sinistro='98',nome_peça='pivo', nome_seguradora='Allianz', data=Data(dia=28, mês=4, ano=2026))

def imprimir_somente_para_alinhar_formatação():
    print('\nSinistros: Numero - Cliente - Telefone')
    for índice, sinistro in enumerate(get_sinistros().values()): print(sinistro)
    print('\nPeças: Nome - Categoria - Preço - Mecânico Próprio')
    for sinistro in get_sinistros().values():
        for peça in sinistro.peças.values(): print(peça)

if __name__ == '__main__':
    cadastrar_seguradoras()
    imprimir_objetos(cabeçalho= '\n Seguradoras: Nome  -  Cidade  -  Cobertura percentual', objetos=get_seguradoras().values())
    cadastrar_sinistros()
    imprimir_somente_para_alinhar_formatação()
    print('\nSinistros: Número - Cliente - Telefone')
    print(' - Peças: Nome - Categoria - Preço - Mecânico Próprio')
    for índice, sinistro in enumerate(get_sinistros().values()):
        imprimir_objeto(índice=índice, objeto_str=sinistro)
        print('-' * 60)
        imprimir_objetos_internos(sinistro.peças.values())
        print('\n')
        print('*' * 60)
        print('\n')
    cadastrar_orçamentos()
    cabeçalho_orçamento = ('Orçamento: Numero do Sinistro - Nome da Peça - Nome da Seguradora - Data do orçamento')
    imprimir_objetos('\n' + cabeçalho_orçamento, get_orçamentos())
    
    filtros, orçamentos_selecionados = selecionar_orçamento()
    cabeçalho_orçamento_filtros = (cabeçalho_orçamento + '\n -- Cobertura Percentual - Telefone no Sinistro - Preço da peça')
    imprimir_objetos_associação_filtros(cabeçalho_orçamento_filtros, orçamentos_selecionados, filtros)

    filtros, orçamentos_selecionados = selecionar_orçamento(data_mínima_orçamento=Data(dia=1, mês=5, ano=2026))
    imprimir_objetos_associação_filtros(cabeçalho_orçamento_filtros, orçamentos_selecionados, filtros)

    filtros, orçamentos_selecionados = selecionar_orçamento(Data(1, 5, 2026), valor_máximo_peça=255)
    imprimir_objetos_associação_filtros(cabeçalho_orçamento_filtros, orçamentos_selecionados, filtros)

    filtros, orçamentos_selecionados = selecionar_orçamento(Data(1, 5, 2026), 255, cobertura_mínima_seguradora=85)
    imprimir_objetos_associação_filtros(cabeçalho_orçamento_filtros, orçamentos_selecionados, filtros)

    filtros, orçamentos_selecionados = selecionar_orçamento(Data(1, 5, 2026), 255, 85, prefixo_telefone_cliente=99)
    imprimir_objetos_associação_filtros(cabeçalho_orçamento_filtros, orçamentos_selecionados, filtros)