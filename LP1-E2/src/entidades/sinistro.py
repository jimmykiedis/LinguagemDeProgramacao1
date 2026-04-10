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
        self.peças = {}

    def __str__(self):
        formato = '{} {:<15} {} {:<21} {} {:<14}'
        sinistro_formatado = formato.format('|', self.numero, '|', self.cliente, '|', self.telefone)      
        return sinistro_formatado
    
    def inserir_peça(self, peça):
        nome_peça = peça.nome
        if nome_peça not in self.peças.keys(): self.peças[nome_peça] = peça
        else: print('Nome ' + nome_peça + ' já foi cadastrada em Sinistro')