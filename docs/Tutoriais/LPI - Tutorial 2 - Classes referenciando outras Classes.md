# Linguagem de Programação I - Tutorial 2

# Classes Referenciando Outras Classes

## 1. Classes Referenciando Outras Classes

No Tutorial 1 foram apresentadas as classes independentes:

- AgênciaPublicidade
- Veículo

Neste tutorial são introduzidas classes que mantêm referências para objetos de outras classes:

- Montadora (relacionamento múltiplo)
- Lançamento (entidade de associação)

---

# 1.1 Entidade de Relacionamento Múltiplo

## Módulo `montadora`

```python
montadoras = {}

def get_montadoras():
    return montadoras

def inserir_montadora(montadora):
    nome_montadora = montadora.nome

    if nome_montadora not in montadoras.keys():
        montadoras[nome_montadora] = montadora
        return True
    else:
        print(
            'Montadora ' +
            nome_montadora +
            ' já tem cadastro'
        )
        return False
```

## Classe Montadora

```python
class Montadora:

    def __init__(
        self,
        nome,
        país_origem,
        sede_maior_fábrica_brasil
    ):
        self.nome = nome
        self.país_origem = país_origem
        self.sede_maior_fábrica_brasil = (
            sede_maior_fábrica_brasil
        )

        self.veículos = {}

    def __str__(self):

        formato = (
            '{} {:<20} {} {:<14} {} {:<17} {}'
        )

        return formato.format(
            '|',
            self.nome,
            '|',
            self.país_origem,
            '|',
            self.sede_maior_fábrica_brasil,
            '|'
        )

    def inserir_veículo(self, veículo):

        marca_modelo = veículo.marca_modelo

        if marca_modelo not in self.veículos.keys():
            self.veículos[marca_modelo] = veículo
        else:
            print(
                'Veículo ' +
                marca_modelo +
                ' já tem cadastro na Montadora'
            )
```

---

## Utilização de Dicionários

Os objetos são armazenados em dicionários porque:

- cada objeto possui uma chave única;
- a recuperação é rápida;
- permite verificar duplicidade facilmente.

Exemplo:

```python
montadoras[nome_montadora] = montadora
```

Obtendo apenas os objetos:

```python
get_montadoras().values()
```

Obtendo apenas as chaves:

```python
get_montadoras().keys()
```

---

## Relacionamento [1:N]

No projeto de referência:

```text
Montadora 1 ------ N Veículo
```

Um veículo pertence a apenas uma montadora.

Por isso os veículos são armazenados dentro do objeto `Montadora`.

---

## Atualização da Classe AgênciaPublicidade

```python
agências_publicidade = {}

def inserir_agência_publicidade(
    agência_publicidade
):
    nome = agência_publicidade.nome

    if nome not in agências_publicidade.keys():
        agências_publicidade[nome] = agência_publicidade
        return True
    else:
        print(
            'Agência de Publicidade ' +
            nome +
            ' já tem cadastro'
        )
        return False
```

---

## Exemplo de Relacionamento [N:N]

Exemplo:

```text
Filme N ------ N Ator
```

Nesse caso o ator pode participar de vários filmes.

```python
def inserir_atores(self, nomes_atores):

    for nome_ator in nomes_atores:

        if nome_ator in get_atores().keys():
            self.atores[nome_ator] = (
                get_atores()[nome_ator]
            )
        else:
            print(
                'Ator ' +
                nome_ator +
                ' não tem cadastro'
            )
```

---

# 1.2 Entidade de Associação

## Classe Lançamento

Representa:

- uma montadora;
- uma agência de publicidade;
- uma data.

```python
from entidades.agência_publicidade import (
    get_agências_publicidade
)

from entidades.montadora import (
    get_montadoras
)

lançamentos = []

def get_lançamentos():
    return lançamentos
```

---

## Inserção de Lançamentos

```python
def inserir_lançamento(lançamento):

    if lançamento not in lançamentos:
        lançamentos.append(lançamento)
    else:
        print(
            'Lançamento já cadastrado'
        )
```

---

## Criação de Lançamentos

```python
def criar_lançamento(
    nome_montadora,
    nome_agência_publicidade,
    data
):

    montadora = get_montadoras()[
        nome_montadora
    ]

    agência_publicidade = (
        get_agências_publicidade()[
            nome_agência_publicidade
        ]
    )

    lançamento = Lançamento(
        montadora,
        agência_publicidade,
        data
    )

    lançamentos.append(lançamento)
```

---

## Classe Lançamento

```python
class Lançamento:

    def __init__(
        self,
        montadora,
        agência_publicidade,
        data
    ):
        self.montadora = montadora
        self.agência_publicidade = (
            agência_publicidade
        )
        self.data = data
```

---

## Método `__str__`

```python
def __str__(self):

    formato = (
        '{} {:<20} {} {:<10} {} {:<10} {}'
    )

    return formato.format(
        '|',
        self.montadora.nome,
        '|',
        self.agência_publicidade.nome,
        '|',
        str(self.data),
        '|'
    )
```

---

# Filtragem de Lançamentos

## Assinatura

```python
def selecionar_lançamentos(
    data_mínima_lançamento=None,
    potência_mínima_veículo=None,
    ranking_máximo_avaliação_agência_publicidade=None,
    país_origem_montadora=None
):
```

## Filtros disponíveis

- Data mínima do lançamento
- Potência mínima dos veículos
- Ranking máximo da agência
- País de origem da montadora

---

## Exemplo de filtro por potência

```python
for veículo in lançamento.montadora.veículos.values():

    if (
        potência_mínima_veículo is not None
        and veículo.potência
        < potência_mínima_veículo
    ):
        excluir_lançamento = True
        break
```

Todos os veículos da montadora precisam satisfazer o filtro.

---

## Método `str_filtro`

Utilizado para exibir:

- ranking da agência;
- país da montadora;
- potência dos veículos.

```python
def str_filtro(self):

    formato = (
        '{:>2} {} {:<14} {} {:<15} {}'
    )

    filtro_formatado = formato.format(
        self.agência_publicidade.ranking_avaliação,
        '|',
        self.montadora.país_origem,
        '|',
        self.str_atributos_veículos(),
        '|'
    )

    return self.__str__() + filtro_formatado
```

---

# 2. Controle do Projeto

## Cadastro de Montadoras

```python
def cadastrar_montadoras():

    montadora = Montadora(
        'Hyundai',
        'Coréia do Sul',
        'Piracicaba - SP'
    )

    inserir_montadora(montadora)

    montadora.inserir_veículo(
        Veículo(
            'Hyundai HB20',
            'flex',
            80,
            False
        )
    )
```

Outras montadoras cadastradas:

- Hyundai
- GM
- Fiat
- BYD
- Volvo
- Volvo Caminhões
- Volkswagen Caminhões
- DAF

---

## Cadastro de Lançamentos

```python
def cadastrar_lançamentos():

    criar_lançamento(
        'Hyundai',
        'Africa',
        Data(1, 9, 2012)
    )

    criar_lançamento(
        'GM',
        'McCann',
        Data(12, 9, 2019)
    )
```

---

## Corpo Principal

```python
if __name__ == '__main__':

    cadastrar_agências_publicidade()

    cadastrar_montadoras()

    cadastrar_lançamentos()

    filtros, lançamentos = (
        selecionar_lançamentos()
    )
```

Responsável por:

1. cadastrar agências;
2. cadastrar montadoras;
3. cadastrar veículos;
4. cadastrar lançamentos;
5. executar filtros;
6. imprimir resultados.

---

# Estruturas de Dados Genéricas

## Linguagens com Tipagem Estática

Exemplos:

- Java
- C++

Necessitam declarar o tipo antecipadamente:

```java
List<Veiculo> veiculos;
```

---

## Python e Tipagem Dinâmica

Em Python:

```python
veiculos = []
```

O tipo é inferido automaticamente.

Vantagens:

- menos código;
- maior flexibilidade;
- listas e dicionários podem armazenar objetos de diferentes classes.

---

# Conclusão

Nesta etapa foram introduzidos:

- relacionamentos entre classes;
- uso de dicionários como repositórios de objetos;
- relacionamento múltiplo;
- entidade de associação;
- filtragem utilizando atributos de várias entidades;
- conceitos de tipagem dinâmica em Python.

Ao final deste tutorial está concluída a **Etapa 2 do projeto de referência**.