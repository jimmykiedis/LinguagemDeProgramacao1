# Linguagem de Programação I - Check List da Etapa 2

---

# 1. Empacotamento

A Etapa 2 será entregue juntamente com a Prova 1 e será considerada inválida (nota zero) caso não siga rigorosamente os procedimentos de empacotamento e a metodologia apresentada nos tutoriais. :contentReference[oaicite:0]{index=0}

---

## 1.1 Nome do Diretório Zipado

Utilizar o padrão:

```text
LPI - Etapa 2 - Nome Completo do Aluno
```

Exemplo:

```text
LPI - Etapa 2 - Alberto Luis da Silva Torres
```

:contentReference[oaicite:1]{index=1}

---

## 1.2 Conteúdo do Arquivo ZIP

Incluir apenas:

```text
src/
espec.pdf
fontes.pdf
```

:contentReference[oaicite:2]{index=2}

---

## 1.3 Diretório para Comprovação da Execução

### Diretório `src`

Deve conter:

- estrutura padronizada do projeto;
- diretórios definidos nos tutoriais;
- arquivos Python do projeto.

:contentReference[oaicite:3]{index=3}

---

## 1.4 Arquivos PDF Obrigatórios

Arquivos:

```text
espec.pdf
fontes.pdf
```

:contentReference[oaicite:4]{index=4}

---

### 1.4.1 Cabeçalho dos PDFs

Utilizar exatamente:

```text
Linguagem de Programação I - Etapa 2 - Nome Completo do Aluno
```

Verificar que:

- `espec.pdf` contém o cabeçalho correto;
- `fontes.pdf` contém o mesmo cabeçalho.

:contentReference[oaicite:5]{index=5}

---

### 1.4.2 Final dos PDFs

Adicionar:

```text
Cidade, dd/mm/aaaa

Assinatura
```

Regras:

- utilizar a data de envio da etapa;
- verificar se os dois PDFs possuem cidade, data e assinatura;
- preferencialmente utilizar assinatura digital;
- evitar assinatura feita com mouse.

:contentReference[oaicite:6]{index=6}

---

### 1.4.3 Conteúdo do `espec.pdf`

O arquivo deve conter:

- título do projeto;
- entidades;
- relacionamentos;
- atributos;
- referências;
- enumerados.

Além disso:

- utilizar apenas as entidades aprovadas pelo professor;
- existir apenas um relacionamento múltiplo;
- a entidade associadora deve referenciar somente duas entidades.

:contentReference[oaicite:7]{index=7}

---

## Exemplo de Estrutura

### Título

```text
Apresentações de Repertórios Musicais
```

### Entidades

```text
ApresentaçãoMusical
Maestro
PeçaMusical
PeçaMusicalClássica
PeçaMusicalPopular
Repertório
```

### Relacionamentos

#### Sem Referências

```text
PeçaMusical
Maestro
```

#### Relacionamento Múltiplo

```text
Repertório [N:N] PeçaMusical
```

#### Associação

```text
ApresentaçãoMusical [Repertório, Maestro]
```

#### Herança

```text
PeçaMusical
├── PeçaMusicalClássica
└── PeçaMusicalPopular
```

:contentReference[oaicite:8]{index=8}

---

### 1.4.4 Conteúdo do `fontes.pdf`

Deve conter todos os arquivos do diretório `src`.

Antes de cada arquivo incluir:

```text
$$$ controle.projeto
$$$ entidades.apresentação_musical
$$$ entidades.maestro
$$$ entidades.peça_musical
$$$ entidades.repertório
$$$ util.data
$$$ util.gerais
```

Regras:

- utilizar somente texto;
- fonte legível;
- fundo branco;
- mesma ordem dos arquivos do projeto.

:contentReference[oaicite:9]{index=9}

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

:contentReference[oaicite:10]{index=10}

---

## Chaves

Com exceção:

- da entidade associadora;
- das subclasses;

o primeiro atributo deve ser a chave identificadora da entidade.

:contentReference[oaicite:11]{index=11}

---

## Referências

### Relacionamento Múltiplo

Deve ser:

```text
plural
```

Exemplo:

```text
peças_musicais
```

### Associação

Devem ser:

```text
singular
```

Exemplo:

```text
repertório
maestro
```

:contentReference[oaicite:12]{index=12}

---

## Quantidade Mínima de Atributos

### Entidade Associadora

```text
mínimo 1 atributo
```

### Superclasse

```text
mínimo 2 atributos
```

### Subclasses

```text
mínimo 2 atributos específicos
```

### Demais Entidades

```text
mínimo 3 atributos
```

:contentReference[oaicite:13]{index=13}

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

:contentReference[oaicite:14]{index=14}

---

## Regras para Atributos

- devem ser relevantes para o projeto;
- não devem repetir o nome da entidade;
- podem representar entidades não modeladas;
- atributos com poucos valores possíveis devem ser enumerados.

Exemplo:

```text
estilo_música
```

Não utilizar enumerados para:

```text
True
False
```

:contentReference[oaicite:15]{index=15}

---

## Exemplo de Atributos

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

:contentReference[oaicite:16]{index=16}

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

:contentReference[oaicite:17]{index=17}

---

# 3. Padronização de Nomes

## Diretórios e Arquivos

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

:contentReference[oaicite:18]{index=18}

---

## Classes

Utilizar PascalCase:

```python
class Maestro:
class PeçaMusical:
```

:contentReference[oaicite:19]{index=19}

---

## Variáveis, Métodos e Funções

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

:contentReference[oaicite:20]{index=20}

---

## Conjuntos e Funções Relacionadas

```python
peças_musicais = {}

get_peças_musicais()

inserir_peça_musical()
```

:contentReference[oaicite:21]{index=21}

---

# 4. Armazenamento dos Objetos

## Conjuntos Globais

Armazenar em:

```python
{}
```

Exemplos:

```python
maestros = {}
repertórios = {}
```

:contentReference[oaicite:22]{index=22}

---

## Entidade Associadora

Armazenar em:

```python
[]
```

Exemplo:

```python
apresentações_musicais = []
```

:contentReference[oaicite:23]{index=23}

---

## Relacionamento N:N

Utilizar dicionário local:

```python
self.peças_musicais = {}
```

Mantendo também o conjunto global da entidade secundária.

:contentReference[oaicite:24]{index=24}

---

## Relacionamento 1:N

Utilizar:

```python
self.veículos = {}
```

Nesse caso:

```text
não existe conjunto global da entidade secundária
```

:contentReference[oaicite:25]{index=25}

---

# 5. Funcionalidades da Etapa

Seguir a metodologia do Tutorial 2.

:contentReference[oaicite:26]{index=26}

---

## Cadastro e Impressão

Cadastrar:

- entidades sem referência;
- entidade principal do relacionamento múltiplo;
- entidade associadora.

Validar enumerados no `__init__`.

:contentReference[oaicite:27]{index=27}

---

## Impressão

Primeira linha:

```text
NomeDaClasse : colunas
```

Exemplo:

```text
PeçaMusical : título, compositor, duração, tom
```

Regras:

- colunas alinhadas;
- sem espaços excessivos;
- largura baseada no maior conteúdo.

:contentReference[oaicite:28]{index=28}

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

:contentReference[oaicite:29]{index=29}

---

## Relacionamento Múltiplo

Exemplo:

```text
Repertório : título, nome, data_montagem, mesmo_compositor
 - PeçaMusical : título, compositor, duração, tom
```

Imprimir:

- objeto principal;
- objetos secundários relacionados.

:contentReference[oaicite:30]{index=30}

---

# 5.2 Filtragem

Os filtros são definidos na entidade associadora.

Deve existir um filtro para cada classe (exceto subclasses).

Exemplos:

```python
data_mínima_apresentação_musical
compositor_peça_musical
prefixo_nome_maestro
mesmo_compositor_repertório
```

:contentReference[oaicite:31]{index=31}

---

## Processo de Filtragem

1. Sem filtros.
2. Aplicar um filtro.
3. Acrescentar outro filtro.
4. Manter os anteriores.
5. Garantir redução gradual dos resultados.

:contentReference[oaicite:32]{index=32}

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

:contentReference[oaicite:33]{index=33}

---

## Filtros Booleanos

```python
estrangeiro = True
```

Mostrar:

```text
estrangeiro
```

```python
estrangeiro = False
```

Mostrar:

```text
não estrangeiro
```

:contentReference[oaicite:34]{index=34}

---

## Não Utilizar como Filtro

Atributos identificadores:

```text
cpf
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

:contentReference[oaicite:35]{index=35}

---

# 6. Avaliação

A Etapa 2 receberá nota zero caso:

- não siga as regras de empacotamento;
- não utilize a metodologia dos tutoriais.

Serão avaliados:

- especificação;
- padronização de nomes;
- armazenamento dos conjuntos;
- cadastro;
- impressão;
- relacionamento múltiplo;
- filtragem.

:contentReference[oaicite:36]{index=36}