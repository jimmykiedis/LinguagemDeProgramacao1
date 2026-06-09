from entidades.seguradora import get_seguradoras
from entidades.sinistro import get_sinistros
from entidades.peca import Peca, PeçaMecânica, PeçaLataria

orcamentos = []

def get_orçamentos(): return orcamentos

def set_orcamentos(orcamentos1):
    global orcamentos
    orcamentos = orcamentos1

def inserir_orçamento(orcamento):
    if orcamento not in orcamentos: orcamentos.append(orcamento)
    else: print ('Orcamento de Pecas tem cadastro --- ' + str(orcamento))

def criar_orçamento(numero_sinistro, código_peça, nome_seguradora, data):
    sinistro = get_sinistros().get(numero_sinistro)
    if sinistro is None:
        print('Sinistro ' + numero_sinistro + ' não cadastrado')
        return
    
    seguradora = get_seguradoras().get(nome_seguradora)
    if seguradora is None:
        print('Seguradora ' + nome_seguradora + ' não cadastrada')
        return

    orcamento = Orcamento(sinistro, código_peça, seguradora, data)
    inserir_orçamento(orcamento)

def filtrar_orçamentos(data_mínima_orcamento, valor_máximo_peca, cobertura_mínima_seguradora, prefixo_telefone_cliente, categoria,
                        tipo_peça_mecânica, dias_garantia_maiores, tipo_peça_lataria,cor_peça_lataria):
    orçamentos_selecionados = []
    for orçamento in orcamentos:
        if data_mínima_orcamento is not None and orçamento.data < data_mínima_orcamento: 
            continue

        excluir_orcamento = False
        for peca in orçamento.sinistro.pecas.values():
            if valor_máximo_peca is not None and peca.preco > valor_máximo_peca:
                excluir_orcamento = True
                break
        if excluir_orcamento:
            continue
        
        if (cobertura_mínima_seguradora is not None 
            and orçamento.seguradora.cobertura_mínima_seguradora < cobertura_mínima_seguradora):
            continue
        
        if prefixo_telefone_cliente is not None and not orçamento.sinistro.telefone.startswith(str(prefixo_telefone_cliente)):
            continue
        
        excluir_lançamento = False
        for peca in orçamento.sinistro.pecas.values():
            if categoria is not None and peca.categoria != categoria:
                excluir_lançamento = True
                break
            
            if isinstance(peca, PeçaMecânica):
                if tipo_peça_mecânica is not None and peca.tipo != tipo_peça_mecânica:
                    excluir_lançamento = True
                    break
                if dias_garantia_maiores is not None: 
                    prazo_dias = int(str(peca.dias_garantia).split()[0])
                    if prazo_dias <= dias_garantia_maiores:
                        excluir_orcamento = True
                        break
            
            elif isinstance(peca, PeçaLataria):
                if tipo_peça_lataria is not None and peca.tipo != tipo_peça_lataria:
                    excluir_orcamento = True
                    break
                if cor_peça_lataria is not None and peca.cor != cor_peça_lataria:
                    excluir_orcamento = True
                    break

        if excluir_orcamento: 
            continue
        
        orçamentos_selecionados.append(orçamento)
    return orçamentos_selecionados

class Orcamento:
    def __init__(self, sinistro, código_peça, seguradora, data):
        self.sinistro = sinistro
        self.código_peça = código_peça
        self.seguradora = seguradora
        self.data = data

    def __str__(self):
        formato = '{} {:<3} {} {:<19} {} {:<10} {}'
        mostra_formato = formato.format('|', self.sinistro.numero, '|', self.seguradora.nome, '|', str(self.data), '|')
        return mostra_formato

    def str_valores_pecas(self):
        valores_pecas_str = ''
        for indice, peca in enumerate(self.sinistro.pecas.values()):
            if indice > 0:
                valores_pecas_str += ' - '
            valores_pecas_str += f'R$ {peca.preco:.2f}'
        return valores_pecas_str

    def str_atributos_pecas(self):
        atributos_pecas_str = ''
        for indice, peca in enumerate(self.sinistro.pecas.values()):
            if indice > 0:
                atributos_pecas_str += ' -- '
            if isinstance(peca, PeçaMecânica):
                atributos_pecas_str += f'{peca.dias_garantia} dias - {peca.tipo}'
            elif isinstance(peca, PeçaLataria):
                atributos_pecas_str += f'{peca.tipo} - {peca.cor}'
        return atributos_pecas_str

    def str_filtro(self):
        formato = '{:>2} {} {:<11} {} {:<23} {} {:<55} {}'
        filtro_formatado = formato.format(
            str(self.seguradora.cobertura_percentual) + '%',
            '|', self.sinistro.telefone,
            '|', self.str_valores_pecas(),
            '|', self.str_atributos_pecas(),
            '|'
        )
        return self.__str__() + filtro_formatado