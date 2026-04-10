def imprimir_objetos(cabeçalho, objetos, filtros=None):
    if filtros is not None: print(filtros)
    print(cabeçalho)
    for indice, objeto in enumerate(objetos): 
        imprimir_objeto(indice, str(objeto))


def imprimir_objeto(indice, objeto_str):
    formato = '{} {} {}'
    ordem = indice + 1
    separador = '_'
    string_formatado = formato.format(f'{ordem:2d}', separador, objeto_str)
    print(string_formatado)