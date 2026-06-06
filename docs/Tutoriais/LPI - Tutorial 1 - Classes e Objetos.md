# Linguagem de Programação I - Tutorial 1

# Classes e Objetos

## 1. Introdução

A Programação Orientada a Objetos (POO) possui duas características fundamentais:

1. Mapeamento de entidades do mundo real em unidades de programação (classes).
2. Reutilização de código através de herança e abstração.

Python é uma linguagem orientada a objetos com:

- Independência de plataforma;
- Gerenciamento automático de memória;
- Tipagem dinâmica;
- Grande biblioteca padrão;
- Forte utilização em Ciência de Dados e Inteligência Artificial.

---

# 2. Configuração do Ambiente

## Instalar Python

Baixe a versão estável mais recente em:

https://www.python.org

## Instalar PyCharm Community

Baixe em:

https://www.jetbrains.com/pt-br/pycharm/

---

## Criando o Projeto

Criar projeto:

```text
File → New Project
```

Nome sugerido:

```text
MP-E1
```

Estrutura inicial:

```text
MP-E1/
└── src/
    └── main.py
```

Marque o diretório `src` como:

```text
Mark Directory as → Source Root
```

---

## Primeiro Programa

```python
def imprimir(linguagem_programação):
    print(
        f'Vamos aprender a programar na linguagem '
        f'{linguagem_programação}.'
    )

if __name__ == '__main__':
    imprimir('Python')
```

Saída:

```text
Vamos aprender a programar na linguagem Python.
```

---

# 3. Conceitos Básicos

## Blocos de Código

Em Python os blocos são definidos por indentação.

Exemplo:

```python
if condição:
    comando()
```

Não são utilizadas chaves `{}`.

---

## Variável Especial `__name__`

```python
if __name__ == '__main__':
    imprimir('Python')
```

Indica o ponto de entrada da aplicação.

---

## Tipagem Dinâmica

Python infere automaticamente os tipos.

```python
disciplina = 'Programação'
carga_horária = 72
nota_mínima = 6.0
obrigatória = True
```

Tipos básicos:

| Tipo | Exemplo |
|--------|----------|
| str | `"Python"` |
| int | `10` |
| float | `7.5` |
| bool | `True` |

---

# 4. Classes e Objetos

## Classe Veículo

```python
class Veículo:

    def __init__(
        self,
        marca_modelo,
        alimentação,
        potência,
        importado
    ):
        self.marca_modelo = marca_modelo

        self.alimentação = (
            alimentação
            if alimentação in (
                'flex',
                'diesel',
                'elétrico'
            )
            else 'indefinida'
        )

        self.potência = potência
        self.importado = importado
```

---

## Construtor

O método:

```python
__init__()
```

é executado quando um objeto é criado.

Exemplo:

```python
veículo = Veículo(
    'Fiat Toro',
    'diesel',
    185,
    False
)
```

---

## Palavra-chave `self`

Representa o próprio objeto.

```python
self.marca_modelo
self.potência
```

---

## Operador Condicional

```python
self.alimentação = (
    alimentação
    if alimentação in (
        'flex',
        'diesel',
        'elétrico'
    )
    else 'indefinida'
)
```

---

# Classe AgênciaPublicidade

```python
class AgênciaPublicidade:

    def __init__(
        self,
        nome,
        país_origem,
        ranking_avaliação
    ):
        self.nome = nome
        self.país_origem = país_origem
        self.ranking_avaliação = ranking_avaliação
```

---

# 5. Classe Auxiliar Data

```python
from datetime import date

class Data:

    def __init__(
        self,
        dia,
        mês,
        ano
    ):
        self.dia = dia
        self.mês = mês
        self.ano = ano
```

---

## Método `__str__`

```python
def __str__(self):

    if self.dia < 10:
        data_str = '0' + str(self.dia)
    else:
        data_str = str(self.dia)

    if self.mês < 10:
        data_str += '/0' + str(self.mês)
    else:
        data_str += '/' + str(self.mês)

    data_str += '/' + str(self.ano)

    return data_str
```

Exemplo:

```python
Data(1, 9, 2024)
```

Resultado:

```text
01/09/2024
```

---

## Comparação de Datas

Métodos especiais:

```python
__eq__()   # ==
__ne__()   # !=
__gt__()   # >
__lt__()   # <
__ge__()   # >=
__le__()   # <=
```

Permitem:

```python
if data1 > data2:
    ...
```

---

## Calcular Idade

```python
def calcular_idade(
    self,
    data_referência=None
):
```

Calcula idade com base na data atual ou em uma data informada.

---

# 6. Método `__str__`

## Classe Veículo

```python
def __str__(self):

    if self.importado:
        importado_str = 'importado |'
    else:
        importado_str = ''

    formato = (
        '{} {:<19} {} {:<8} {} {:<6} {} {}'
    )

    return formato.format(
        '|',
        self.marca_modelo,
        '|',
        self.alimentação,
        '|',
        f'{self.potência:3d} cv',
        '|',
        importado_str
    )
```

---

## Classe AgênciaPublicidade

```python
def __str__(self):

    formato = (
        '{} {:<10} {} {:<14} {} {:<1} {}'
    )

    return formato.format(
        '|',
        self.nome,
        '|',
        self.país_origem,
        '|',
        str(self.ranking_avaliação),
        '|'
    )
```

---

# 7. Armazenando Objetos

## Lista de Veículos

```python
veículos = []
```

Funções auxiliares:

```python
def get_veículos():
    return veículos

def inserir_veículo(veículo):
    veículos.append(veículo)
```

---

## Lista de Agências

```python
agências_publicidade = []
```

```python
def get_agências_publicidade():
    return agências_publicidade

def inserir_agência_publicidade(
    agência_publicidade
):
    agências_publicidade.append(
        agência_publicidade
    )
```

---

# 8. Filtragem de Objetos

## Selecionar Veículos

```python
def selecionar_veículos(
    importado=None,
    alimentação=None,
    potência_máxima=None
):
```

Filtros:

- Importado ou nacional;
- Tipo de alimentação;
- Potência máxima.

---

### Exemplo

```python
filtros, veículos = (
    selecionar_veículos(
        False,
        'diesel',
        200
    )
)
```

---

## Selecionar Agências

```python
def selecionar_agências_publicidade(
    ranking_máximo_avaliação=None,
    país_origem=None,
    prefixo_nome=None
)
```

Filtros:

- Ranking máximo;
- País de origem;
- Prefixo do nome.

---

# 9. Controle do Projeto

## Cadastro de Agências

```python
def cadastrar_agências_publicidade():

    inserir_agência_publicidade(
        AgênciaPublicidade(
            'BETC Havas',
            'França',
            1
        )
    )

    inserir_agência_publicidade(
        AgênciaPublicidade(
            'Galeria',
            'Brasil',
            2
        )
    )
```

---

## Cadastro de Veículos

```python
def cadastrar_veículos():

    inserir_veículo(
        Veículo(
            'Hyundai HB20',
            'flex',
            80,
            False
        )
    )

    inserir_veículo(
        Veículo(
            'Volvo XC40',
            'elétrico',
            231,
            True
        )
    )
```

---

## Corpo Principal

```python
if __name__ == '__main__':

    cadastrar_agências_publicidade()

    cadastrar_veículos()

    filtros, veículos = (
        selecionar_veículos()
    )
```

---

# 10. Impressão de Objetos

```python
def imprimir_objetos(
    cabeçalho,
    objetos,
    filtros=None
):

    if filtros is not None:
        print(filtros)

    print(cabeçalho)

    for índice, objeto in enumerate(objetos):
        imprimir_objeto(
            índice,
            str(objeto)
        )
```

---

## Impressão Individual

```python
def imprimir_objeto(
    índice,
    objeto_str
):

    ordem = índice + 1

    print(
        f'{ordem:2d} - {objeto_str}'
    )
```

---

# 11. Encapsulamento

Sem encapsulamento:

```python
agência.país_origem = 'Espanha'
```

Com encapsulamento:

```python
@property
def país_origem(self):
    return self.__país_origem
```

```python
@país_origem.setter
def país_origem(
    self,
    país_origem
):
    self.__país_origem = país_origem
```

---

# 12. Depuração (Debug)

Estratégia simples:

```python
print(objeto)
```

Exemplo:

```python
def inserir_agência_publicidade(
    agência_publicidade
):
    print(
        agência_publicidade
    )

    agências_publicidade.append(
        agência_publicidade
    )
```

Permite verificar:

- parâmetros recebidos;
- objetos criados;
- listas preenchidas;
- fluxo de execução.

---

# Conceitos Aprendidos

- Classes
- Objetos
- Construtores
- Métodos
- Atributos
- Tipagem dinâmica
- Classe auxiliar Data
- Métodos especiais (`__str__`, `__eq__`, etc.)
- Listas de objetos
- Filtragem
- Controle da aplicação
- Encapsulamento
- Depuração

---

## Etapa Concluída

Ao final deste tutorial foram implementadas as entidades:

- Veículo
- AgênciaPublicidade

correspondentes à **Etapa 1 do projeto de referência "Divulgação de Lançamentos de Veículos"**.