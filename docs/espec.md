# Linguagem de Programação I - Etapa 3

**Aluno:** Leonardo Farias de Oliveira

---

# Projeto

## Orçamento de Peças de um Sinistro para uma Seguradora

---

# Entidades

- Sinistro
- Seguradora
- Peça
- PeçaCarro
- PeçaMoto
- Orçamento

### Plural das Entidades

| Entidade | Plural |
|-----------|---------|
| Sinistro | Sinistros |
| Seguradora | Seguradoras |
| Peça | Peças |
| PeçaCarro | PeçasCarro |
| PeçaMoto | PeçasMoto |
| Orçamento | Orçamentos |

---

# Relacionamentos

## Entidades sem Referências

- Seguradora
- Peça

---

## Relacionamento Múltiplo

```text
Sinistro [1:N] Peça
```

Um sinistro pode possuir várias peças associadas.

---

## Associação

```text
Orçamento [Sinistro, Seguradora]
```

Um orçamento relaciona um sinistro a uma seguradora.

---

## Herança

```text
Peça
├── PeçaCarro
└── PeçaMoto
```

---

# Atributos e Referências

## Sinistro

| Atributo | Tipo |
|-----------|--------|
| segurado | atributo |
| data | atributo |
| cidade | atributo |
| peças | referência |

---

## Seguradora

| Atributo | Tipo |
|-----------|--------|
| nome | identificador |
| cidade | atributo |
| cobertura_percentual | atributo |

---

## Peça

| Atributo | Tipo |
|-----------|--------|
| código | identificador |
| nome | atributo |
| marca | atributo |
| preço | atributo |

---

## PeçaCarro

| Atributo | Tipo |
|-----------|--------|
| tipo_peça_carro | atributo |
| categoria_peça | atributo |

---

## PeçaMoto

| Atributo | Tipo |
|-----------|--------|
| tipo_peça_moto | atributo |
| categoria_peça | atributo |

---

## Orçamento

| Atributo | Tipo |
|-----------|--------|
| data | atributo |
| sinistro | referência |
| seguradora | referência |

---

# Enumerados

## tipo_peça_carro

```text
farol
parachoque
capô
lanterna
porta
```

---

## tipo_peça_moto

```text
escapamento
pistão
biela
cabeçote
```

---

## categoria_peça

```text
original
genuína
OEM
```

---

# Resumo da Estrutura

## Relacionamento Múltiplo

```text
Sinistro [1:N] Peça
```

## Associação

```text
Orçamento [Sinistro, Seguradora]
```

## Herança

```text
Peça
├── PeçaCarro
└── PeçaMoto
```