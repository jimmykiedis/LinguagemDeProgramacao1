seguradoras = {}

def get_seguradoras(): return seguradoras

def inserir_seguradora(seguradora): 
    nome_seguradora = seguradora.nome
    if nome_seguradora not in seguradoras.keys():
        seguradoras[nome_seguradora] = seguradora
        return True
    else:
        print('Seguradora ' + nome_seguradora + ' tem cadastro')
        return False

class Seguradora:
    
    def __init__(self, nome, cidade, cobertura_percentual):
        self.nome = nome
        self.cidade = cidade
        self.cobertura_percentual = cobertura_percentual
    
    def __str__(self):
        formato = '{} {:<18} {} {:<14} {} {:<3} {}'
        seguradora_formatada = formato.format('|', self.nome, '|', self.cidade, '|', str(self.cobertura_percentual), '|')
        return seguradora_formatada