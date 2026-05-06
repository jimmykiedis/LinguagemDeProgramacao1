sinistros = {}

def get_sinistros (): return sinistros

def inserir_sinistro(sinistro):
    numero_sisnitro = sinistro.numero
    if numero_sisnitro not in sinistros.keys():
        sinistros[numero_sisnitro] = sinistro
        return True
    else:
        print('Sinistro ' + numero_sisnitro + ' já tem cadastro')
        return False

class Sinistro:

    def __init__(self, numero, cliente, telefone):
        self.numero = numero
        self.cliente = cliente
        self.telefone = telefone
        self.pecas = {}

    def __str__(self):
        formato = '{} {:<3} {} {:<15} {} {:<14} {}'
        sinistro_formatado = formato.format('|', self.numero, '|', self.cliente, '|', self.telefone, '|')      
        return sinistro_formatado
    
    def inserir_peca(self, peca):
        nome_peca = peca.nome
        if nome_peca not in self.pecas.keys(): self.pecas[nome_peca] = peca
        else: print('Nome ' + nome_peca + ' já foi cadastrada em Sinistro')