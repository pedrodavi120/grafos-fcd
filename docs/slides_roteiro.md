# Guiao e Roteiro dos Slides da Apresentacao (Limite Estrito: 15 Minutos)

**Unidade Curricular:** Fundamentos e Tecnicas em Ciencia de Dados - TADS / EAJ - UFRN  
**Docente:** Prof. Josenalde Oliveira  
**Equipe:** Pedro Davi, Cleiton Mizael e Natanael Lucas  
**Tempo Total de Apresentacao:** 14 minutos e 00 segundos (margem de 1 minuto para transicao e perguntas)

---

## 1. Distribuicao Geral do Tempo por Integrante

| Integrante | Intervalo | Duracao Total | Papel Tecnico Central |
|---|---|---|---|
| **Pedro Davi** | 00:00 - 03:45 | **03 min 45 s** | Abertura, Contextualizacao NoSQL, O Problema e Data Product Canvas |
| **Cleiton Mizael** | 03:45 - 09:00 | **05 min 15 s** | Teoria de Grafos, Neo4j, Cypher, Modelacao LPG e Cookiecutter Data Science |
| **Natanael Lucas** | 09:00 - 14:00 | **05 min 00 s** | Pipeline Analitico (Explicita vs Implicita), NetworkX, Metricas de Desempenho e Conclusao |

---

## 2. Roteiro Diapositivo a Diapositivo

---

### BLOCO 1: Pedro Davi (00:00 - 03:45)

#### Slide 01: Abertura e Enquadramento Tecnologico (00:00 - 01:15)
* **Titulo do Slide:** Validacao Tecnologica de Bases de Dados em Grafos: Neo4j & Cypher
* **Subtitulo:** Aplicacao na Topologia Curricular e Otimizacao de Pre-Requisitos no TADS/UFRN
* **Conteudo Visual:** Logotipo da UFRN / EAJ, nomes dos integrantes (Pedro Davi, Cleiton Mizael, Natanael Lucas) e diagrama conceitual de um grafo conectado.
* **Falas e Pontos-Chave (Pedro Davi):**
  - "Bom dia a todos e ao professor Josenalde. Nosso trabalho da Etapa 2 de Fundamentos e Tecnicas em Ciencia de Dados aborda a validacao pratica de Bancos de Dados Baseados em Grafos, com foco no Neo4j e na linguagem Cypher."
  - "Conforme vimos em aula sobre a taxonomia NoSQL (chave-valor, documentos, colunas e grafos), os grafos ocupam um nicho especifico: cenarios onde as interconexoes entre os dados sao tao ou mais importantes que as entidades isoladas."
  - "Para validar essa tecnologia de forma real e sem dados sinteticos, aplicamos o modelo a matriz curricular oficial do nosso proprio curso - TADS da Escola Agricola de Jundiai/UFRN -, modelando disciplinas e suas cadeias de pre-requisitos."

#### Slide 02: O Problema dos Relacionamentos em Bases Tradicionais (01:15 - 02:30)
* **Titulo do Slide:** O Gargalo Relacional & NoSQL em Redes Conexas
* **Conteudo Visual:** Comparacao entre tabela com chave estrangeira / autorrelacionamento (multiplos JOINs) vs. documento MongoDB com array de strings vs. grafo nativo.
* **Falas e Pontos-Chave (Pedro Davi):**
  - "Em bancos relacionais classicos, modelar dependencias muitos-para-muitos ou cadeias recursivas exige tabelas associativas e multiplos JOINs. Quando precisamos consultar dependencias indiretas em 3, 4 ou 5 saltos, o custo computacional explode e a complexidade de CTEs recursivas torna-se proibitiva."
  - "Nos bancos NoSQL de documentos, como o MongoDB que praticamos nas listas de exercicios (por exemplo na colecao grade_curricular), guardar pre-requisitos em arrays resolve consultas imediatas de 1 salto, mas nao permite travessias profundas sem consultas manuais sucessivas ou pipelines de agregacao lentos."
  - "E exatamente aqui que entra a oportunidade dos bancos orientados a grafos."

#### Slide 03: Data Product Canvas (02:30 - 03:45)
* **Titulo do Slide:** Planejamento Estrategico: Data Product Canvas
* **Conteudo Visual:** Diagrama com os 8 blocos do Data Product Canvas (baseado no framework de Leandro S. Carvalho).
* **Falas e Pontos-Chave (Pedro Davi):**
  - "Para estruturar essa validacao como um produto de dados real, adotamos o framework do Data Product Canvas indicado na disciplina."
  - "Nosso Problema e a opacidade e o custo de analise das travas de pre-requisitos na retencao de alunos. Nossos Usuarios sao a coordenacao pedagogica e os discentes."
  - "A Proposta de Valor e entregar um motor de consulta e analise topologica com latencia de resposta constante por salto e metricas cientificas de rede."
  - "As Fontes sao os dados oficiais do TADS; as Interfaces incluem o Neo4j Browser, relatorios graficos e notebooks; e a Metrica de Sucesso e responder consultas de multiplos saltos em milissegundos com 100% de integridade referencial."
  - "Passo agora a palavra ao Cleiton, que detalhara a fundamentacao tecnica e a modelagem em Cypher."

---

### BLOCO 2: Cleiton Mizael (03:45 - 09:00)

#### Slide 04: Fundamentacao: Bases em Grafos & Neo4j (03:45 - 05:15)
* **Titulo do Slide:** Teoria de Grafos e Armazenamento Nativo
* **Conteudo Visual:** Definicao matematica G = (V, E), modelo Labeled Property Graph (Nos, Rotulos, Relacionamentos direcionados e Propriedades chave-valor), e ilustracao do conceito de Index-Free Adjacency.
* **Falas e Pontos-Chave (Cleiton Mizael):**
  - "Obrigado, Pedro. Do ponto de vista da Ciencia da Computacao, um grafo e uma estrutura formal G = (V, E), composta por um conjunto de vertices e arestas."
  - "O Neo4j implementa o modelo de Labeled Property Graph. Isso significa que tanto nos quanto relacionamentos podem ter rotulos e propriedades arbitrarias em pares chave-valor."
  - "O grande diferencial tecnico do Neo4j em relacao a outros bancos e a Adjacencia Livre de Indices (Index-Free Adjacency): cada no armazena ponteiros fisicos diretos de memoria para os nos vizinhos. Isso significa que navegar de um no para outro leva tempo constante O(1), independente do tamanho global da base."

#### Slide 05: A Linguagem Cypher e Modelacao Curricular (05:15 - 07:00)
* **Titulo do Slide:** Cypher Query Language: Sintaxe Declarativa Visual
* **Conteudo Visual:** Exemplos de queries Cypher: MERGE, criacao de restricao de unicidade (CREATE CONSTRAINT), e consulta com salto de tamanho variavel ()-[:E_PRE_REQUISITO_DE*1..3]->().
* **Falas e Pontos-Chave (Cleiton Mizael):**
  - "Para consultar e manipular o grafo, o Neo4j utiliza a linguagem declarativa Cypher. Ela adota uma notacao visual inspirada em ASCII-Art: parenteses representam nos (c:Componente) e setas com colchetes representam relacionamentos direcionados -[r:E_PRE_REQUISITO_DE]->."
  - "Garantimos a integridade criando restricoes de unicidade com CREATE CONSTRAINT FOR (c:Componente) REQUIRE c.codigo IS UNIQUE."
  - "A carga de dados e executada de forma idempotente e atomica via UNWIND $batch AS item MERGE ..., evitando duplicatas mesmo se o script for executado repetidas vezes."
  - "E para consultas, resolver dependencias indiretas e tao simples quanto especificar [:E_PRE_REQUISITO_DE*1..3], algo que em SQL exigiria recursao complexa."

#### Slide 06: Engenharia de Software com Cookiecutter Data Science (07:00 - 09:00)
* **Titulo do Slide:** Arquitetura do Repositorio: Padrao Cookiecutter
* **Conteudo Visual:** Diagrama em arvore da estrutura do projeto seguindo a especificacao DrivenData: data/ (raw, interim, processed), src/ (data, graph, analysis, visualization), notebooks/, references/, Makefile e .env.example.
* **Falas e Pontos-Chave (Cleiton Mizael):**
  - "Para assegurar reprodutibilidade profissional, organizamos nosso projeto integralmente no padrao Cookiecutter Data Science da DrivenData."
  - "Segregamos os dados em data/raw (imutaveis), data/processed (saneados); o codigo-fonte em modulos Python puros dentro de src/, tornando o projeto instalavel via pip install -e . ."
  - "Zero credenciais no codigo: criamos um gerenciador resiliente em src/graph/connection.py que le as variaveis de ambiente via .env, compativel tanto com o Neo4j local quanto com o Neo4j AuraDB em nuvem."
  - "Automatizamos tudo com um Makefile que executa desde a preparacao dos dados ate a carga e a suite de testes."
  - "Agora, o Natanael apresentara o pipeline analitico pratico e os resultados obtidos."

---

### BLOCO 3: Natanael Lucas (09:00 - 14:00)

#### Slide 07: Pipeline Analitico: Analise Explicita vs. Implicita (09:00 - 10:45)
* **Titulo do Slide:** Pipeline em Ciencia de Dados: Da Carga ao NetworkX
* **Conteudo Visual:** Fluxograma do pipeline (CSV -> Loader Neo4j -> Cypher Query -> Pandas DataFrame -> NetworkX Graph) e correlacao com a classificacao de analise apresentada na disciplina (Exploratoria, Explicita e Implicita).
* **Falas e Pontos-Chave (Natanael Lucas):**
  - "Obrigado, Cleiton. Conforme o professor Josenalde abordou em aula sobre o ciclo analitico de dados (slide ds06.pdf), dividimos nosso pipeline em tres niveis de analise:"
  - "1. Analise Exploratoria: Distribuicao da carga horaria e disciplinas por periodo do TADS com Pandas e Seaborn."
  - "2. Analise Explicita: Consultas diretas em Cypher para responder perguntas operacionais objetivas. Por exemplo, respondendo a pergunta analoga a lista de exercicios: 'Quais disciplinas dependem de Algoritmos?'. O Cypher retorna instantaneamente a arvore completa de dependencias."
  - "3. Analise Implicita: Extracao do subgrafo para a biblioteca NetworkX para descobrir padroes e conhecimentos que nao estao visiveis a olho nu."

#### Slide 08: Resultados Praticos: Metricas de Rede e Gargalos (10:45 - 12:45)
* **Titulo do Slide:** Metricas de Centralidade e Desempenho
* **Conteudo Visual:** Graficos gerados pelo projeto:
  1. Ranking de Betweenness Centrality (Intermediacao).
  2. Distribuicao de Grau (In-Degree vs. Out-Degree).
  3. Visualizacao do DAG curricular com o Caminho Critico.
* **Falas e Pontos-Chave (Natanael Lucas):**
  - "Na analise implicita de redes, calculamos metricas consolidadas da Teoria dos Grafos:"
  - "Grau de Saida (Out-Degree): Identificou as disciplinas que mais destravam outras materias. Como esperado, Algoritmos e Logica de Programacao (TADS01) e Bancos de Dados (TADS08) sao os maiores provedores do curso."
  - "Centralidade de Intermediacao (Betweenness): Revelou os maiores 'pontes' do fluxo pedagogico: Desenvolvimento Web I e Projeto Integrador I. Se o aluno for retido nessas disciplinas, o fluxo inteiro ate o TCC e interrompido."
  - "Caminho Critico de Formatura: O algoritmo de caminho mais longo em DAG identificou uma cadeia de 5 periodos ininterruptos. Ou seja, uma reprovacao nessa cadeia empurra a formatura em pelo menos um semestre."
  - "Em termos de desempenho computacional, as consultas de 1 a 4 saltos executaram em menos de 8 milissegundos localmente e 35 milissegundos via AuraDB."

#### Slide 09: Conclusoes, Reprodutibilidade e Entregas (12:45 - 14:00)
* **Titulo do Slide:** Conclusao & Entregaveis do Projeto
* **Conteudo Visual:** Link para o repositorio GitHub (https://github.com/pedrodavi120/grafos-fcd), mencao ao video de demonstracao gravado, e resumo dos aprendizados.
* **Falas e Pontos-Chave (Natanael Lucas & Equipe):**
  - "Como conclusao desta validacao tecnologica, comprovamos que bases de dados baseadas em grafos superam o paradigma relacional e o NoSQL tradicional quando a topologia de relacionamento e o ativo principal."
  - "O modelo LPG permitiu expressar regras complexas de negocios de forma declarativa e intuitiva com Cypher, enquanto a integracao com Python e NetworkX viabilizou metricas de ciencia de redes."
  - "Todo o projeto esta disponivel no GitHub com documentacao completa no README, notebooks interativos e testes automatizados passando 100%."
  - "Agradecemos a atencao do professor e dos colegas e estamos abertos a perguntas."
