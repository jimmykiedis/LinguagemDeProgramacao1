class Peça:

    def __init__(self, nome, categoria, preço, mecânico_próprio):
        self.nome = nome
        self.categoria = categoria if categoria in ('Original', 'Genuína', 'OEM') else 'indefinida'
        self.preço = preço
        self.mecânico_próprio = mecânico_próprio

    def __str__(self):
        if self.mecânico_próprio: mecânico_próprio_str = ' Mecânico Próprio |'
        else: mecânico_próprio_str = ''
        formato = '   {} {:<15} {} {:<12} {} {:<6} {} {}'
        peça_formatado = formato.format('|', self.nome, '|', self.categoria, '|', self.preço, '|', mecânico_próprio_str)
        return peça_formatado