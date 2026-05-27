from util.gerais import imprimir_objetos, imprimir_objeto, imprimir_objetos_internos, imprimir_objetos_associação_filtros
from util.data import converte_str_para_data
from entidades.sinistro import Sinistro, inserir_sinistro, get_sinistros
from entidades.seguradora import Seguradora, inserir_seguradora, get_seguradoras
from entidades.peca import PeçaMecânica, PeçaLataria
from entidades.orcamento import Orcamento, filtrar_orçamentos, get_orçamentos, criar_orçamento, inserir_orçamento

def loop_opções_execução():
    sair_loop = False
    cabeçalho_seguradora = '\nSeguradoras : nome - cidade - cobertura percentual'
    cabeçalho_sinistro_peças = ('\nSinistro : numero - clientes - telefone'
    + '\n - Peças : código - nome - categoria - preço - peça mecânica:[tipo - prazo de garantia] | peça lataria:[tipo - cor]'
    + ' - mão_obra_própria')
    cabeçalho_orçamento = ('\nOrçamento : Numero do sinistro - tipo de peça - nome da seguradora'
    + ' - data do orçamento')

    while not sair_loop:
        print()
        operação = ler_str('Opções [C: Cadastrar / I: Imprimir / S: Selecionar / T: imprimir Todos / <ENTER>: Parar]', retornar=True)
        if operação == None: break
        elif operação in ('C', 'I'):
            opção_conteúdo = ler_str('A: Seguradoras / M: Sinistros / L: Orçamentos / <ENTER>: retornar]', retornar=True)
            if opção_conteúdo == None: pass
            elif opção_conteúdo == 'A':
                if operação == 'C': loop_leitura_seguradoras()
                imprimir_objetos(cabeçalho_seguradora, get_seguradoras().values())
            elif opção_conteúdo in 'M':
                if operação == 'C': loop_leitura_sinistros()
                imprimir_sinistros_peças(cabeçalho_sinistro_peças)
            elif opção_conteúdo == 'L':
                if operação == 'C': loop_leitura_orçamentos()
                imprimir_objetos(cabeçalho_orçamento, get_orçamentos())
            elif operação == 'S': loop_seleção_orçamentos()
            elif operação == 'T':
                imprimir_objetos(cabeçalho_agência_publicidade, get_agências_publicidade().values())
                imprimir_montadoras_veículos(cabeçalho_montadora_veículos)
                imprimir_objetos(cabeçalho_lançamento, get_lançamentos())