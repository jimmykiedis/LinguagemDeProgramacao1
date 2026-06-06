# Linguagem de Programação I - Revisão da Etapa 1

---

# Etapa 1

## Itens Avaliados

- Implementação
- Especificação (`spec`)
- Empacotamento

---

# Implementação

## Estrutura do Projeto

Nome do projeto:

```text
LPI-E1
```

Estrutura:

```text
src/
├── controle/
│   └── projeto.py
├── entidades/
└── util/
```

---

## Arquivo `controle/projeto.py`

### Cadastro de Peças Musicais

```python
cadastrar_peças_musicais()
```

Cadastrar pelo menos **4 objetos**.

Exemplo:

```python
inserir_peça_musical(
    PeçaMusical(
        título='Sonata ao Luar',
        compositor='Beethoven',
        ...
    )
)
```

---

### Cadastro de Maestros

```python
cadastrar_maestros()
```

Mesmo procedimento utilizado para as peças musicais.

---

### Corpo Principal

```python
if __name__ == '__main__':

    print(
        '\nApresentação de Peças Musicais '
        'de um Repertório por um Maestro'
    )

    cadastrar_peças_musicais()

    cabeçalho = (
        'PeçaMusical: '
        'título, compositor, duração, tom'
    )

    imprimir_objetos(
        cabeçalho='\n' + cabeçalho,
        objetos=get_peças_musicais()
    )

    filtros, peças_musicais_selecionadas = (
        selecionar_peças_musicais()
    )

    imprimir_objetos(
        cabeçalho,
        peças_musicais_selecionadas,
        filtros
    )
```

---

### Filtragem

Executar:

1. Sem filtros.
2. Acrescentar o primeiro filtro.
3. Acrescentar o segundo filtro mantendo o primeiro.
4. Acrescentar o terceiro filtro mantendo os anteriores.

Fazer o mesmo para:

```python
selecionar_maestros()
```

---

# Entidades Sem Referências

Arquivos:

```text
entidades/
├── peça_musical.py
└── maestro.py
```

---

## Estrutura da Classe

Cada entidade deve possuir:

- Classe com nome da entidade;
- Método `__init__`;
- Validação dos enumerados;
- Método `__str__`.

---

## Atributos

Cada entidade deve possuir pelo menos:

- um atributo booleano;
- um atributo enumerado;
- um atributo numérico.

---

## Conjunto de Objetos

Criar:

```python
peças_musicais = []
```

ou

```python
maestros = []
```

---

## Funções Obrigatórias

### Obter conjunto

```python
get_peças_musicais()
```

### Inserir objeto

```python
inserir_peça_musical(objeto)
```

Deve utilizar:

```python
append()
```

---

## Seleção com Filtros

```python
selecionar_objetos(
    filtro1=None,
    filtro2=None,
    filtro3=None
)
```

Requisitos:

- pelo menos um filtro booleano;
- pelo menos um filtro numérico.

---

## Filtros Numéricos

Utilizar valores mínimos ou máximos.

Exemplos:

```python
data_mínima
```

```python
potência_máxima
```

```python
anos_experiência_mínimo
```

---

# Diretório `util`

Arquivos:

```text
util/
├── data.py
└── gerais.py
```

---

## Arquivo `data.py`

Utilizar o código apresentado no tutorial.

Implementar:

- `__init__`
- `__str__`
- `calcular_idade()`
- 6 métodos comparadores

Métodos:

```python
__eq__()
__ne__()
__lt__()
__le__()
__gt__()
__ge__()
```

---

## Arquivo `gerais.py`

Implementar:

```python
imprimir_objetos()
```

```python
imprimir_objeto()
```

---

# Execução

Para cada entidade:

- imprimir cadastro completo;
- executar filtragens.

---

## Impressão dos Cadastros

Cabeçalho:

```text
Entidade : colunas
```

Exemplo:

```text
PeçaMusical:
título, compositor, duração, tom
```

---

### Formatação

Regras:

- valores alinhados;
- colunas organizadas;
- largura baseada no maior texto da coluna;
- espaçamento entre colunas de 2 ou 3 caracteres.

---

### Atributos Booleanos

Mostrar apenas quando o valor for verdadeiro.

Exemplo:

```text
estrangeiro
```

para:

```python
estrangeiro = True
```

Não mostrar texto para:

```python
estrangeiro = False
```

---

# Filtragem

A saída deve mostrar:

- filtros utilizados;
- objetos selecionados.

---

## Primeira Filtragem

Sem filtros.

Resultado esperado:

```text
todos os objetos cadastrados
```

---

## Filtragens Posteriores

Adicionar filtros progressivamente:

```text
Filtro 1
Filtro 1 + Filtro 2
Filtro 1 + Filtro 2 + Filtro 3
```

---

## Regras

A cada filtro acrescentado:

- pelo menos um objeto deve ser removido da seleção;
- os filtros anteriores devem permanecer ativos.

Ao final:

```text
deve sobrar pelo menos um objeto
```

---

# espec.pdf

Cabeçalho obrigatório:

```text
Linguagem de Programação I - Etapa 1 - Nome Completo do Aluno
```

Exemplo:

```text
Linguagem de Programação I - Etapa 1 - Alberto Luis da Silva Torres
```

---

## Conteúdo

### Entidades

Informar:

```text
entidade
plural
```

---

### Relacionamentos

Apresentar os quatro tipos:

```text
Sem referência
Relacionamento múltiplo
Associação
Herança
```

---

### Atributos e Referências

Regras:

- entidades com pelo menos 3 atributos;
- associação: mínimo de 1 atributo;
- subclasses: mínimo de 2 atributos.

---

### Identificador

O primeiro atributo deve ser o identificador.

Destacar:

```text
sublinhado
```

Exceções:

- associação;
- subclasses.

---

### Referências

Devem aparecer ao final da entidade em **negrito**.

#### Associação

Duas referências:

```text
singular
```

#### Relacionamento Múltiplo

Uma referência:

```text
plural
```

---

### Enumerados

Definir conjuntos de valores possíveis.

Exemplo:

```text
estilo_música
```

Não utilizar:

```text
True
False
```

como enumerados.

---

## Final do Documento

Adicionar:

```text
Cidade, dd/mm/2026
```

e

```text
Assinatura
```

Assinatura:

- gov.br (preferencialmente);
- ou nome completo em letra cursiva legível.

---

# Empacotamento

## Nome do Arquivo ZIP

```text
LPI - Etapa 1 - Nome Completo do Aluno
```

Exemplo:

```text
LPI - Etapa 1 - Alberto Luis da Silva Torres
```

---

## Conteúdo

```text
src/
espec.pdf
fontes.pdf
```

---

### Diretório `src`

Remover:

```text
__pycache__
```

---

## fontes.pdf

Cabeçalho:

```text
Linguagem de Programação I - Etapa 1 - Nome Completo do Aluno
```

---

### Caminhos dos Arquivos

Exemplo:

```text
$$$ src.controle.projeto

$$$ src.entidades.maestro

$$$ src.entidades.peça_musical

$$$ src.util.data

$$$ src.util.gerais
```

---

### Conteúdo

Após cada caminho:

1. Copiar todo o código fonte.
2. Colar no PDF.
3. Iniciar nova página para o próximo arquivo.

---

### Final do PDF

Adicionar:

```text
Cidade, dd/mm/2026
```

```text
Assinatura
```

---

# Teste de Empacotamento

Antes da entrega, validar o arquivo ZIP utilizando:

```text
teste-empacotamento-etapas.squareweb.app
```