from util.gerais import imprimir_objetos, imprimir_objeto, imprimir_objetos_internos, imprimir_objetos_associação_filtros
from util.data import converte_str_para_data
from entidades.sinistro import Sinistro, inserir_sinistro, get_sinistros
from entidades.seguradora import Seguradora, inserir_seguradora, get_seguradoras
from entidades.peca import PeçaMecânica, PeçaLataria
from entidades.orcamento import Orcamento, filtrar_orçamentos, get_orçamentos, criar_orçamento, inserir_orçamento

def loop_opções_execução():
    sair_loop = False
    cabeçalho_seguradora = '\nSeguradoras : nome - cidade - cobertura percentual'
    cabeçalho_sinistro =  '\nSinistro : numero - clientes - telefone'
    cabeçalho_peças_sinistros = ('\nSinistro : numero - clientes - telefone'
    + '\n - Peças : código - nome - categoria - preço - peça mecânica:[tipo - prazo de garantia] | peça lataria:[tipo - cor]'
    + ' - mão_obra_própria')
    cabeçalho_orçamento = ('\nOrçamento : Numero do sinistro - tipo de peça - nome da seguradora'
    + ' - data do orçamento')

    while not sair_loop:
        print()
        operação = ler_str('Opções [C: Cadastrar / I: Imprimir / S: Selecionar / T: imprimir Todos / <ENTER>: Parar]', retornar=True)
        if operação == None:
            break
        elif operação == 'C':
            opção_conteúdo = ler_str('A: Seguradoras / B: Sinistros / C: Orçamentos / <ENTER>: retornar]',
                                     retornar=True)
            if opção_conteúdo == None:
                pass
            elif opção_conteúdo == 'A':
                loop_leitura_seguradoras()
            elif opção_conteúdo == 'B':
                loop_leitura_sinistros()
            elif opção_conteúdo == 'C':
                loop_leitura_orçamentos()

        elif operação == 'I':
            opção_conteúdo = ler_str('A: Seguradoras / B: Sinistros / C: Orçamentos / P: Peças do sinistro /'
                                     + '<ENTER>: retornar]',
                                     retornar=True)
            if opção_conteúdo == None:
                pass
            elif opção_conteúdo == 'A':
                imprimir_objetos(cabeçalho_seguradora, get_seguradoras().values())
            elif opção_conteúdo == 'B':
                imprimir_objetos(cabeçalho_sinistro, get_sinistros().values())
            elif opção_conteúdo == 'C':
                imprimir_objetos(cabeçalho_orçamento, get_orçamentos())
            elif opção_conteúdo == 'P':
                imprimir_peças_sinistro(cabeçalho_peças_sinistros)

        elif operação == 'S':
            loop_seleção_orçamentos()

        elif operação == 'T':
            imprimir_objetos(cabeçalho_seguradora, get_seguradoras().values())
            imprimir_objetos(cabeçalho_sinistro, get_sinistros().values())
            imprimir_objetos(cabeçalho_orçamento, get_orçamentos())
            imprimir_peças_sinistro(cabeçalho_peças_sinistros)

def imprimir_peças_sinistro(cabeçalho_peças_sinistros):
    print(cabeçalho_peças_sinistros)
    for indice, sinistro in enumerate(get_sinistros().values()):
        imprimir_objeto(índice=indice, objeto_str=str(sinistro))
        imprimir_objetos_internos(sinistro.pecas.values())

def loop_leitura_seguradoras():
    sair_loop = False
    print('--- Leitura de Dados das Seguradoras ---')
    while not sair_loop:
        seguradora = ler_seguradora()
        if seguradora is not None:
            inserir_seguradora(seguradora)
        else:
            print(' - ERRO : na leitura da seguradora')
        sair_loop = ler_sair_loop('cadastro de seguradoras')

def loop_leitura_sinistros():
    sair_loop = False
    print('--- Leitura de Dados dos Sinistros ---')
    while not sair_loop:
        sinistro = ler_sinistro()
        if sinistro is not None:
            inserir_sinistro(sinistro)
            loop_leitura_peças_sinistro(sinistro)
        else: 
            print(' - ERRO : na leitura do sinistro')
        sair_loop = ler_sair_loop('cadastro de sinistro')

def loop_leitura_peças_sinistro(sinistro):
    sair_loop = False
    print('--- Leitura de Dados das Peças do Sinistro : ' + sinistro.numero + ' ---')
    while not sair_loop:
        peça = ler_peça()
        if peça is not None: sinistro.inserir_peca(peça)
        else: 
            print(' - ERRO : na leitura de peça')
        sair_loop = ler_sair_loop('cadastro de peça do sinistro')

def loop_leitura_orçamentos():
    sair_loop = False
    print('--- Leitura de Dados de Orçamentos ---')
    while not sair_loop:
        orçamento = ler_orçamento()
        if orçamento is not None: 
            inserir_orçamento(orçamento)
        else: 
            print(' - ERRO : na leitura do orçamento')
        sair_loop = ler_sair_loop('cadastro do orçamento')

def ler_sair_loop(loop):
    try:
        sair = input('\n-- sair do loop de ' + loop + ' [S]: ')
        if sair == 'S': 
            return True
    except IOError: 
        pass
    return False

def loop_seleção_orçamentos():
    sair_loop = False
    print('--- Seleção de Orçamentos ---')
    while not sair_loop:
        filtros, orçamentos_selecionados = selecionar_orçamentos()
        if filtros is not None:
            cabeçalho = ('Orçamento : número do sinistros - nome da seguradora - data do orçamento'
                 + '\n -- cobertura percentual - cidade'
                 + '\n - peças[tipo_peça_mecânica - dias_garantia | tipo_peça_lataria - cor_peça_lataria]')
            imprimir_objetos_associação_filtros(cabeçalho, orçamentos_selecionados, filtros)
        sair_loop = ler_sair_loop('seleção de lançamentos')

def ler_seguradora():
    nome = ler_str('nome da seguradora')
    if nome == None:
        return None
    cidade = ler_str('cidade da seguradora')
    if cidade == None:
        return None
    cobertura_percentual = ler_int_positivo('cobertura percentual da seguradora')
    if cobertura_percentual == None:
        return None
    return Seguradora(nome, cidade, cobertura_percentual)

def ler_sinistro():
    número = ler_str('numero do sinistro')
    if número == None:
        return None
    cliente = ler_str('cliente do Sinistro')
    if cliente == None:
        return None
    telefone = ler_str('telefone no sinistro [DDD + NUM]')
    if telefone == None:
        return None
    return Sinistro(número, cliente, telefone)

def ler_peça():
    código = ler_int_positivo('código da peça')
    if código == None:
        return None
    nome = ler_str('nome da peça')
    if nome == None:
        return None
    categoria = ler_categoria_peça('categoria da peça')
    if categoria == None:
        return None
    preço = ler_int_positivo('preço da peça')
    if preço == None:
        return None
    mão_obra_própria = ler_bool('mão de obra própria')
    if mão_obra_própria == None:
        return None
    espécie_peça = ler_str('espécie de peça [Pm=Peça mecânica / Pl=Peça lataria]')

    if espécie_peça == 'Pm':
        tipo = ler_tipo_peça_mecanica()
        if tipo == None:
            return None
        dias_garantia = ler_int_positivo('Dias de garantia')
        if dias_garantia == None:
            return None
        return PeçaMecânica(código, nome, categoria, preço, tipo, dias_garantia, mão_obra_própria)

    if espécie_peça == 'Pl':
        tipo = ler_tipo_peça_lataria()
        if tipo == None:
            return None
        cor = ler_str('cor da peça')
        if cor == None:
            return None
        return PeçaLataria(código, nome, categoria, preço, tipo, cor, mão_obra_própria)
    else:
        return None

def ler_orçamento():
    numero_sinistro = ler_str('numero do sisnitro')
    if numero_sinistro == None:
        return None
    nome_seguradora = ler_str('nome da seguradora')
    if nome_seguradora == None:
        return None
    data_orçamento = ler_data('data da orçamento')
    if data_orçamento is None:
        return None
    return criar_orçamento(numero_sinistro, nome_seguradora, data_orçamento)

def selecionar_orçamentos():
    filtros = '\nFiltros -- '

    data_mínima_orcamento = ler_data('data mínima do orçamento', filtro=True)
    if data_mínima_orcamento is not None: filtros += 'Data mínima do orcamento: ' + str(data_mínima_orcamento)

    valor_máximo_peca = ler_int_positivo('maior valor da peça', filtro=True)
    if valor_máximo_peca is not None: filtros += ' - Maior valor da peca: ' + str(valor_máximo_peca)

    cobertura_mínima_seguradora = ler_int_positivo('cobertura mínima da seguradora', filtro=True)
    if cobertura_mínima_seguradora is not None: filtros += '\n - cobertura mínima da seguradora: ' + str(cobertura_mínima_seguradora)

    prefixo_telefone_cliente = ler_str('prefixo do telefone do cliente', filtro=True)
    if prefixo_telefone_cliente is not None: filtros += (' - DDD telefone cliente: ' + str(prefixo_telefone_cliente))

    categoria = ler_str('categoria da peça', filtro=True)
    if categoria is not None: filtros += ' - categoria: ' + str(categoria)

    tipo_peça_mecânica = ler_str('tipo de peça mecânica', filtro=True)
    if tipo_peça_mecânica is not None: filtros += ' - tipo de peça: ' + str(tipo_peça_mecânica)

    dias_garantia_maiores = ler_int_positivo('garantia maior que (dias)', filtro=True)
    if dias_garantia_maiores is not None: filtros += '\n - garantia maior que (dias): ' + str(dias_garantia_maiores)

    tipo_peça_lataria = ler_str('tipo de lataria', filtro=True)
    if tipo_peça_lataria is not None: filtros += ' - tipo de lataria: ' + str(tipo_peça_lataria)

    cor_peça_lataria = ler_str('cor da peça', filtro=True)
    if cor_peça_lataria is not None: filtros += ' - cor da peça: ' + str(cor_peça_lataria)

    orçamentos_selecionados = filtrar_orçamentos(data_mínima_orcamento,
                                                   valor_máximo_peca, cobertura_mínima_seguradora,
                                                   prefixo_telefone_cliente, categoria, tipo_peça_mecânica, dias_garantia_maiores, 
                                                   tipo_peça_lataria,cor_peça_lataria)
    return filtros, orçamentos_selecionados

def ler_categoria_peça(filtro=False):
    try:
        string = input(
            '- tipo de peça [A=Original / B=Genuína / C=OEM ]: ')
        if len(string) == 0 and filtro: return None
        if string == 'A': return 'Original'
        if string == 'B': return 'Genuína'
        if string == 'C': return 'OEM'
    except IOError: 
        pass
    print('Erro na leitura da categoria de peça')
    return None

def ler_tipo_peça_mecanica(filtro=False):
    try:
        string = input(
            '- tipo de peça [A=suspensão / B=direção / C=motor]: ')
        if len(string) == 0 and filtro: 
            return None
        if string == 'A': return 'suspensão'
        if string == 'B': return 'direção'
        if string == 'C': return 'motor'
    except IOError: 
        pass
    print('Erro na leitura do tipo de peça mecânica')
    return None

def ler_tipo_peça_lataria(filtro=False):
    try:
        string = input(
            '- tipo de peça [A=externo / B=interno]: ')
        if len(string) == 0 and filtro: 
            return None
        if string == 'A': return 'externo'
        if string == 'B': return 'interno'
    except IOError: 
        pass
    print('Erro na leitura do tipo de peça de lataria')
    return None

def ler_str(dado, filtro=False, retornar=False):
    try:
        string = input('- ' + dado + ' : ')
        if len(string) == 0 and (filtro or retornar): 
            return None
        if len(string) > 0: 
            return string
    except IOError: 
        pass
    print('Erro na leitura do dado: ' + dado)
    return None

def ler_int_positivo(dado, filtro=False):
    try:
        string = input('- ' + dado + ' : ')
        if len(string) == 0 and filtro: 
            return None
        int_positivo = int(string)
        if int_positivo > 0: 
            return int_positivo
    except ValueError: 
        pass
    print('Erro na leitura/conversão do inteiro positivo: ' + dado)
    return None

def ler_float_positivo(dado, filtro=False):
    try:
        string = input('- ' + dado + ' : ')
        if len(string) == 0 and filtro: 
            return None
        float_positivo = float(string)
        if float_positivo > 0.0: return float_positivo
    except ValueError: 
        pass
    print('Erro na leitura/conversão do flutuante positivo: ' + dado)
    return None

def ler_bool(dado, filtro=False):
    try:
        string = input('- ' + dado + ' [S/N]: ')
        if len(string) == 0 and filtro: 
            return None
        if string == 'S': 
            return True
        elif string == 'N': 
            return False
    except ValueError: 
        pass
    print('Erro na leitura do booleano: ' + dado)
    return None

def ler_data(dado, filtro=False):
    try:
        string = input('- ' + dado + ' [dd/mm/aaaa]: ')
        if len(string) == 0 and filtro: 
            return None
        data = converte_str_para_data(string)
        if data is not None: return data
    except IOError: 
        pass
    print('Erro na leitura da data: ' + dado)
    return None
