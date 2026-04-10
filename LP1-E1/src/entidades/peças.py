peças = []

def get_peças(): return peças

def inserir_peça(peça): peças.append(peça)

def selecionar_peças(mecânico_próprio=None, categoria=None, preço=None):
    filtros = '\nFiltros -- '
    if mecânico_próprio: filtros += ' Mecãnico Próprio '
    elif mecânico_próprio == False: filtros += ' Manual'
    if categoria is not None: filtros += ' - Categoria: ' + categoria
    if preço is not None: filtros += ' - Preço Menor que: R$ ' + str(preço)
    peças_selecionados = []
    for peça in peças:
        if mecânico_próprio in (True, False) and peça.mecânico_próprio != mecânico_próprio: continue  # pronta entrega ou sob encomenda
        if categoria is not None and peça.categoria != categoria: continue  # novo, usado, recuperado
        if preço is not None and peça.preço > preço: continue  # menor preço
        peças_selecionados.append(peça)
    return filtros, peças_selecionados

class Peça:

    def __init__(self, nome, categoria, preço, mecânico_próprio):
        self.nome = nome
        self.categoria = categoria if categoria in ('original', 'genuína', 'OEM') else 'indefinida'
        self.preço = preço
        self.mecânico_próprio = mecânico_próprio

    def __str__(self):
        if self.mecânico_próprio: mecânico_próprio_str = 'Mecânico Próprio |'
        else: mecânico_próprio_str = ''
        formato = '{} {:<15} {} {:<12} {} {:<6} {} {}'
        peça_formatado = formato.format('|', self.nome, '|', self.categoria, '|', self.preço, '|', mecânico_próprio_str)
        return peça_formatado