# Guia para agentes neste repositório

Este repositório é do trabalho incremental de Linguagem de Programação I
(UFGD/FACET, 2026/1) do aluno Leonardo Farias de Oliveira. O sistema é
desenvolvido em Python e evolui por etapas. O objetivo do guia é evitar que um
agente precise reler todos os PDFs ou varrer o diretório inteiro antes de
trabalhar.

## Contexto do projeto

Tema do sistema:

```text
Orçamento de Peças de um Sinistro para uma Seguradora
```

Modelo de domínio usado pelo código atual:

- `Seguradora`: entidade sem referência, armazenada globalmente em dicionário.
  Chave observada no código: `nome`. Atributos: `nome`, `cidade`,
  `cobertura_percentual`.
- `Sinistro`: entidade principal do relacionamento múltiplo, armazenada
  globalmente em dicionário. Chave observada no código: `numero`. Atributos
  atuais: `numero`, `cliente`, `telefone`, `pecas`.
- `Peca`: superclasse das peças de um sinistro. Atributos atuais: `código`,
  `nome`, `categoria`, `preco`, `mão_obra_própria`.
- `PeçaMecânica`: subclasse de `Peca`. Atributos específicos atuais: `tipo`,
  `dias_garantia`. Tipos aceitos: `suspensão`, `direção`, `motor`.
- `PeçaLataria`: subclasse de `Peca`. Atributos específicos atuais: `tipo`,
  `cor`. Tipos aceitos: `externo`, `interno`.
- `Orcamento`: entidade associadora, armazenada globalmente em lista. Relaciona
  um `Sinistro`, uma `Seguradora` e a `data` do orçamento.

Relacionamentos do projeto:

- Sem referência: `Seguradora` e a superclasse `Peca`.
- Relacionamento múltiplo: `Sinistro [1:N] Peca`, implementado por
  `Sinistro.pecas`, um dicionário local de peças.
- Associação: `Orcamento [Sinistro, Seguradora]`.
- Herança: `Peca -> PeçaMecânica, PeçaLataria`.

Há inconsistências entre alguns documentos e o código. Em caso de conflito para
implementação, use `LP1-E3/src` como referência funcional mais confiável e os
PDFs `LP1-E*/espec.pdf` apenas para confirmar a proposta acordada. Exemplos de
conflito já observados: `docs/espec.md` cita `PeçaCarro`/`PeçaMoto`, enquanto o
código usa `PeçaMecânica`/`PeçaLataria`; `LP1-E4/espec.pdf` está dentro da
Etapa 4, mas ainda possui cabeçalho de Etapa 2.

## Estrutura

```text
LP1-E1/   Etapa inicial: classes simples, filtros básicos.
LP1-E2/   Etapa com relacionamento múltiplo e associação.
LP1-E3/   Etapa com herança; melhor referência funcional atual.
LP1-E4/   Etapa alvo de interface textual e persistência; ainda incompleta.
docs/     Resumos em Markdown, checklists, tutoriais e PDFs da disciplina.
```

Cada etapa segue a estrutura:

```text
src/
├── controle/
│   └── projeto.py
├── entidades/
└── util/
```

A Etapa 4 também possui:

```text
src/interfaces/interface_textual.py
src/util/persistência_arquivo.py
```

## Estado atual das etapas

- `LP1-E1/src` compila, mas `python3 -m controle.projeto` falha porque
  `controle/projeto.py` importa `scr.*` em vez de `src`/imports locais.
- `LP1-E2/src` compila e executa a partir do diretório `LP1-E2/src`.
- `LP1-E3/src` compila e executa a partir do diretório `LP1-E3/src`; é a base
  principal para entender cadastros, impressão, relacionamento múltiplo,
  associação, herança e filtros acumulados.
- `LP1-E4/src` ainda não compila. O erro atual conhecido está em
  `interfaces/interface_textual.py`, no import com vírgula final. A interface
  também mistura nomes antigos do tutorial de referência (`lançamentos`,
  `montadora`, `tipo_carro`) com o domínio real de orçamentos.

## Como executar

Execute sempre a partir do `src` da etapa, porque os imports são relativos a
esse diretório:

```bash
cd "LP1-E3/src"
python3 -m controle.projeto
```

Para trocar de etapa:

```bash
cd "LP1-E2/src"
python3 -m controle.projeto
```

Validação rápida:

```bash
python3 -m compileall -q LP1-E3/src
```

Depois de compilar ou executar, remova `__pycache__` antes de empacotar:

```bash
find LP1-E1/src LP1-E2/src LP1-E3/src LP1-E4/src -type d -name __pycache__ -prune -exec rm -rf {} +
```

## Regras da disciplina que importam para código

- Use Python puro; não introduza dependências de runtime sem necessidade.
- Preserve o estilo do projeto: identificadores em português, inclusive com
  acentos onde já existirem.
- Classes em PascalCase; funções, métodos, variáveis e arquivos em snake_case.
- Diretórios padronizados: `controle`, `entidades`, `util` e, na Etapa 4,
  `interfaces`.
- Entidades com chave própria devem usar dicionários globais e impedir
  duplicidade na inserção.
- A entidade associadora deve usar lista global.
- No relacionamento múltiplo, a entidade principal mantém um dicionário local
  com os objetos relacionados.
- Subclasses devem ser armazenadas nas estruturas da superclasse ou nos
  relacionamentos baseados na superclasse.
- Valide enumerados no `__init__`; quando o valor não for aceito, o padrão local
  é usar `indefinida`.
- Booleanos devem aparecer na impressão apenas quando forem `True`.
- Os filtros devem ficar na entidade associadora, acumular progressivamente e
  reduzir os resultados. Evite filtrar diretamente por identificadores
  (`nome`, `telefone`, `numero`); use prefixos ou faixas quando necessário.
- A classe `Data` em `util/data.py` fornece `__str__`, comparadores e
  `calcular_idade`; use-a para filtros por data.

## Etapa 4: direção esperada

A Etapa 4 deve evoluir a Etapa 3 com:

- interface textual para cadastrar seguradoras, sinistros, peças e orçamentos;
- leitura de filtros pela interface;
- persistência em arquivo com `pickle`;
- diretório `dados/` contendo `conjuntos_globais.bin`;
- recuperação dos conjuntos globais no início e salvamento no fim;
- geração/registro de saída para `saida.pdf`.

Ao trabalhar na Etapa 4, primeiro alinhe a interface com o domínio real:
`Seguradora`, `Sinistro`, `Peca`/`PeçaMecânica`/`PeçaLataria` e `Orcamento`.
Não reaproveite nomes do exemplo de referência (`Montadora`, `Lançamento`,
`Veículo`, `Carro`, `Caminhão`) a menos que esteja editando os documentos de
tutorial.

Pontos conhecidos a revisar na Etapa 4:

- `interface_textual.py` tem import sintaticamente inválido.
- O arquivo chama funções com acento (`criar_orçamento`, `get_orçamentos`) que
  não existem no módulo atual (`criar_orcamento`, `get_orcamentos`).
- `controle/projeto.py` importa `set_seguradoras`, `set_pecas`,
  `set_sinistros` e `set_orcamentos`, mas esses setters não existem nos módulos
  atuais.
- `ler_peça()` passa argumentos das subclasses em ordem diferente da assinatura
  em `entidades/peca.py`.
- `imprimir_peças_sinistro()` usa variáveis trocadas (`montadora`, `sinistro`).

## Empacotamento das entregas

Nome do diretório zipado:

```text
LPI - Etapa n - Leonardo Farias de Oliveira
```

Troque `n` pelo número da etapa.

Etapas 2 e 3 devem conter somente:

```text
src/
espec.pdf
fontes.pdf
```

Etapa 4 deve conter somente:

```text
dados/
src/
espec.pdf
fontes.pdf
saida.pdf
```

Cabeçalho obrigatório dos PDFs:

```text
Linguagem de Programação I - Etapa n - Leonardo Farias de Oliveira
```

No final dos PDFs, incluir cidade, data de envio e assinatura. O checklist
recomenda assinatura digital ou manuscrita legível digitalizada.

Há um site anotado em `Leia-me.txt` para testar empacotamento:

```text
https://teste-empacotamento-etapas.squareweb.app
```

## Documentos de apoio

Leia primeiro os Markdown em `docs/`; eles resumem os PDFs. Use PDFs somente
quando houver dúvida, conflito ou necessidade de confirmar cabeçalhos/regras
oficiais.

Arquivos úteis:

- `docs/espec.md`: resumo da especificação do projeto, mas contém nomes
  divergentes do código atual.
- `docs/checklist e revisões/*.md`: regras de avaliação e empacotamento por
  etapa.
- `docs/Tutoriais/*.md`: metodologia do professor e modelo de referência.
- `LP1-E*/espec.pdf`: especificação entregue ou planejada por etapa.
- `LP1-E*/fontes.pdf`: snapshot em PDF dos fontes de cada etapa entregue.

## Ao editar

- Identifique a etapa alvo antes de alterar arquivos.
- Não altere nenhum arquivo dentro de `LP1-E*/src/util`. O professor proibiu
  mudanças nessas pastas para evitar quebra entre as entregas. Isso inclui
  `LP1-E1/src/util`, `LP1-E2/src/util`, `LP1-E3/src/util` e `LP1-E4/src/util`.
- Para comportamento atual do sistema, compare com `LP1-E3/src` antes de mexer
  na Etapa 4.
- Não apague mudanças não relacionadas.
- Mantenha as alterações pequenas e coerentes com a metodologia dos tutoriais.
- Ao final de mudanças em código, rode `compileall` da etapa editada e, se
  possível, `python3 -m controle.projeto` a partir do `src`.
- Não deixe `__pycache__` no pacote de entrega.
