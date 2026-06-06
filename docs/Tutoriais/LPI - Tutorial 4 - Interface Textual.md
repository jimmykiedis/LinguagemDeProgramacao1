````markdown
# Linguagem de Programação I - Tutorial 5
## Interface Textual

---

# 1. Persistência de Objetos em Arquivos e Tratamento de Exceção

Nos três tutoriais anteriores, os atributos dos objetos eram gerados na própria implementação.

Neste tutorial, vamos implementar uma aplicação na qual os objetos serão criados a partir da leitura de seus atributos, utilizando uma interface textual. À medida que os atributos forem sendo lidos, os objetos serão criados e armazenados.

Para evitar a perda dos dados ao encerrar a aplicação, os objetos serão persistidos em arquivo antes do encerramento e recuperados no início da execução.

Com a biblioteca `pickle`, é possível armazenar e recuperar conjuntos de objetos de forma simples.

## Módulo `persistência_arquivo`

```python
import pickle

def salvar_arquivo(nome_arquivo, objetos):
    arquivo = open('../../dados/' + nome_arquivo + '.bin', 'wb')
    pickle.dump(objetos, arquivo)
    arquivo.close()

def carregar_arquivo(nome_arquivo):
    try:
        arquivo = open('../../dados/' + nome_arquivo + '.bin', 'rb')
        objetos = pickle.load(arquivo)
    except IOError:
        objetos = None

    return objetos
````

### Função `salvar_arquivo`

Responsável por salvar um conjunto de objetos em um arquivo binário (`.bin`).

* `'wb'` → write binary
* `pickle.dump()` → grava os objetos no arquivo

### Função `carregar_arquivo`

Responsável por recuperar os objetos previamente armazenados.

* `'rb'` → read binary
* `pickle.load()` → carrega os objetos do arquivo
* Utiliza tratamento de exceções para evitar falhas caso o arquivo não exista.

---

## Exceções

Uma exceção é uma situação que pode interromper a execução normal da aplicação.

Exemplos:

* Divisão por zero.
* Acesso a arquivo inexistente.

Estrutura básica:

```python
try:
    # código que pode gerar exceção
except IOError:
    # tratamento da exceção
```

---

# 2. Interface Textual

Módulo:

```python
from util.gerais import (
    imprimir_objetos,
    imprimir_objeto,
    imprimir_objetos_internos,
    imprimir_objetos_associação_filtros
)

from util.data import converte_str_para_data

from entidades.montadora import (
    Montadora,
    inserir_montadora,
    get_montadoras
)

from entidades.agência_publicidade import (
    AgênciaPublicidade,
    inserir_agência_publicidade,
    get_agências_publicidade
)

from entidades.veículo import Carro, Caminhão

from entidades.lançamento import (
    Lançamento,
    filtrar_lançamentos,
    get_lançamentos,
    criar_lançamento,
    inserir_lançamento
)
```

## Função principal de execução

```python
def loop_opções_execução():
    ...
```

Responsável por controlar:

* Cadastro de Agências de Publicidade
* Cadastro de Montadoras
* Cadastro de Lançamentos
* Impressão de objetos
* Seleção de lançamentos por filtros

```

Posso também :contentReference[oaicite:0]{index=0}, pronto para usar no VS Code, GitHub ou Obsidian.
```
