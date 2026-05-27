from util.gerais import imprimir_objetos, imprimir_objeto, imprimir_objetos_internos, imprimir_objetos_associação_filtros
from util.data import Data
from entidades.seguradora import inserir_seguradora, Seguradora, get_seguradoras
from entidades.peca import Peca, PeçaMecânica, PeçaLataria
from entidades.sinistro import inserir_sinistro, Sinistro, get_sinistros
from entidades.orcamento import criar_orcamento, get_orcamentos, selecionar_orcamento

def cadastrar_seguradoras():
    inserir_seguradora(Seguradora(nome='Porto Seguro', cidade='Dourados', cobertura_percentual=90))
    inserir_seguradora(Seguradora(nome='Bradesco Seguros', cidade='Campo Grande', cobertura_percentual=80))
    inserir_seguradora(Seguradora(nome='SulAmérica', cidade='Ponta Porã', cobertura_percentual=90))
    inserir_seguradora(Seguradora(nome='Mapfre', cidade='Dourados', cobertura_percentual=85))
    inserir_seguradora(Seguradora(nome='Allianz', cidade='Campo Grande', cobertura_percentual=75))
    inserir_seguradora(Seguradora(nome='Tokio Marine', cidade='Ponta Porã', cobertura_percentual=90))
    inserir_seguradora(Seguradora(nome='Azos Seguros', cidade='São Paulo', cobertura_percentual=99))
    inserir_seguradora(Seguradora(nome='Liberty Seguros', cidade='Dourados', cobertura_percentual=85))
    inserir_seguradora(Seguradora(nome='Sompo Seguros', cidade='Maracaju', cobertura_percentual=75))
    inserir_seguradora(Seguradora(nome='HDI Seguros', cidade='Naviraí', cobertura_percentual=82))


def cadastrar_sinistros():
    sinistro = Sinistro(numero='1', cliente='Leon', telefone='67 99888-1100')
    inserir_sinistro(sinistro)
    sinistro.inserir_peca(PeçaMecânica(código=11, nome='bandeja', categoria='OEM', preco=245, tipo='suspensão', prazo_garantia='90 dias', mão_obra_própria=False))
    sinistro.inserir_peca(PeçaMecânica(código=12, nome='pivô', categoria='OEM', preco=250, tipo='suspensão', prazo_garantia='90 dias', mão_obra_própria=False))

    sinistro = Sinistro(numero='6', cliente='Scott', telefone='67 98988-1101')
    inserir_sinistro(sinistro)
    sinistro.inserir_peca(PeçaLataria(código=21, nome='para-choque', categoria='Original', preco=200, tipo='externo', cor='preto', mão_obra_própria=False))
    sinistro.inserir_peca(PeçaLataria(código=22, nome='capô', categoria='Original', preco=180, tipo='externo', cor='cinza', mão_obra_própria=False))

    sinistro = Sinistro(numero='11', cliente='Kennedy', telefone='67 96898-1000')
    inserir_sinistro(sinistro)
    sinistro.inserir_peca(PeçaMecânica(código=31, nome='amortecedor', categoria='Original', preco=180, tipo='suspensão', prazo_garantia='90 dias', mão_obra_própria=True))
    sinistro.inserir_peca(PeçaMecânica(código=33, nome='kit batente', categoria='Original', preco=220, tipo='suspensão', prazo_garantia='180 dias', mão_obra_própria=True))

    sinistro = Sinistro(numero='19', cliente='Chris', telefone='67 90898-0100')
    inserir_sinistro(sinistro)
    sinistro.inserir_peca(PeçaLataria(código=41, nome='painel central', categoria='OEM', preco=135, tipo='interno', cor='cinza', mão_obra_própria=True))
    sinistro.inserir_peca(PeçaLataria(código=44, nome='volante', categoria='Original', preco=60, tipo='interno', cor='cinza', mão_obra_própria=True))

    sinistro = Sinistro(numero='98', cliente='Redfield', telefone='66 91681-1198')
    inserir_sinistro(sinistro)
    sinistro.inserir_peca(PeçaMecânica(código=51, nome='pistão', categoria='Genuína', preco=150, tipo='motor', prazo_garantia='365 dias', mão_obra_própria=True))
    sinistro.inserir_peca(PeçaMecânica(código=55, nome='biela', categoria='Genuína', preco=230, tipo='motor', prazo_garantia='365 dias', mão_obra_própria=True))

    sinistro = Sinistro(numero='102', cliente='Jill', telefone='67 99234-8811')
    inserir_sinistro(sinistro)
    sinistro.inserir_peca(PeçaMecânica(código=61, nome='amortecedor', categoria='OEM', preco=150, tipo='suspensão', prazo_garantia='180 dias', mão_obra_própria=False))
    sinistro.inserir_peca(PeçaMecânica(código=62, nome='mola', categoria='OEM', preco=210, tipo='suspensão', prazo_garantia='180 dias', mão_obra_própria=False))

    sinistro = Sinistro(numero='145', cliente='Claire', telefone='67 98112-2290')
    inserir_sinistro(sinistro)
    sinistro.inserir_peca(PeçaLataria(código=71, nome='retrovisor', categoria='Original', preco=210, tipo='externo', cor='cinza', mão_obra_própria=False))
    sinistro.inserir_peca(PeçaLataria(código=72, nome='porta dianteira', categoria='Original', preco=170, tipo='externo', cor='cinza', mão_obra_própria=False))

    sinistro = Sinistro(numero='201', cliente='Ada', telefone='65 99677-4400')
    inserir_sinistro(sinistro)
    sinistro.inserir_peca(PeçaMecânica(código=81, nome='radiador', categoria='Genuína', preco=160, tipo='motor', prazo_garantia='365 dias', mão_obra_própria=True))
    sinistro.inserir_peca(PeçaMecânica(código=82, nome='bieleta', categoria='Genuína', preco=140, tipo='suspensão', prazo_garantia='365 dias', mão_obra_própria=True))

    sinistro = Sinistro(numero='250', cliente='Rebecca', telefone='67 99123-4455')
    inserir_sinistro(sinistro)
    sinistro.inserir_peca(PeçaLataria(código=91, nome='farol', categoria='Original', preco=140, tipo='externo', cor='prata', mão_obra_própria=False))
    sinistro.inserir_peca(PeçaLataria(código=92, nome='lanterna', categoria='OEM', preco=200, tipo='externo', cor='preto', mão_obra_própria=True))

    sinistro = Sinistro(numero='310', cliente='Carlos', telefone='67 98455-7712')
    inserir_sinistro(sinistro)
    sinistro.inserir_peca(PeçaMecânica(código=101, nome='pastilha de freio', categoria='OEM', preco=190, tipo='freio', prazo_garantia='180 dias', mão_obra_própria=False))
    sinistro.inserir_peca(PeçaMecânica(código=102, nome='disco de freio', categoria='Original', preco=320, tipo='freio', prazo_garantia='365 dias', mão_obra_própria=True))

def cadastrar_orcamentos():
    criar_orcamento(numero_sinistro='1', nome_seguradora='Porto Seguro', data=Data(dia=12, mês=6, ano=2026))
    criar_orcamento(numero_sinistro='6', nome_seguradora='Bradesco Seguros', data=Data(dia=10, mês=10, ano=2026))
    criar_orcamento(numero_sinistro='11', nome_seguradora='SulAmérica', data=Data(dia=3, mês=8, ano=2026))
    criar_orcamento(numero_sinistro='19', nome_seguradora='Mapfre', data=Data(dia=2, mês=5, ano=2026))
    criar_orcamento(numero_sinistro='98', nome_seguradora='Allianz', data=Data(dia=28, mês=4, ano=2026))
    criar_orcamento(numero_sinistro='102', nome_seguradora='Tokio Marine', data=Data(dia=15, mês=7, ano=2026))
    criar_orcamento(numero_sinistro='145', nome_seguradora='Azos Seguros', data=Data(dia=22, mês=9, ano=2026))
    criar_orcamento(numero_sinistro='201', nome_seguradora='Liberty Seguros', data=Data(dia=5, mês=11, ano=2026))
    criar_orcamento(numero_sinistro='250', nome_seguradora='Sompo Seguros', data=Data(dia=18, mês=12, ano=2026))
    criar_orcamento(numero_sinistro='310', nome_seguradora='HDI Seguros', data=Data(dia=9, mês=9, ano=2026))

if __name__ == '__main__':
    cadastrar_seguradoras()
    imprimir_objetos(cabeçalho= '\n Seguradoras: Nome  -  Cidade  -  Cobertura percentual', objetos=get_seguradoras().values())

    cadastrar_sinistros()
    imprimir_objetos(cabeçalho='\n Sinistros: Número  -  Cliente  -  Telefone',
                    objetos=get_sinistros().values())

    print('\n Sinistros: Número  -  Cliente  -  Telefone')
    print(' - Pecas: Nome - Categoria - Preco - Tipo - Prazo de Garantia - Mão de obra própria')
    for índice, sinistro in enumerate(get_sinistros().values()):
        imprimir_objeto(índice=índice, objeto_str=str(sinistro))
        imprimir_objetos_internos(sinistro.pecas.values())

    cadastrar_orcamentos()
    cabecalho_orcamento = ('Orcamento: Numero do Sinistro - Nome da Seguradora - Data do orcamento')
    cabecalho_orcamento_filtros = (cabecalho_orcamento + '\n -- Cobertura Percentual - Telefone no Sinistro - Precos das pecas'
                                   + '\n PeçaMecânica[Tipo], PeçaLataria[Cor]')

    imprimir_objetos('\n' + cabecalho_orcamento, get_orcamentos())
    
    filtros, orcamentos_selecionados = selecionar_orcamento()
    imprimir_objetos_associação_filtros(cabecalho_orcamento_filtros, orcamentos_selecionados, filtros)

    filtros, orcamentos_selecionados = selecionar_orcamento(data_mínima_orcamento=Data(dia=1, mês=5, ano=2026))
    imprimir_objetos_associação_filtros(cabecalho_orcamento_filtros, orcamentos_selecionados, filtros)

    filtros, orcamentos_selecionados = selecionar_orcamento(Data(1, 5, 2026), valor_máximo_peca=255)
    imprimir_objetos_associação_filtros(cabecalho_orcamento_filtros, orcamentos_selecionados, filtros)

    filtros, orcamentos_selecionados = selecionar_orcamento(Data(1, 5, 2026), 255, cobertura_mínima_seguradora=80)
    imprimir_objetos_associação_filtros(cabecalho_orcamento_filtros, orcamentos_selecionados, filtros)

    filtros, orcamentos_selecionados = selecionar_orcamento(Data(1, 5, 2026), 255, 80, prefixo_telefone_cliente=67)
    imprimir_objetos_associação_filtros(cabecalho_orcamento_filtros, orcamentos_selecionados, filtros)

    filtros, orcamentos_selecionados = selecionar_orcamento(Data(1, 5, 2026), 255, 80, tipo_peça_mecânica='suspensão')
    imprimir_objetos_associação_filtros(cabecalho_orcamento_filtros, orcamentos_selecionados, filtros)

    filtros, orcamentos_selecionados = selecionar_orcamento(Data(1, 5, 2026), 255, 80, cor_peça_lataria='cinza')
    imprimir_objetos_associação_filtros(cabecalho_orcamento_filtros, orcamentos_selecionados, filtros)
