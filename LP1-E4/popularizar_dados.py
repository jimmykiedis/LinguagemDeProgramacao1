from pathlib import Path
import pickle
import sys

BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR / 'src'
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from util.data import Data
from entidades.seguradora import Seguradora, inserir_seguradora, set_seguradoras, get_seguradoras
from entidades.sinistro import Sinistro, inserir_sinistro, set_sinistros, get_sinistros
from entidades.peca import PeçaMecânica, PeçaLataria
from entidades.orcamento import criar_orçamento, set_orcamentos, get_orçamentos

ARQUIVO_TXT = BASE_DIR / 'dados.txt'
ARQUIVO_BIN = BASE_DIR / 'dados' / 'arquivo.bin'


def limpar_conjuntos_globais():
    set_seguradoras({})
    set_sinistros({})
    set_orcamentos([])


def normalizar_texto(texto):
    return texto.strip().rstrip(';')


def ler_dados_txt():
    with ARQUIVO_TXT.open('r', encoding='utf-8') as arquivo:
        linhas = [linha.rstrip() for linha in arquivo]

    seguradoras_dados = []
    sinistros_dados = []
    orcamentos_dados = []

    indice = 0
    while indice < len(linhas):
        linha = linhas[indice].strip()
        if linha == 'seguradoras[nome, cidade, cobertura_percentual]:':
            indice += 1
            while indice < len(linhas):
                linha = linhas[indice].strip()
                if not linha:
                    indice += 1
                    break
                if linha.startswith('Sinistros['):
                    break
                if linha.startswith('Orçamentos['):
                    break
                partes = [parte.strip() for parte in normalizar_texto(linha).split(',')]
                if len(partes) == 3:
                    seguradoras_dados.append(tuple(partes))
                indice += 1
            continue

        if linha.startswith('Sinistros['):
            indice += 1
            sinistro_atual = None
            while indice < len(linhas):
                linha = linhas[indice].rstrip()
                linha_strip = linha.strip()
                if not linha_strip:
                    indice += 1
                    continue
                if linha_strip.startswith('Orçamentos['):
                    break
                conteudo = linha_strip.lstrip('→').strip()
                partes = [parte.strip() for parte in normalizar_texto(conteudo).split(',')]
                if len(partes) == 3:
                    sinistro_atual = {'numero': partes[0], 'cliente': partes[1], 'telefone': partes[2], 'pecas': []}
                    sinistros_dados.append(sinistro_atual)
                elif len(partes) == 7 and sinistro_atual is not None:
                    sinistro_atual['pecas'].append(tuple(partes))
                indice += 1
            continue

        if linha.startswith('Orçamentos['):
            indice += 1
            while indice < len(linhas):
                linha = linhas[indice].strip()
                if not linha:
                    indice += 1
                    continue
                partes = [parte.strip() for parte in normalizar_texto(linha).split(',')]
                if len(partes) == 3:
                    orcamentos_dados.append(tuple(partes))
                indice += 1
            continue

        indice += 1

    return seguradoras_dados, sinistros_dados, orcamentos_dados


def cadastrar_seguradoras(seguradoras_dados):
    for nome, cidade, cobertura_percentual in seguradoras_dados:
        inserir_seguradora(Seguradora(nome=nome, cidade=cidade, cobertura_percentual=int(cobertura_percentual)))


def cadastrar_sinistros(sinistros_dados):
    for sinistro_dado in sinistros_dados:
        sinistro = Sinistro(numero=sinistro_dado['numero'], cliente=sinistro_dado['cliente'], telefone=sinistro_dado['telefone'])
        inserir_sinistro(sinistro)
        for peca_dado in sinistro_dado['pecas']:
            codigo, nome, categoria, preco, tipo, extra, mao_obra_própria = peca_dado
            if tipo in ('suspensão', 'direção', 'motor'):
                sinistro.inserir_peca(
                    PeçaMecânica(
                        código=int(codigo),
                        nome=nome,
                        categoria=categoria,
                        preco=float(preco),
                        tipo=tipo,
                        dias_garantia=extra,
                        mão_obra_própria=mao_obra_própria == 'True',
                    )
                )
            else:
                sinistro.inserir_peca(
                    PeçaLataria(
                        código=int(codigo),
                        nome=nome,
                        categoria=categoria,
                        preco=float(preco),
                        tipo=tipo,
                        cor=extra,
                        mão_obra_própria=mao_obra_própria == 'True',
                    )
                )


def cadastrar_orcamentos(orcamentos_dados):
    for numero_sinistro, nome_seguradora, data_str in orcamentos_dados:
        dia, mes, ano = [int(parte) for parte in data_str.split('/')]
        nome_resolvido = resolver_nome_seguradora(nome_seguradora)
        criar_orçamento(numero_sinistro=numero_sinistro, nome_seguradora=nome_resolvido, data=Data(dia=dia, mês=mes, ano=ano))


def resolver_nome_seguradora(nome_seguradora):
    seguradoras = get_seguradoras()
    if nome_seguradora in seguradoras:
        return nome_seguradora

    se_nome_sem_sufixo = nome_seguradora.removesuffix(' Seguros')
    if se_nome_sem_sufixo in seguradoras:
        return se_nome_sem_sufixo

    nome_com_sufixo = nome_seguradora if nome_seguradora.endswith(' Seguros') else nome_seguradora + ' Seguros'
    if nome_com_sufixo in seguradoras:
        return nome_com_sufixo

    return nome_seguradora


def salvar_binario():
    ARQUIVO_BIN.parent.mkdir(parents=True, exist_ok=True)
    with ARQUIVO_BIN.open('wb') as arquivo:
        pickle.dump([get_seguradoras(), get_sinistros(), get_orçamentos()], arquivo)


def main():
    seguradoras_dados, sinistros_dados, orcamentos_dados = ler_dados_txt()
    limpar_conjuntos_globais()
    cadastrar_seguradoras(seguradoras_dados)
    cadastrar_sinistros(sinistros_dados)
    cadastrar_orcamentos(orcamentos_dados)
    salvar_binario()
    print(f'Dados gravados em {ARQUIVO_BIN}')


if __name__ == '__main__':
    main()
