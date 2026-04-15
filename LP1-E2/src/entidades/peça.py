class Peça:

    def __init__(self, código, nome, categoria, preço, mecânico_próprio):
        self.código = código
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

    def str_atributos_peças(self):
        atributos_peças_str = ''
        for índice, peça in enumerate(self.sinistro.peças.values()):
            if (índice > 0): atributos_peças_str += '-'
            atributos_peças_str += 'R$ ' + f'{peça.preço:3d}'
        return atributos_peças_str

    def str_filtro(self):
        formato = '{:>2} {} {:<14} {} {:<15} {}'
        filtro_formatado = formato.format(str(self.seguradora.cobertura_percentual),
                                          '|', self.sinistro.cliente, '|', self.atributos_peças_str(), '|')
        return self.__str__() + filtro_formatado