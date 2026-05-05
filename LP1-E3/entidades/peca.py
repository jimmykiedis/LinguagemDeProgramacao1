class Peca:

    def __init__(self, código, nome, categoria, preco, mecânico_próprio):
        self.código = código
        self.nome = nome
        self.categoria = categoria if categoria in ('Original', 'Genuína', 'OEM') else 'indefinida'
        self.preco = preco
        self.mecânico_próprio = mecânico_próprio

    def __str__(self):
        if self.mecânico_próprio: mecânico_próprio_str = ' Mecânico Próprio |'
        else: mecânico_próprio_str = ''
        formato = '   {} {:<15} {} {:<12} {} {:<6} {} {}'
        peca_formatado = formato.format('|', self.nome, '|', self.categoria, '|', self.preco, '|', mecânico_próprio_str)
        return peca_formatado