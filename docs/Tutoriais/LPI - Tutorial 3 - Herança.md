# Linguagem de Programação I - Tutorial 3

# Herança

## 1. Fatorando Dados e Métodos Comuns na Superclasse e Herdando nas Subclasses

No contexto da Programação Orientada a Objetos (POO), a herança permite definir dados (atributos e referências) e métodos comuns em uma classe mais genérica, denominada **superclasse**, que serão herdados por classes mais específicas, chamadas **subclasses**.

### Exemplo do Projeto

#### Superclasse: Veículo

A classe `Veículo` armazena os atributos comuns:

- marca_modelo
- alimentação (flex, diesel, elétrico)
- potência
- importado

#### Subclasse: Carro

Herda os atributos de `Veículo` e adiciona:

- tipo (passeio, utilitário, caminhonete)
- volume_carga

#### Subclasse: Caminhão

Herda os atributos de `Veículo` e adiciona:

- tração (6x4, 6x2, 4x4)
- capacidade_carga

### Vantagens da Herança

- Reutilização de código.
- Alterações nos atributos e métodos comuns são feitas apenas na superclasse.
- Facilita manutenção e evolução do sistema.

### Regra Fundamental

Para que uma classe seja superclasse de outra, deve existir uma relação do tipo:

> "A subclasse é um tipo da superclasse."

Exemplos válidos:

- Carro é um tipo de Veículo.
- Caminhão é um tipo de Veículo.

Exemplo inválido:

- Carro não é um tipo de Motor.

Nesse caso, deve-se utilizar associação/composição em vez de herança.

---

## Implementação da Classe Carro

```python
class Carro(Veículo):

    def __init__(
        self,
        marca_modelo,
        alimentação,
        potência,
        importado,
        tipo,
        volume_carga
    ):
        super().__init__(
            marca_modelo,
            alimentação,
            potência,
            importado
        )

        self.tipo = (
            tipo
            if tipo in (
                'passeio',
                'utilitário',
                'caminhonete'
            )
            else 'indefinida'
        )

        self.volume_carga = volume_carga

    def __str__(self):

        if self.importado:
            importado_str = 'importado |'
        else:
            importado_str = ''

        formato = (
            '{} {:<19} {} {:<8} {} {:<6} {} {:<11} {} {:>8} {} {}'
        )

        carro_formatado = formato.format(
            '|',
            self.marca_modelo,
            '|',
            self.alimentação,
            '|',
            f'{self.potência:3d} cv',
            '|',
            self.tipo,
            '|',
            f'{self.volume_carga:4d} l',
            '|',
            importado_str
        )

        return carro_formatado
```

---

## Implementação da Classe Caminhão

```python
class Caminhão(Veículo):

    def __init__(
        self,
        marca_modelo,
        alimentação,
        potência,
        importado,
        tração,
        capacidade_carga
    ):
        super().__init__(
            marca_modelo,
            alimentação,
            potência,
            importado
        )

        self.tração = (
            tração
            if tração in ('6x4', '6x2', '4x4')
            else 'sem tração'
        )

        self.capacidade_carga = capacidade_carga

    def __str__(self):

        if self.importado:
            importado_str = 'importado |'
        else:
            importado_str = ''

        formato = (
            '{} {:<19} {} {:<8} {} {:<6} {} {:<11} {} {:<6} {} {}'
        )

        caminhão_formatado = formato.format(
            '|',
            self.marca_modelo,
            '|',
            self.alimentação,
            '|',
            f'{self.potência:3d} cv',
            '|',
            self.tração,
            '|',
            f'{self.capacidade_carga:5d} kg',
            '|',
            importado_str
        )

        return caminhão_formatado
```

---

## Características Importantes da Herança

### Definição da superclasse

```python
class Carro(Veículo):
```

### Reutilização do construtor da superclasse

```python
super().__init__(
    marca_modelo,
    alimentação,
    potência,
    importado
)
```

### Acesso aos atributos herdados

As subclasses acessam diretamente:

- `marca_modelo`
- `alimentação`
- `potência`
- `importado`

---

## Polimorfismo e Sobreposição de Métodos

Um método herdado pode ser redefinido na subclasse mantendo sua assinatura.

Exemplo:

```python
def __str__(self):
```

Quando um objeto da subclasse executa:

```python
str(objeto)
```

será utilizada a implementação da subclasse e não a da superclasse.

Esse comportamento é chamado de **Polimorfismo**.