# Linguagem de Programação I - Check List da Etapa 4

---

# 1. Empacotamento

> A Etapa 4 será entregue junto com a Prova 2 e será considerada inválida (nota zero) caso não siga rigorosamente os procedimentos de empacotamento e a metodologia apresentada nos tutoriais.

---

## 1.1 Nome do Diretório Zipado

Utilizar o seguinte padrão:

```text
LPI - Etapa 4 - Nome Completo do Aluno
```

Exemplo:

```text
LPI - Etapa 4 - Alberto Luis da Silva Torres
```

---

## 1.2 Conteúdo do Arquivo ZIP

O arquivo compactado deve conter apenas:

```text
dados/
src/
espec.pdf
fontes.pdf
saida.pdf
```

---

## 1.3 Diretórios para Comprovação da Execução

### Diretório `dados`

Deve conter:

```text
conjuntos_globais.bin
```

### Diretório `src`

Deve conter apenas:

- arquivos `.py`
- estrutura padronizada do projeto

Remover:

```text
__pycache__
```

---

## 1.4 Arquivos PDF Obrigatórios

### Arquivos

```text
espec.pdf
fontes.pdf
saida.pdf
```

---

### 1.4.1 Cabeçalho dos PDFs

Utilizar exatamente:

```text
Linguagem de Programação I - Etapa 4 - Nome Completo do Aluno
```

Verificar que:

- `espec.pdf` possui o cabeçalho correto
- `fontes.pdf` possui o mesmo cabeçalho

---

### 1.4.2 Final dos PDFs

Inserir:

```text
Cidade, dd/mm/aaaa

Assinatura
```

A assinatura pode ser:

- digital (gov.br)
- manuscrita digitalizada

Evitar assinatura feita com mouse.

---

### 1.4.3 Conteúdo do `espec.pdf`

O arquivo deve conter:

- título do projeto
- entidades
- relacionamentos
- atributos
- referências
- enumerados

---

## Exemplo

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
ApresentaçãoMusical
[Repertório, Maestro]
```

#### Herança

```text
PeçaMusical
├── PeçaMusicalClássica
└── PeçaMusicalPopular
```

---

### 1.4.4 Conteúdo do `fontes.pdf`

Incluir todos os arquivos do diretório `src`.

Cada arquivo deve iniciar com:

```text
$$$ src.controle.projeto
```

Exemplos:

```text
$$$ src.controle.projeto
$$$ src.entidades.maestro
$$$ src.entidades.peça_musical
$$$ src.entidades.repertório
$$$ src.util.data
$$$ src.util.gerais
$$$ src.util.persistência_arquivo
```

Regras:

- fonte legível
- fundo branco
- sem capturas de tela
- conteúdo idêntico aos arquivos `.py`

---

### 1.4.5 Conteúdo do `saida.pdf`

Mostrar a saída da segunda execução do sistema.

Deve conter:

- impressão completa dos conjuntos
- impressão do relacionamento múltiplo
- execução de todos os filtros
- resultado após cada filtragem

---

# 2. Definição da Especificação

---

## 2.1 Regras de Nomenclatura

### Entidades

```text
Maestro
PeçaMusical
Repertório
```

### Atributos

```text
anos_experiência
compositor
```

### Referências

```text
maestro
peça_musical
```

---

## 2.2 Chaves

A primeira informação da entidade deve ser sua chave.

Exemplos:

```text
nome
cpf
isbn
```

Exceções:

- entidade associadora
- subclasses

---

## 2.3 Referências

Relacionamento múltiplo:

```text
peças_musicais
```

(plural)

Associação:

```text
repertório
maestro
```

(singular)

---

## 2.4 Quantidade Mínima de Atributos

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

## 2.5 Herança

### Superclasse

Define:

- chave
- atributos comuns

### Subclasses

Definem:

- atributos específicos
- atributos diferentes entre si

---

## 2.6 Enumerados

Devem ser utilizados quando houver poucos valores possíveis.

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

---

# 3. Padronização de Nomes

---

## 3.1 Diretórios e Arquivos

Utilizar:

```text
letras minúsculas
```

Separação:

```text
underscore (_)
```

Exemplos:

```text
controle/
entidades/
util/

peça_musical.py
repertório.py
```

---

## 3.2 Classes

Utilizar:

```text
PascalCase
```

Exemplos:

```python
class Maestro:
class PeçaMusical:
```

---

## 3.3 Variáveis, Métodos e Funções

Utilizar:

```text
snake_case
```

Exemplos:

```python
calcular_idade()
cadastrar_peças_musicais()
```

---

## 3.4 Conjuntos de Objetos

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

Devem ser armazenados em:

```python
{}
```

(dicionários)

Exemplo:

```python
maestros = {}
repertórios = {}
```

---

## 4.2 Entidade Associadora

Deve ser armazenada em:

```python
[]
```

(lista)

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

Os objetos armazenados na superclasse passam a ser objetos das subclasses.

---

# 5. Funcionalidades da Etapa

---

## 5.1 Cadastro via Interface Textual

Cadastrar:

- entidades sem referência
- entidade principal do relacionamento
- entidade associadora
- subclasses

Todos os atributos devem ser lidos pela interface textual.

---

## 5.2 Impressão

A primeira linha deve conter:

```text
Nome da Classe : nomes das colunas
```

Exemplo:

```text
PeçaMusical:
título, compositor, duração, tom
```

---

### Regras

- colunas alinhadas
- evitar espaços excessivos
- largura baseada no maior conteúdo

---

### Booleanos

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

## 5.3 Impressão do Relacionamento Múltiplo

Exemplo:

```text
Repertório:
título, nome, data_montagem

 - PeçaMusical:
   título, compositor, duração, tom
```

---

# 5.2 Filtragem

Os filtros devem ser definidos na entidade associadora.

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
2. Adicionar um filtro.
3. Adicionar outro filtro.
4. Manter filtros anteriores.
5. Garantir redução gradual dos resultados.

---

## Filtros Numéricos

Utilizar:

```text
mínimo
```

ou

```text
máximo
```

Exemplos:

```python
mínimo_anos_experiência
preço_máximo_ingresso
```

---

## Filtros Booleanos

Exemplo:

```python
estrangeiro = True
```

Mostrar:

```text
estrangeiro
```

Exemplo:

```python
estrangeiro = False
```

Mostrar:

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
email
telefone
```

Utilizar:

```python
prefixo_nome
prefixo_telefone
```

---

# 5.3 Interface Textual

Implementar:

- menu principal
- leitura dos objetos
- leitura dos filtros
- criação dos objetos
- validação dos atributos

---

## Leitura das Subclasses

Fluxo:

1. Ler atributos da superclasse.
2. Escolher a subclasse.
3. Ler atributos específicos.

---

# 6. Avaliação

A Etapa 4 receberá nota zero se:

- não seguir o empacotamento;
- não seguir os tutoriais;
- não implementar corretamente as funcionalidades.

---

## Critérios Avaliados

- especificação;
- padronização de nomes;
- armazenamento dos conjuntos;
- implementação correta;
- filtragem;
- interface textual;
- persistência em arquivo;
- execução completa do sistema.