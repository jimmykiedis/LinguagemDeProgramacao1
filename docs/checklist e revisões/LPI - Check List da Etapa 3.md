# Linguagem de Programação I - Check List da Etapa 3

---

# 1. Empacotamento

A Etapa 3 serve para verificar a evolução do projeto antes da Etapa 4 (Prova 2).

---

## 1.1 Nome do Diretório Zipado

Formato obrigatório:

```text
LPI - Etapa 3 - Nome Completo do Aluno
```

Exemplo:

```text
LPI - Etapa 3 - Alberto Luis da Silva Torres
```

---

## 1.2 Conteúdo do Arquivo ZIP

Incluir somente:

```text
src/
espec.pdf
fontes.pdf
```

---

## 1.3 Diretório de Comprovação

### Diretório `src`

Deve conter:

- estrutura padronizada do projeto;
- diretórios obrigatórios;
- arquivos Python.

---

## 1.4 PDFs Obrigatórios

### Arquivos

```text
espec.pdf
fontes.pdf
```

---

### 1.4.1 Cabeçalho

Utilizar:

```text
Linguagem de Programação I - Etapa 3 - Nome Completo do Aluno
```

O mesmo cabeçalho deve aparecer nos dois PDFs.

---

### 1.4.2 Rodapé

Adicionar:

```text
Cidade, dd/mm/aaaa

Assinatura
```

Recomendações:

- utilizar assinatura digital (gov.br) quando possível;
- caso seja manuscrita, digitalizar;
- evitar assinatura feita com mouse.

---

### 1.4.3 Conteúdo do `espec.pdf`

Deve conter:

- título do projeto;
- entidades;
- relacionamentos;
- atributos;
- referências;
- enumerados.

### Exemplo

#### Título

```text
Apresentações de Repertórios Musicais
```

#### Entidades

```text
ApresentaçãoMusical
Maestro
PeçaMusical
PeçaMusicalClássica
PeçaMusicalPopular
Repertório
```

#### Relacionamentos

```text
Sem Referências:
PeçaMusical
Maestro
```

```text
Relacionamento Múltiplo:
Repertório [N:N] PeçaMusical
```

```text
Associação:
ApresentaçãoMusical [Repertório, Maestro]
```

```text
Herança:
PeçaMusical
├── PeçaMusicalClássica
└── PeçaMusicalPopular
```

---

### 1.4.4 Conteúdo do `fontes.pdf`

Deve conter todos os arquivos do diretório `src`.

Antes de cada arquivo incluir:

```text
$$$ src.controle.projeto
```

Exemplos:

```text
$$$ src.controle.projeto
$$$ src.entidades.apresentação_musical
$$$ src.entidades.maestro
$$$ src.entidades.peça_musical
$$$ src.entidades.repertório
$$$ src.util.data
$$$ src.util.gerais
```

Regras:

- fonte legível;
- texto puro (não screenshots);
- fundo branco;
- mesma ordem dos arquivos no projeto.

---

# 2. Definição da Especificação

---

## Regras Gerais

### Nomes

Exemplos:

#### Entidades

```text
Maestro
PeçaMusical
```

#### Atributos

```text
anos_experiência
compositor
```

#### Referências

```text
maestro
peça_musical
```

---

## Chaves

O primeiro atributo da entidade deve ser sua chave.

Exemplos:

```text
nome
cpf
isbn
```

Exceções:

- entidade associadora;
- subclasses (herdam a chave).

---

## Referências

### Relacionamento Múltiplo

Deve estar no plural:

```text
peças_musicais
```

### Associação

Devem estar no singular:

```text
repertório
maestro
```

---

## Quantidade Mínima de Atributos

### Entidade Associadora

Mínimo:

```text
1 atributo
```

### Superclasse

Mínimo:

```text
2 atributos
```

### Subclasses

Mínimo:

```text
2 atributos específicos
```

### Demais Entidades

Mínimo:

```text
3 atributos
```

---

## Herança

### Superclasse

Define:

- chave;
- atributos comuns.

### Subclasses

Definem:

- atributos próprios;
- atributos diferentes entre si.

---

## Enumerados

Utilizar para atributos com poucos valores possíveis.

Exemplo:

```text
estilo_musical
```

Não utilizar para:

```text
True
False
```

---

## Exemplo de Especificação

### ApresentaçãoMusical

```text
data
repertório
maestro
```

### Maestro

```text
nome
anos_experiência
estrangeiro
```

### PeçaMusical

```text
título
compositor
duração
tom
```

### PeçaMusicalClássica

```text
estilo_música_clássica
muito_conhecida
```

### PeçaMusicalPopular

```text
estilo_música_popular
instrumentação_característica
```

### Repertório

```text
título
nome
data_montagem
mesmo_compositor
peças_musicais
```

---

## Enumerados

### estilo_música_clássica

```text
barroco
romântico
clássico
modernismo
```

### estilo_música_popular

```text
pop
rock
country
reggae
blues
jazz
```

### instrumentação_característica

```text
guitarra elétrica
bateria
baixo
teclado
saxofone
violão
trompete
piano
bateria eletrônica
violino
contrabaixo
sintetizador
```

---

# 3. Padronização de Nomes

---

## 3.1 Diretórios e Arquivos

Utilizar:

```text
letras minúsculas
underscore (_)
```

Diretórios:

```text
controle
entidades
util
```

Exemplos:

```text
apresentações_repertórios_musicais.py
maestro.py
peça_musical.py
data.py
gerais.py
```

---

## 3.2 Classes

Utilizar PascalCase:

```python
class Maestro:
class PeçaMusical:
```

---

## 3.3 Variáveis, Métodos e Funções

Utilizar snake_case:

```python
calcular_idade()
cadastrar_peças_musicais()
```

Métodos especiais:

```python
__init__()
__str__()
```

---

## 3.4 Conjuntos e Funções

Entidade:

```text
PeçaMusical
```

Conjunto:

```python
peças_musicais = {}
```

Funções:

```python
get_peças_musicais()
inserir_peça_musical()
```

---

# 4. Armazenamento dos Objetos

---

## 4.1 Conjuntos Globais

Armazenar em dicionários:

```python
{}
```

Exemplo:

```python
maestros = {}
repertórios = {}
```

---

## 4.2 Entidade Associadora

Armazenar em lista:

```python
[]
```

Exemplo:

```python
apresentações_musicais = []
```

---

## 4.3 Relacionamento N:N

A entidade principal mantém um dicionário local.

Exemplo:

```python
self.peças_musicais = {}
```

O dicionário global da entidade secundária continua existindo.

---

## 4.4 Relacionamento 1:N

Exemplo:

```python
self.veículos = {}
```

Nesse caso:

```text
não existe conjunto global da entidade secundária
```

---

## 4.5 Subclasses

Os dicionários da superclasse passam a armazenar objetos das subclasses.

---

# 5. Funcionalidades da Etapa

Seguir a metodologia do Tutorial 3.

---

## 5.1 Cadastro e Impressão

Cadastrar:

- entidades sem referências;
- entidade principal do relacionamento múltiplo;
- entidade associadora;
- subclasses.

---

### Validação de Enumerados

O método `__init__` deve verificar:

```python
if valor in ('opção1', 'opção2'):
```

---

### Cadastro das Subclasses

O cadastro da superclasse deve criar objetos das subclasses.

---

## 5.1.2 Cabeçalho das Impressões

Exemplo:

```text
PeçaMusical:
título, compositor, duração, tom

clássica:
estilo_música_clássica, muito_conhecida

popular:
estilo_música_popular,
instrumentação_característica
```

---

## Regras de Impressão

- colunas alinhadas;
- sem espaços excessivos;
- largura baseada no maior conteúdo.

---

## Booleanos

Mostrar apenas quando forem `True`.

Exemplo:

```text
muito conhecida
```

Não mostrar:

```text
não muito conhecida
```

---

## Relacionamento Múltiplo

Imprimir:

```text
Repertório
```

e abaixo:

```text
PeçaMusical
```

Exemplo:

```text
1 - Mestres da Música Clássica

 - Fuga em Ré Menor
 - Rondo Alla Turca
 - Sonata ao Luar
```

---

# 5.2 Filtragem

Os filtros são definidos na entidade associadora.

---

## Um filtro para cada classe

Exemplo:

```python
data_mínima_apresentação_musical

compositor_peça_musical

prefixo_nome_maestro

mesmo_compositor_repertório

estilo_música_clássica

instrumentação_característica_música_popular
```

---

## Processo de Filtragem

1. Sem filtros.
2. Aplicar primeiro filtro.
3. Aplicar segundo filtro.
4. Manter filtros anteriores.
5. Garantir redução da lista.

---

## Filtros Numéricos

Utilizar:

```python
mínimo_anos_experiência
```

ou

```python
preço_máximo_ingresso
```

---

## Filtros Booleanos

```python
estrangeiro = True
```

Imprimir:

```text
estrangeiro
```

```python
estrangeiro = False
```

Imprimir:

```text
não estrangeiro
```

---

## Não Utilizar como Filtro

Atributos identificadores:

```text
cpf
isbn
nome
título
telefone
email
```

Utilizar:

```python
prefixo_nome
prefixo_telefone
```

---

# 6. Verificação da Etapa 3

Serão avaliados:

- empacotamento;
- especificação;
- padronização de nomes;
- armazenamento dos conjuntos;
- cadastro de objetos;
- impressão;
- herança;
- relacionamento múltiplo;
- filtros.

Somente as funcionalidades que executarem corretamente e estiverem de acordo com a especificação serão consideradas válidas.