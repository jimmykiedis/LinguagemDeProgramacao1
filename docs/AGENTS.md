# Guia para agentes em `docs/`

Este diretório reúne material de apoio da disciplina Linguagem de Programação I:
resumos em Markdown, PDFs originais, checklists, tutoriais e a especificação do
projeto. O objetivo é servir como fonte rápida de contexto, não como cópia
integral dos PDFs.

## Como usar estes documentos

- Leia os `.md` primeiro. Eles existem para evitar consultas constantes aos
  PDFs.
- Consulte os PDFs quando o Markdown estiver incompleto, parecer contraditório
  ou quando for necessário confirmar uma regra oficial de avaliação.
- Ao encontrar conflito entre resumo e PDF oficial da disciplina, considere o
  PDF/checklist oficial como fonte mais forte e atualize o `.md` com uma nota
  clara.
- Ao encontrar conflito entre `docs/espec.md` e o código atual, use
  `LP1-E3/src` como referência funcional do domínio e registre a divergência
  em vez de apagá-la silenciosamente.

## Separar exemplo do professor e projeto real

Muitos tutoriais usam o sistema de referência do professor:

```text
Lançamentos de veículos de uma montadora por uma agência de Publicidade
Montadora, Veículo, Carro, Caminhão, AgênciaPublicidade, Lançamento
```

Esse modelo é exemplo didático. O projeto real deste repositório é:

```text
Orçamento de Peças de um Sinistro para uma Seguradora
Sinistro, Seguradora, Peca, PeçaMecânica, PeçaLataria, Orcamento
```

Ao editar documentação, deixe explícito quando um trecho é regra geral do
professor e quando é adaptação ao projeto do aluno.

## Arquivos principais

- `espec.md`: resumo da especificação do projeto. Atenção: há nomes
  possivelmente antigos ou divergentes (`PeçaCarro`/`PeçaMoto`) em relação ao
  código atual (`PeçaMecânica`/`PeçaLataria`).
- `checklist e revisões/LPI - Revisão da Etapa 1.md`: critérios da primeira
  etapa: entidades simples, `Data`, impressão e filtros.
- `checklist e revisões/LPI - Check List da Etapa 2.md`: relacionamento
  múltiplo, associação, empacotamento e filtros da associadora.
- `checklist e revisões/LPI - Check List da Etapa 3.md`: herança,
  subclasses, filtros com atributos da superclasse e das subclasses.
- `checklist e revisões/LPI - Check List da Etapa 4.md`: interface textual,
  persistência, diretório `dados/`, `saida.pdf` e empacotamento final.
- `Tutoriais/*.md`: metodologia e exemplos do professor. Não trate os exemplos
  como entidades do projeto real.
- `plano de aula/LPI - Plano de Ensino - 1S26.pdf`: calendário e visão geral
  da disciplina.

## Regras resumidas da disciplina

- O sistema é incremental em quatro etapas.
- Etapas 2 e 3: entregar somente `src/`, `espec.pdf` e `fontes.pdf`.
- Etapa 4: entregar somente `dados/`, `src/`, `espec.pdf`, `fontes.pdf` e
  `saida.pdf`.
- O cabeçalho dos PDFs deve seguir:

```text
Linguagem de Programação I - Etapa n - Leonardo Farias de Oliveira
```

- A especificação deve conter título, entidades, relacionamentos, atributos,
  referências e enumerados.
- Deve haver somente um relacionamento múltiplo.
- A entidade associadora deve referenciar somente duas entidades.
- Entidades com chave própria usam o primeiro atributo como identificador.
  Associação e subclasses são exceções.
- Relacionamento múltiplo usa referência no plural; associação usa referências
  no singular.
- Dicionários globais são usados para conjuntos com chave; listas são usadas
  para entidades associadoras.
- Booleanos aparecem na impressão apenas quando verdadeiros.
- Filtros devem ser acumulativos e reduzir gradualmente os resultados.

## Cuidados ao atualizar Markdown

- Remova artefatos como `:contentReference[...]` quando estiver limpando um
  arquivo.
- Não copie páginas inteiras de PDFs para Markdown; resuma regras e exemplos
  necessários.
- Preserve nomes próprios e termos da disciplina em português.
- Use blocos de código para estruturas de diretório, cabeçalhos obrigatórios e
  exemplos de assinatura de função.
- Se atualizar `espec.md`, confira também os `LP1-E*/espec.pdf` e o código da
  etapa correspondente.
- Se atualizar checklists, mantenha separado: empacotamento, especificação,
  implementação, filtragem e avaliação.

## PDFs já consultados

Os seguintes PDFs foram usados para consolidar o contexto dos `AGENTS.md`:

- `LP1-E2/espec.pdf`
- `LP1-E3/espec.pdf`
- `LP1-E4/espec.pdf`
- `docs/plano de aula/LPI - Plano de Ensino - 1S26.pdf`
- `docs/checklist e revisões/pdfs/LPI - Check List da Etapa 4.pdf`

Observação importante: `LP1-E4/espec.pdf` está em `LP1-E4/`, mas o texto
extraído mostra cabeçalho de Etapa 2. Isso deve ser corrigido se a Etapa 4 for
preparada para entrega.
