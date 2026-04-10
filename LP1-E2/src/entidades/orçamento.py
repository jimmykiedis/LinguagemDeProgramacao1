from entidades.seguradora import get_seguradoras
from entidades.sinistro import get_sinistros

orçamentos = []

def get_orçamentos(): return orçamentos

def inserir_orçamento(orçamento):
    if orçamento not in orçamentos: orçamentos.append(orçamento)
    else: print ('Orçamento de Peças tem cadastro --- ' + str(orçamento))

def criar_orçamento(numero_sinistro, nome_peça, nome_seguradora, data):
    sinistro = get_sinistros()[numero_sinistro]
    if sinistro is None:
        print('Sinistro ' + numero_sinistro + ' não cadastrado')
        return
    peça = sinistro.peças[nome_peça]
    if peça is None:
        print('Peça ' + nome_peça + ' não cadastrada no sinistro ' + numero_sinistro)
        return
    seguradora = get_seguradoras()[nome_seguradora]
    if seguradora is None:
        print('Seguradora' + nome_seguradora + ' Não cadastrada')
        return
    orçamento = Orçamento(sinistro, peça, seguradora, data)
    inserir_orçamento(orçamento)

def selecionar_orçamento(data_mínima_orçamento=None, valor_máximo_peça=None, cobertura_mínima_seguradora=None, prefixo_telefone_cliente=None):
    filtros = '\nFiltros -- '
    if data_mínima_orçamento is not None: filtros += ' Data mínima do orçamento: ' + str(data_mínima_orçamento)
    if valor_máximo_peça is not None: filtros += ' Menor valor da peça: ' + str(valor_máximo_peça)
    if cobertura_mínima_seguradora is not None: filtros += '\n - Cobertura mínima da seguradora: ' + str(cobertura_mínima_seguradora)
    if prefixo_telefone_cliente is not None: filtros += (' - Telefone do Cliente: ' + str(prefixo_telefone_cliente))
    orçamentos_selecionados = []
    for orçamento in orçamentos:
        if data_mínima_orçamento is not None and orçamento.data < data_mínima_orçamento: continue
        if valor_máximo_peça is not None and orçamento.peça.preço > valor_máximo_peça: continue
        if (cobertura_mínima_seguradora is not None and orçamento.seguradora.cobertura_percentual < cobertura_mínima_seguradora): continue
        if prefixo_telefone_cliente is not None and not orçamento.sinistro.telefone.startswith(str(prefixo_telefone_cliente)): continue
        orçamentos_selecionados.append(orçamento)
    return filtros, orçamentos_selecionados

class Orçamento:

    def __init__(self, sinistro, peça, seguradora, data):
        self.sinistro = sinistro
        self.peça = peça
        self.seguradora = seguradora
        self.data = data

    def __str__(self):
        formato = '{} {:<15} {} {:<17} {} {:<19} {} {:<10} {}'
        mostra_formato = formato.format('|', self.sinistro.numero, '|', self.peça.nome, '|', self.seguradora.nome, '|', str(self.data), '|')
        return mostra_formato

    def str_filtro(self):
        formato = '{:>2} {} {:<11} {} {:<3} {}'
        filtro_formatado = formato.format(str(self.seguradora.cobertura_percentual), '|', self.sinistro.telefone, '|', f'{self.peça.preço}' + ' preço', '|')
        return self.__str__() + filtro_formatado