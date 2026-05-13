class Peca:

    def __init__(self, código, nome, categoria, preco, mão_obra_própria):
        self.código = código
        self.nome = nome
        self.categoria = categoria if categoria in ('Original', 'Genuína', 'OEM') else 'indefinida'
        self.preco = preco
        self.mão_obra_própria = mão_obra_própria

    def __str__(self):
        if self.mão_obra_própria: mão_obra_própria_str = ' Mão de obra Própria |'
        else: mão_obra_própria_str = ''
        formato = '   {} {:<15} {} {:<12} {} {:<6} {} {}'
        peca_formatado = formato.format('|', self.nome, '|', self.categoria, '|', f'R$ {self.preco:.2f}', '|', mão_obra_própria_str)
        return peca_formatado
    
class PeçaMecânica(Peca):
    def __init__(self, código, nome, categoria, preco, tipo, prazo_garantia, mão_obra_própria):
        super().__init__(código, nome, categoria, preco, mão_obra_própria) 
        self.tipo = tipo if tipo in ('suspensão', 'direção', 'motor') else 'indefinida'
        self.prazo_garantia = prazo_garantia

    def __str__(self):
        if self.mão_obra_própria: mão_obra_própria_str = ' Mecânico Próprio |'
        else: mão_obra_própria_str = ''
        formato = '   {} {:<15} {} {:<8} {} {:<12} {} {:<8} {} {:>8} {} {}'
        peca_formatado = formato.format('|', self.nome, '|', self.categoria, '|', f'R$ {self.preco:.2f}', '|', self.tipo, '|', self.prazo_garantia, '|', mão_obra_própria_str)
        return peca_formatado

class PeçaLataria(Peca):
    def __init__(self, código, nome, categoria, preco, tipo, cor, mão_obra_própria):
        super().__init__(código, nome, categoria, preco, mão_obra_própria) 
        self.tipo = tipo if tipo in ('externo', 'interno') else 'indefinida'
        self.cor = cor

    def __str__(self):
        if self.mão_obra_própria: mão_obra_própria_str = ' Funileiro Próprio |'
        else: mão_obra_própria_str = ''
        formato = '   {} {:<15} {} {:<8} {} {:<12} {} {:<8} {} {:>8} {} {}'
        peca_formatado = formato.format('|', self.nome, '|', self.categoria, '|', f'R$ {self.preco:.2f}', '|', self.tipo, '|', self.cor, '|', mão_obra_própria_str)
        return peca_formatado