seguradoras = []

def get_seguradoras(): return seguradoras

def inserir_seguradora(seguradora): seguradoras.append(seguradora)

def selecionar_seguradoras(cobertura_percentual = None, cidade = None, prefixo_nome = None):
    filtros = '\nFiltros -- '
    if cobertura_percentual is not None: filtros += ' Cobertura Percentual Mínima: ' + str(cobertura_percentual)
    if cidade is not None: filtros += ' Cidade: ' + str(cidade)
    if prefixo_nome: filtros += ' Prefixo do nome: ' + (prefixo_nome)
    seguradoras_selecionadas = []
    for seguradora in seguradoras:
        if cobertura_percentual is not None and seguradora.cobertura_percentual < cobertura_percentual: continue
        if cidade is not None and seguradora.cidade != cidade: continue
        if prefixo_nome is not None and not seguradora.nome.startswith(prefixo_nome): continue
        seguradoras_selecionadas.append(seguradora)
    return filtros, seguradoras_selecionadas

class Seguradora:
    
    def __init__(self, nome, cidade, cobertura_percentual):
        self.nome = nome
        self.cidade = cidade
        self.cobertura_percentual = cobertura_percentual
    
    def __str__(self):
        formato = '{} {:<18} {} {:<14} {} {:<1} {}'
        seguradora_formatada = formato.format('|', self.nome, '|', self.cidade, '|', str(self.cobertura_percentual), '|')
        return seguradora_formatada