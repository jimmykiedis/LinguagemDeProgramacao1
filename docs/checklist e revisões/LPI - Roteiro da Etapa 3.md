# Linguagem de Programação I - Roteiro da Etapa 3

---

# Superclasse Veículo e Subclasses Carro e Caminhão

## Cadastro

Cadastrar **6 objetos**:

- 3 carros
- 3 caminhões

Formato:

```text
veículos [ potência - tipo_carro | capacidade_carga_caminhão ]
```

Exemplos:

```text
| 100 cv - passeio       -- 120 cv - passeio       |
| 116 cv - passeio       -- 130 cv - caminhonete   |
|  85 cv - passeio       -- 185 cv - caminhonete   |

| 460 cv - 38000 kg      -- 540 cv - 80000 kg      |
| 530 cv - 74000 kg      -- 510 cv - 50000 kg      |
| 510 cv - 50000 kg      -- 540 cv - 80000 kg      |
```

---

# Sequência 1 - Filtragem de Carros

## Filtro 1

### Potência mínima do veículo

```text
100 cv
```

Resultado:

```text
| 100 cv - passeio       -- 120 cv - passeio       |
| 116 cv - passeio       -- 130 cv - caminhonete   |

| 460 cv - 38000 kg      -- 540 cv - 80000 kg      |
| 530 cv - 74000 kg      -- 510 cv - 50000 kg      |
| 510 cv - 50000 kg      -- 540 cv - 80000 kg      |
```

---

## Filtro 2

### Tipo do carro

```text
passeio
```

Resultado:

```text
| 100 cv - passeio       -- 120 cv - passeio       |

| 460 cv - 38000 kg      -- 540 cv - 80000 kg      |
| 530 cv - 74000 kg      -- 510 cv - 50000 kg      |
| 510 cv - 50000 kg      -- 540 cv - 80000 kg      |
```

---

# Sequência 2 - Filtragem de Caminhões

## Filtro 1

### Potência mínima do veículo

```text
500 cv
```

Resultado:

```text
| 530 cv - 74000 kg      -- 510 cv - 50000 kg      |
| 510 cv - 50000 kg      -- 540 cv - 80000 kg      |
```

---

## Filtro 2

### Capacidade máxima de carga do caminhão

```text
75000 kg
```

Resultado:

```text
| 530 cv - 74000 kg      -- 510 cv - 50000 kg      |
```

---

# Objetivo da Etapa 3

Implementar a herança da entidade:

```text
Veículo
├── Carro
└── Caminhão
```

com:

- cadastro de objetos das subclasses;
- armazenamento nos conjuntos da superclasse;
- impressão diferenciada por tipo;
- filtragem utilizando atributos da superclasse e das subclasses;
- manutenção dos filtros acumulados durante as seleções.