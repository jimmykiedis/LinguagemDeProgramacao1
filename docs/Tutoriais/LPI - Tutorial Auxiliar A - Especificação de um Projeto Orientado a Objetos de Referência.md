# Linguagem de Programação I – Tutorial Auxiliar A

# Especificação de um Projeto Orientado a Objetos de Referência

---

# 1. Mapeando Entidades do Mundo Real

Uma entidade na computação representa algo do mundo real que faz parte do escopo de um projeto.

## Exemplos

### Clínica Médica

Entidades:

- Paciente
- Médico
- Consulta

### Manutenção Informática

Entidades:

- Cliente
- Equipamento
- OrdemServico

### Loja de Calçados

Entidades:

- Cliente
- Calçado
- Venda

---

## Entidade → Classe

No paradigma orientado a objetos, cada entidade é mapeada para uma classe.

Exemplo:

```text
Cliente
```

Atributos:

- nome
- cpf
- email
- telefone
- sexo
- estado_civil

Objetos possíveis:

```text
cliente1
cliente2
cliente3
...
clienteN
```

Cada objeto possui valores próprios para seus atributos.

---

## Convenção de Nomes

### Entidade simples

```text
Cliente
Paciente
Veículo
```

### Entidade composta

```text
LojaCalçados
AgênciaPublicidade
OrdemServico
```

Regra:

- primeira letra de cada palavra em maiúsculo;
- sem espaços.

---

# Tipos de Relacionamentos

## Entidades sem referência

Possuem apenas atributos.

Exemplos:

- Veículo
- AgênciaPublicidade

---

## Relacionamento Múltiplo

Uma entidade incorpora várias instâncias de outra entidade.

### Exemplo 1

```text
Casa [1:N] Quarto
```

- uma casa possui vários quartos;
- um quarto pertence a uma única casa.

### Exemplo 2

```text
Montadora [1:N] Veículo
```

- uma montadora produz vários veículos;
- um veículo pertence a uma única montadora.

---

## Relacionamento Muitos para Muitos

### Exemplo

```text
Filme [N:N] Ator
```

- um filme possui vários atores;
- um ator participa de vários filmes.

Outro exemplo:

```text
Projeto [N:N] Implementador
```

- um projeto possui vários implementadores;
- um implementador participa de vários projetos.

---

## Associação

Associa duas ou mais entidades.

### Exemplos

```text
Venda
Cliente → Produto
```

```text
Aluguel
Cliente → Imóvel
```

```text
Agendamento
Paciente → Médico → Cirurgia
```

---

## Herança

Especialização de uma entidade mais genérica.

### Exemplo

```text
Veículo
├── Carro
├── Moto
└── Caminhão
```

### Outro exemplo

```text
Calçado
├── Sapato
├── Tênis
└── Sandália
```

---

## Estratégia para Relacionamentos N:N

Todo relacionamento N:N pode ser transformado em dois relacionamentos 1:N.

Exemplo:

```text
Filme [N:N] Ator
```

equivale a:

```text
Filme [1:N] Ator

Ator [1:N] Filme
```

Na implementação, normalmente escolhe-se apenas um lado para manter as referências.

Exemplo:

```text
Filme → atores
```

e quando necessário:

```text
Ator → filmes
```

é obtido por pesquisa.

---

# 2. Entidades do Projeto de Referência

## Tema

```text
Divulgação de Lançamentos de Veículos
```

---

## Entidades sem Referência

### AgênciaPublicidade

Atributos:

- nome
- país_origem
- ranking_avaliação

### Veículo

Atributos:

- marca_modelo
- alimentação
- potência
- importado

---

## Relacionamento Múltiplo

```text
Montadora [1:N] Veículo
```

Uma montadora produz vários veículos.

---

## Associação

```text
Lançamento
```

Relaciona:

- Veículo
- Montadora
- AgênciaPublicidade

---

## Herança

```text
Veículo
├── Carro
└── Caminhão
```

---

## Regra da Herança

Correta:

```text
Carro é um tipo de Veículo
```

Incorreta:

```text
Motor é um tipo de Veículo
```

---

# Identificadores

Toda entidade deve possuir uma chave única.

## Exemplos

### Cliente

```text
CPF
```

### Veículo

```text
placa
```

ou

```text
marca_modelo
```

(dependendo do contexto)

### Livro

```text
ISBN
```

---

# 3. Modelo para Projetos Individuais

Os projetos dos alunos devem conter:

- uma entidade sem relacionamento;
- um relacionamento múltiplo;
- uma entidade associadora;
- uma hierarquia de herança.

---

## Regras

### Relacionamento Múltiplo

Utilizar apenas um:

```text
1:N
```

ou

```text
N:N
```

---

### Entidade Associadora

Deve associar apenas duas entidades.

Uma delas:

```text
entidade principal
```

A outra:

```text
entidade sem relacionamento
```

---

### Referências

Relacionamento múltiplo:

```text
veículos
```

(no plural)

Associação:

```text
montadora
veículo
agência_publicidade
```

(no singular)

---

# Modelo de Projeto

## Título

```text
Divulgação de Lançamentos de Veículos
```

---

## Relacionamentos

### Sem Relacionamentos

- AgênciaPublicidade
- Veículo

### Relacionamento Múltiplo

```text
Montadora [1:N] Veículo
```

### Associação

```text
Lançamento
```

### Herança

```text
Veículo
├── Carro
└── Caminhão
```

---

## Atributos

### AgênciaPublicidade

- nome
- país_origem
- ranking_avaliação

### Veículo

- marca_modelo
- alimentação
- potência
- importado

### Carro

- tipo
- volume_carga

### Caminhão

- tração
- capacidade_carga

### Montadora

- nome
- país_origem
- sede_maior_fábrica_brasil
- veículos

### Lançamento

- montadora
- veículo
- agência_publicidade
- data

---

## Enumerados

### alimentação

```text
flex
diesel
elétrico
```

### tipo

```text
passeio
utilitário
caminhonete
```

### tração

```text
6x4
6x2
4x4
```

---

# 4. Etapas do Projeto

# Etapa 1

## Cadastros

### AgênciaPublicidade

| Nome | País | Ranking |
|--------|--------|--------|
| BETC Havas | França | 1 |
| Galeria | Brasil | 2 |
| Artplan | Brasil | 3 |
| McCann | Estados Unidos | 4 |
| Africa | Estados Unidos | 5 |

---

### Veículo

| Modelo | Alimentação | Potência | Importado |
|----------|----------|----------|----------|
| Hyundai HB20 | flex | 80 | False |
| Chevrolet Onix Plus | flex | 116 | False |
| Fiat Strada | diesel | 130 | False |
| Fiat Toro | diesel | 185 | False |
| BYD Dolphin | elétrico | 95 | True |
| Volvo XC40 | elétrico | 231 | True |
| Volvo FH 540 | diesel | 540 | False |
| VW Delivery 11180 | diesel | 175 | False |
| DAF XF 530 | diesel | 530 | False |
| Volvo FH 460 | diesel | 460 | False |

---

## Filtros

### AgênciaPublicidade

```python
ranking_máximo_avaliação = 3
```

```python
país_origem = 'Brasil'
```

```python
prefixo_nome = 'A'
```

### Veículo

```python
importado = False
```

```python
alimentação = 'diesel'
```

```python
potência_máxima = 200
```

---

# Etapa 2

## Cadastros

### Montadora

- Hyundai
- GM
- Fiat
- BYD
- Volvo
- Volvo Caminhões
- Volkswagen Caminhões
- DAF

Relacionadas aos seus respectivos veículos.

---

### Lançamento

Relaciona:

```text
Montadora
+
Veículo
+
AgênciaPublicidade
+
Data
```

Exemplo:

```python
(
    'Hyundai',
    'Hyundai HB20',
    'Africa',
    Data(1, 9, 2012)
)
```

---

## Filtros

```python
data_mínima_lançamento = Data(1,1,2012)
```

```python
ranking_máximo_avaliação_agência_publicidade = 3
```

```python
alimentação_veículo = 'diesel'
```

```python
país_origem_montadora = 'Suécia'
```

---

# Etapa 3

## Carro

Atributos adicionais:

- tipo
- volume_carga

Exemplos:

```text
Hyundai HB20
Chevrolet Onix Plus
Fiat Strada
Fiat Toro
BYD Dolphin
Volvo XC40
```

---

## Caminhão

Atributos adicionais:

- tração
- capacidade_carga

Exemplos:

```text
Volvo FH 540
VW Delivery 11180
DAF XF 530
Volvo FH 460
```

---

## Filtros

```python
data_mínima_lançamento = Data(1,1,2012)
```

```python
potência_mínima_veículo = 150
```

```python
tipo_carro = 'passeio'
```

```python
capacidade_mínima_carga_caminhão = 200
```

```python
ranking_máximo_avaliação_agência_publicidade = 3
```

```python
país_origem_montadora = 'Suécia'
```

---

# Resumo dos Conceitos

Ao final deste tutorial auxiliar, os conceitos apresentados foram:

- Entidades
- Classes
- Objetos
- Atributos
- Identificadores
- Relacionamentos 1:N
- Relacionamentos N:N
- Associação
- Herança
- Enumerados
- Entidades de referência
- Estruturação de projetos orientados a objetos
- Planejamento das etapas de implementação