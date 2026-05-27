from util.persistência_arquivo import carregar_arquivo, salvar_arquivo
from entidades.seguradora import get_seguradoras, set_seguradoras
from entidades.peca import get_pecas, set_pecas
from entidades.sinistro import get_sinistros, set_sinistros
from entidades.orcamento import get_orcamentos, set_orcamentos
from interfaces.interface_textual import loop_opções_execução

nome_arquivo = 'orçamento_peças'

def salvar_aplicação():
    orçamento_peças = []
    orçamento_peças.append(get_seguradoras())
    orçamento_peças.append(get_sinistros())
    orçamento_peças.append(get_orcamentos())
    salvar_arquivo(nome_arquivo, objetos=orçamento_peças)

def recuperar_aplicação():
    orçamento_peças = carregar_arquivo(nome_arquivo)
    if orçamento_peças is not None:
        set_seguradoras(orçamento_peças[0])
        set_sinistros(orçamento_peças[1])
        set_orcamentos(orçamento_peças[2])

if __name__ == '__main__':
    recuperar_aplicação()
    loop_opções_execução()
    salvar_aplicação()