from entidades.seguradora import get_seguradoras
from entidades.sinistro import get_sinistros
from entidades.peca import Peca, PeçaMecânica, PeçaLataria

orcamentos = []

def get_orcamentos(): return orcamentos

def inserir_orcamento(orcamento):
    if orcamento not in orcamentos: orcamentos.append(orcamento)
    else: print ('Orcamento de Pecas tem cadastro --- ' + str(orcamento))

def criar_orcamento(numero_sinistro, nome_seguradora, data):
    sinistro = get_sinistros().get(numero_sinistro)
    if sinistro is None:
        print('Sinistro ' + numero_sinistro + ' não cadastrado')
        return

    seguradora = get_seguradoras().get(nome_seguradora)
    if seguradora is None:
        print('Seguradora ' + nome_seguradora + ' não cadastrada')
        return

    orcamento = Orcamento(sinistro, seguradora, data)
    inserir_orcamento(orcamento)


def selecionar_orcamento(data_mínima_orcamento=None, valor_máximo_peca=None, cobertura_mínima_seguradora=None, prefixo_telefone_cliente=None, 
                         tipo_peça_mecânica=None, prazo_garantia_maiores=None, tipo_peça_lataria=None, cor_peça_lataria=None):
    filtros = '\nFiltros -- '
    if data_mínima_orcamento is not None: filtros += 'Data mínima do orcamento: ' + str(data_mínima_orcamento)
    if valor_máximo_peca is not None: filtros += ' - Maior valor da peca: ' + str(valor_máximo_peca)
    if cobertura_mínima_seguradora is not None: filtros += '\n - Cobertura mínima da seguradora: ' + str(cobertura_mínima_seguradora)
    if prefixo_telefone_cliente is not None: filtros += (' - DDD telefone cliente: ' + str(prefixo_telefone_cliente))
    if tipo_peça_mecânica is not None: filtros += ' - Tipo de peça: ' + str(tipo_peça_mecânica)
    if prazo_garantia_maiores is not None: filtros += ' - Garantia maior que (dias): ' + str(prazo_garantia_maiores)
    if tipo_peça_lataria is not None: filtros += ' - Tipo de lataria: ' + str(tipo_peça_lataria)
    if cor_peça_lataria is not None: filtros += ' - Cor da peça: ' + str(cor_peça_lataria)


    filtrar_mecanica = tipo_peça_mecânica is not None or prazo_garantia_maiores is not None
    filtrar_lataria = tipo_peça_lataria is not None or cor_peça_lataria is not None

    orcamentos_selecionados = []
    for orcamento in orcamentos:
        if data_mínima_orcamento is not None and orcamento.data < data_mínima_orcamento:
            continue

        excluir_orcamento = False
        for peca in orcamento.sinistro.pecas.values():
            if valor_máximo_peca is not None and peca.preco > valor_máximo_peca:
                excluir_orcamento = True
                break

        if excluir_orcamento:
            continue

        if cobertura_mínima_seguradora is not None and orcamento.seguradora.cobertura_percentual < cobertura_mínima_seguradora:
            continue

        if prefixo_telefone_cliente is not None and not orcamento.sinistro.telefone.startswith(str(prefixo_telefone_cliente)):
            continue

        pecas_mecanicas = [peca for peca in orcamento.sinistro.pecas.values() if isinstance(peca, PeçaMecânica)]
        pecas_lataria = [peca for peca in orcamento.sinistro.pecas.values() if isinstance(peca, PeçaLataria)]

        if filtrar_mecanica and not pecas_mecanicas:
            continue
        if filtrar_lataria and not pecas_lataria:
            continue

        for peca in pecas_mecanicas:
            if tipo_peça_mecânica is not None and peca.tipo != tipo_peça_mecânica:
                excluir_orcamento = True
                break
            if prazo_garantia_maiores is not None:
                prazo_dias = int(str(peca.prazo_garantia).split()[0])
                if prazo_dias <= prazo_garantia_maiores:
                    excluir_orcamento = True
                    break
        if excluir_orcamento:
            continue

        for peca in pecas_lataria:
            if tipo_peça_lataria is not None and peca.tipo != tipo_peça_lataria:
                excluir_orcamento = True
                break
            if cor_peça_lataria is not None and peca.cor != cor_peça_lataria:
                excluir_orcamento = True
                break
        if excluir_orcamento:
            continue

        orcamentos_selecionados.append(orcamento)
    return filtros, orcamentos_selecionados

class Orcamento:
    def __init__(self, sinistro, seguradora, data):
        self.sinistro = sinistro
        self.seguradora = seguradora
        self.data = data

    def __str__(self):
        formato = '{} {:<3} {} {:<19} {} {:<10} {}'
        mostra_formato = formato.format('|', self.sinistro.numero, '|', self.seguradora.nome, '|', str(self.data), '|')
        return mostra_formato

    def str_atributos_pecas(self):
        atributos_pecas_str = ''
        for indice, peca in enumerate(self.sinistro.pecas.values()):
            if indice > 0:
                atributos_pecas_str += ' -- '
            atributos_pecas_str += f'R$ {peca.preco:.2f} - '
            if isinstance(peca, PeçaMecânica):
                atributos_pecas_str += peca.tipo
            elif isinstance(peca, PeçaLataria):
                atributos_pecas_str += peca.cor
        return atributos_pecas_str

    def str_filtro(self):
        formato = '{:>2} {} {:<11} {} {:<46} {}'
        filtro_formatado = formato.format(
            str(self.seguradora.cobertura_percentual) + '%',
            '|', self.sinistro.telefone, '|', self.str_atributos_pecas(), '|'
        )
        return self.__str__() + filtro_formatado
