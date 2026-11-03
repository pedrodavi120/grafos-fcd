# Guião e Roteiro dos Diapositivos da Apresentação Oral (15 Minutos)

**Unidade Curricular:** Fundamentos e Técnicas em Ciência de Dados  
**Docente:** Prof. Dr. Josenalde Oliveira  
**Curso:** Análise e Desenvolvimento de Sistemas (TADS) — EAJ / UFRN  
**Grupo:** G1 — T7: Banco de Dados Baseado em Grafos (Neo4j & Cypher)  
**Data da Apresentação:** Quarta-feira, 04/11/2026, às 07h50 (Abertura dos Seminários)  
**Equipe:** Pedro Davi, Cleiton Mizael e Natanael Lucas  
**Tempo Total Planejado:** 14 minutos e 00 segundos (reserva de 1 minuto para transições e encerramento)

> **Nota Estratégica:** Em conformidade com a orientação do docente ("Evitem demonstrações ao vivo... Para demonstrações o ideal é exibir vídeo curto focado na funcionalidade"), a demonstração prática nos slides 07 e 08 baseia-se na exibição do vídeo demonstrativo gravado ou nos gráficos analíticos já processados em alta resolução.

---

## 1. Distribuição de Tempo por Integrante

| Integrante | Intervalo | Duração Total | Foco Temático |
|---|---|---|---|
| **Pedro Davi** | 00:00 - 03:45 | **03 min 45 s** | Abertura, Contextualização NoSQL, O Problema e Data Product Canvas |
| **Cleiton Mizael** | 03:45 - 09:00 | **05 min 15 s** | Teoria de Grafos, Neo4j, Linguagem Cypher, Modelagem LPG e Cookiecutter |
| **Natanael Lucas** | 09:00 - 14:00 | **05 min 00 s** | Pipeline Analítico (Explícita vs. Implícita), NetworkX, Métricas e Conclusão |

---

## 2. Conteúdo dos Diapositivos e Guia de Fala

---

### BLOCO 1: Pedro Davi (00:00 - 03:45)

#### Diapositivo 01: Abertura e Enquadramento Tecnológico (00:00 - 01:15)
* **Título:** Validação Tecnológica de Bases de Dados em Grafos: Neo4j & Cypher
* **Subtítulo:** Análise Topológica e Otimização de Pré-Requisitos Curriculares no TADS / UFRN
* **Elementos Visuais:** Identificação institucional da UFRN / EAJ, nomes dos integrantes e diagrama conceitual de um grafo direcionado.
* **Pontos da Fala:**
  - Apresentação da equipe e objetivo do trabalho da Etapa 2 de Fundamentos e Técnicas em Ciência de Dados.
  - Enquadramento na taxonomia NoSQL estudada em aula: posicionamento dos bancos em grafos frente aos modelos chave-valor, documentos e colunas.
  - Justificativa do corpus de dados: aplicação sobre a matriz curricular real do curso de TADS da UFRN/EAJ, dispensando dados sintéticos e garantindo validade prática.

#### Diapositivo 02: O Gargalo Relacional e NoSQL em Redes Conexas (01:15 - 02:30)
* **Título:** Limitações de Modelos Tradicionais em Estruturas Conectadas
* **Elementos Visuais:** Diagrama comparativo entre modelagem relacional com chaves estrangeiras recursivas (`JOIN`), modelagem documental em MongoDB com vetores de strings e modelo em grafo nativo.
* **Pontos da Fala:**
  - Explicação do custo computacional de múltiplos `JOIN`s e expressões de tabela comuns recursivas em bancos relacionais quando a profundidade dos saltos aumenta.
  - Paralelo com as atividades práticas de MongoDB da disciplina: armazenamento de pré-requisitos em vetores da coleção `grade_curricular`, que resolve buscas diretas de 1 salto, mas restringe percursos de múltiplos níveis sem rotinas pesadas de agregação.
  - Apresentação da oportunidade técnica proporcionada pelas bases de dados em grafos.

#### Diapositivo 03: Data Product Canvas (02:30 - 03:45)
* **Título:** Planejamento Estratégico: Data Product Canvas
* **Elementos Visuais:** Matriz dos 8 blocos do Data Product Canvas segundo a metodologia de Leandro S. Carvalho.
* **Pontos da Fala:**
  - Exposição estruturada do canvas: Problema (visibilidade e custo de análise de travas curriculares), Usuários (coordenação e corpo discente), Proposta de Valor (travessias instantâneas em tempo constante por salto) e Métricas de Sucesso (latência milimétrica e integridade referencial total).
  - Transição formal da fala para o integrante Cleiton Mizael.

---

### BLOCO 2: Cleiton Mizael (03:45 - 09:00)

#### Diapositivo 04: Fundamentação: Bases em Grafos & Neo4j (03:45 - 05:15)
* **Título:** Teoria dos Grafos e Armazenamento Nativo
* **Elementos Visuais:** Representação matemática formal $G = (V, E)$, modelo *Labeled Property Graph* (nós, rótulos, arestas direcionadas e propriedades) e ilustração do conceito de *Index-Free Adjacency*.
* **Pontos da Fala:**
  - Definição conceitual de vértices e arestas no contexto da ciência de dados.
  - Características do modelo LPG implementado pelo Neo4j.
  - O diferencial da Adjacência Livre de Índices: nós conectados diretamente por ponteiros de memória, possibilitando tempo de travessia $O(1)$ por salto independentemente do volume total de dados da base.

#### Diapositivo 05: A Linguagem Cypher e a Modelagem Curricular (05:15 - 07:00)
* **Título:** Cypher Query Language: Sintaxe Declarativa Visual
* **Elementos Visuais:** Exemplos de comandos Cypher: cláusulas `MERGE`, restrição de unicidade com `CREATE CONSTRAINT` e percursos de profundidade variável `()-[:E_PRE_REQUISITO_DE*1..3]->()`.
* **Pontos da Fala:**
  - Funcionamento da sintaxe em padrão ASCII visual: parênteses `()` para nós e setas com colchetes `-[]->` para relacionamentos.
  - Garantia de atomicidade e idempotência nas cargas de dados com `UNWIND` e `MERGE`.
  - Expressividade da consulta de múltiplos saltos em contraste com o SQL recursivo tradicional.

#### Diapositivo 06: Engenharia de Software com Cookiecutter Data Science (07:00 - 09:00)
* **Título:** Arquitetura do Repositório: Padrão Cookiecutter
* **Elementos Visuais:** Estrutura hierárquica das pastas do projeto (`data/`, `src/`, `notebooks/`, `references/`, `reports/`, `Makefile` e `.env.example`).
* **Pontos da Fala:**
  - Adoção das diretrizes de reprodutibilidade da DrivenData: segregação entre dados imutáveis brutos (`raw`) e dados processados (`processed`).
  - Módulos Python estruturados dentro de `src/`, permitindo instalação em modo editável (`pip install -e .`).
  - Práticas de segurança: ausência de credenciais no código-fonte através do uso de variáveis de ambiente (`.env`) e validação via testes automatizados. Transição formal da palavra para Natanael Lucas.

---

### BLOCO 3: Natanael Lucas (09:00 - 14:00)

#### Diapositivo 07: Pipeline Analítico: Análise Explícita vs. Implícita (09:00 - 10:45)
* **Título:** Pipeline em Ciência de Dados: Da Ingestão ao NetworkX
* **Elementos Visuais:** Fluxograma do pipeline (CSV $\rightarrow$ Loader Neo4j $\rightarrow$ Cypher Query $\rightarrow$ Pandas DataFrame $\rightarrow$ Grafo NetworkX) e correlação com a classificação de análise apresentada na disciplina (`ds06.pdf`).
* **Pontos da Fala:**
  - Análise Exploratória (AED): reconhecimento descritivo dos dados curriculares conforme a literatura técnica de John Tukey (1977).
  - Análise Explícita: execução de consultas Cypher para resolução direta de perguntas pontuais de pré-requisitos (análogas ao exercício da lista).
  - Análise Implícita: transição para a biblioteca `NetworkX` para extração de propriedades topológicas não observáveis em consultas pontuais.

#### Diapositivo 08: Resultados Empíricos: Métricas de Rede e Gargalos (10:45 - 12:45)
* **Título:** Métricas de Centralidade e Desempenho Computacional
* **Elementos Visuais:** Gráficos analíticos gerados no projeto: ranking de *Betweenness Centrality*, dispersão de graus (entrada vs. saída) e visualização estratificada do DAG com o caminho crítico destacado.
* **Pontos da Fala:**
  - Grau de saída (*Out-Degree*): demonstração de *Algoritmos e Programação* (TAD0102) como a maior provedora da base com 4 dependências diretas.
  - Centralidade de Intermediação (*Betweenness*): demonstração matemática de que a própria disciplina da matéria, *Fundamentos e Técnicas em Ciência de Dados* (TAD0204), atua como o principal nó estruturante e articulador da formação acadêmica na matriz real de TADS/EAJ.
  - Caminho Crítico de Formatura: cadeia contínua de 5 períodos letivos ininterruptos de Algoritmos até Projetos Aplicados II.
  - Desempenho computacional: execução das travessias em menos de 8 milissegundos localmente e 35 milissegundos via Neo4j AuraDB.

#### Diapositivo 09: Conclusões e Entregas do Projeto (12:45 - 14:00)
* **Título:** Conclusões e Disponibilização dos Entregáveis
* **Elementos Visuais:** Hiperligação e código de acesso para o repositório no GitHub (`https://github.com/pedrodavi120/grafos-fcd`), menção ao vídeo demonstrativo gravado e síntese das contribuições.
* **Pontos da Fala:**
  - Síntese da validação: conformidade plena da tecnologia de grafos para cenários de alta conectividade.
  - Disponibilidade pública de todo o código, dados processados, cadernos interativos e testes automatizados aprovados na íntegra.
  - Agradecimento ao docente e aos colegas de turma, abrindo espaço para a fase de perguntas da avaliação.
