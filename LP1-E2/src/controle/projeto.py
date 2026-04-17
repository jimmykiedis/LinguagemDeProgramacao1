from util.gerais import imprimir_objetos, imprimir_objeto, imprimir_objetos_internos, imprimir_objetos_associação_filtros
from util.data import Data
from entidades.seguradora import inserir_seguradora, Seguradora, get_seguradoras
from entidades.peca import Peca
from entidades.sinistro import inserir_sinistro, Sinistro, get_sinistros
from entidades.orcamento import criar_orcamento, get_orcamentos, selecionar_orcamento

def cadastrar_seguradoras():
    inserir_seguradora(Seguradora(nome='Porto Seguro', cidade='Dourados', cobertura_percentual=90))
    inserir_seguradora(Seguradora(nome='Bradesco Seguros', cidade='Campo Grande', cobertura_percentual=80))
    inserir_seguradora(Seguradora(nome='SulAmérica', cidade='Ponta porã', cobertura_percentual=70))
    inserir_seguradora(Seguradora(nome='Mapfre', cidade='Dourados', cobertura_percentual=85))
    inserir_seguradora(Seguradora(nome='Allianz', cidade='Campo Grande', cobertura_percentual=75))

def cadastrar_sinistros():
    sinistro = Sinistro(numero='1', cliente='Leon', telefone='67 99888-1100')
    inserir_sinistro(sinistro)
    sinistro.inserir_peca(Peca(código=11, nome='bandeja', categoria='OEM', preco=245, mecânico_próprio=False))
    sinistro.inserir_peca(Peca(código=12, nome='pivo', categoria='OEM', preco=250, mecânico_próprio=False))

    sinistro = Sinistro(numero='6', cliente='Scott', telefone='67 98988-1101')
    inserir_sinistro(sinistro)
    sinistro.inserir_peca(Peca(código=21, nome='amortecedor', categoria='Original', preco=310, mecânico_próprio=False))
    sinistro.inserir_peca(Peca(código=22, nome='kit batente', categoria='Original', preco=90, mecânico_próprio=False))

    sinistro = Sinistro(numero='11', cliente='Kennedy', telefone='67 96898-1000')
    inserir_sinistro(sinistro)
    sinistro.inserir_peca(Peca(código=31, nome='rolamento', categoria='Original', preco=180, mecânico_próprio=True))
    sinistro.inserir_peca(Peca(código=33, nome='cubo', categoria='Original', preco=180, mecânico_próprio=True))

    sinistro = Sinistro(numero='19', cliente='Chris', telefone='44 90898-0100')
    inserir_sinistro(sinistro)
    sinistro.inserir_peca(Peca(código=41, nome='terminal', categoria='Original', preco=90, mecânico_próprio=True))
    sinistro.inserir_peca(Peca(código=44, nome='barra axial', categoria='Original', preco=90, mecânico_próprio=True))

    sinistro = Sinistro(numero='98', cliente='Redfield', telefone='66 91681-1198')
    inserir_sinistro(sinistro)
    sinistro.inserir_peca(Peca(código=51, nome='disco freio', categoria='Genuína', preco=150, mecânico_próprio=True))
    sinistro.inserir_peca(Peca(código=55, nome='pastilha freio', categoria='Genuína', preco=150, mecânico_próprio=True))

def cadastrar_orcamentos():
    criar_orcamento(numero_sinistro='1', nome_seguradora='Porto Seguro', data=Data(dia=12, mês=6, ano=2026))
    criar_orcamento(numero_sinistro='6', nome_seguradora='Bradesco Seguros', data=Data(dia=10, mês=10, ano=2026))
    criar_orcamento(numero_sinistro='11', nome_seguradora='SulAmérica', data=Data(dia=3, mês=8, ano=2026))
    criar_orcamento(numero_sinistro='19', nome_seguradora='Mapfre', data=Data(dia=2, mês=5, ano=2026))
    criar_orcamento(numero_sinistro='98', nome_seguradora='Allianz', data=Data(dia=28, mês=4, ano=2026))

if __name__ == '__main__':
    cadastrar_seguradoras()
    imprimir_objetos(cabeçalho= '\n Seguradoras: Nome  -  Cidade  -  Cobertura percentual', objetos=get_seguradoras().values())

    cadastrar_sinistros()
    imprimir_objetos(cabeçalho='\n Sinistros: Número  -  Cliente  -  Telefone percentual',
                    objetos=get_sinistros().values())

    print('\n Sinistros: Número  -  Cliente  -  Telefone percentual')
    print('\n - Pecas: Nome - Categoria - Preco - Mecânico Próprio')
    for índice, sinistro in enumerate(get_sinistros().values()):
        imprimir_objeto(índice=índice, objeto_str=sinistro)
        imprimir_objetos_internos(sinistro.pecas.values())

    cadastrar_orcamentos()
    cabecalho_orcamento = ('Orcamento: Numero do Sinistro - Nome da Seguradora - Data do orcamento')
    cabecalho_orcamento_filtros = (cabecalho_orcamento + '\n -- Cobertura Percentual - Telefone no Sinistro - Precos das pecas no sinistro')

    imprimir_objetos('\n' + cabecalho_orcamento, get_orcamentos())
    
    filtros, orcamentos_selecionados = selecionar_orcamento()
    imprimir_objetos_associação_filtros(cabecalho_orcamento_filtros, orcamentos_selecionados, filtros)

    filtros, orcamentos_selecionados = selecionar_orcamento(data_mínima_orcamento=Data(dia=1, mês=5, ano=2026))
    imprimir_objetos_associação_filtros(cabecalho_orcamento_filtros, orcamentos_selecionados, filtros)

    filtros, orcamentos_selecionados = selecionar_orcamento(Data(1, 5, 2026), valor_máximo_peca=255)
    imprimir_objetos_associação_filtros(cabecalho_orcamento_filtros, orcamentos_selecionados, filtros)

    filtros, orcamentos_selecionados = selecionar_orcamento(Data(1, 5, 2026), 255, cobertura_mínima_seguradora=85)
    imprimir_objetos_associação_filtros(cabecalho_orcamento_filtros, orcamentos_selecionados, filtros)

    filtros, orcamentos_selecionados = selecionar_orcamento(Data(1, 5, 2026), 255, 85, prefixo_telefone_cliente=67)
    imprimir_objetos_associação_filtros(cabecalho_orcamento_filtros, orcamentos_selecionados, filtros)
