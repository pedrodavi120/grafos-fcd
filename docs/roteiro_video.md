# Guiao para Gravacao do Video Demonstrativo (Duracao: 3 a 5 Minutos)

**Projeto:** Validacao Tecnologica de Bases de Dados em Grafos (Neo4j & Cypher)  
**Unidade Curricular:** Fundamentos e Tecnicas em Ciencia de Dados - TADS / EAJ - UFRN  
**Docente:** Prof. Josenalde Oliveira  
**Responsavel pela Gravacao e Edicao:** Natanael Lucas  
**Equipe:** Pedro Davi, Cleiton Mizael e Natanael Lucas

---

## 1. Visao Geral da Gravacao
* **Duracao Ideal:** Entre 3 minutos e 30 segundos e 4 minutos e 15 segundos (limite maximo de 5 minutos).
* **Software Sugerido:** OBS Studio ou gravador de tela nativo do Windows (`Win + Alt + R`).
* **Qualidade:** 1080p, audio claro, sem ruidos.
* **Janelas a Capturar:** VS Code (terminal e codigo) e Navegador (Neo4j Browser / Jupyter Lab).

---

## 2. Cronograma Minuto a Minuto

### 00:00 - 00:45 | Introducao e Data Product Canvas
* **Em Tela:** Slide de abertura com o titulo do trabalho, nomes da equipe e a imagem do Data Product Canvas.
* **Audio:**
  > "Ola professor Josenalde. Este e o video de demonstracao da nossa validacao tecnologica da Etapa 2, com foco em Bancos de Dados em Grafos utilizando Neo4j e a linguagem Cypher.
  > Nosso objetivo foi modelar as disciplinas e a grade de pre-requisitos do curso de TADS da EAJ/UFRN para testar o desempenho e a expressividade de grafos frente ao modelo relacional e NoSQL documental.
  > Estruturamos a solucao com base no Data Product Canvas, definindo requisitos tecnicos, proposta de valor e criterios de sucesso."

### 00:45 - 01:45 | Estrutura Cookiecutter e Ingestao de Dados
* **Em Tela:** VS Code mostrando a estrutura de pastas (`data/`, `src/`, `notebooks/`, `Makefile`).
* **Acao ao Vivo no Terminal:**
  1. Mostrar o arquivo `data/raw/tads_disciplinas.csv`.
  2. Executar o comando de carga:
     ```bash
     python src/graph/loader.py
     ```
* **Audio:**
  > "O projeto foi estruturado seguindo o padrao Cookiecutter Data Science.
  > Os dados curriculares brutos ficam em data/raw e sao saneados para data/processed.
  > O script loader.py se conecta ao Neo4j atraves do driver oficial e executa comandos Cypher utilizando UNWIND e MERGE, o que garante atomicidade e idempotencia sem duplicar registros.
  > Como vemos na saida do terminal, foram carregados 26 componentes e 27 relacionamentos de pre-requisito."

### 01:45 - 03:00 | Demonstracao no Neo4j Browser (Cypher)
* **Em Tela:** Neo4j Browser conectado ao banco.
* **Acoes ao Vivo:**
  1. Executar a visualizacao geral:
     ```cypher
     MATCH (n:Componente) RETURN n LIMIT 25;
     ```
     (Exibir a rede de vertices e arestas direcionadas).
  2. Executar a consulta de pre-requisitos diretos e indiretos (analoga ao exercicio da lista):
     ```cypher
     MATCH path = (alg:Componente {codigo: 'TADS01'})-[:E_PRE_REQUISITO_DE*1..3]->(alvo)
     RETURN path;
     ```
* **Audio:**
  > "No Neo4j Browser, podemos ver a topologia visual do grafo. Cada no e uma disciplina e cada aresta direcionada indica a relacao E_PRE_REQUISITO_DE.
  > Aqui executamos uma consulta que busca todas as disciplinas destravadas a partir de Algoritmos em ate 3 saltos.
  > Graças a Adjacencia Livre de Indices do Neo4j, essa busca ocorre por ponteiros diretos de memoria em poucos milissegundos, sem precisar de joins aninhados ou recursao em SQL."

### 03:00 - 04:00 | Metricas de Teoria dos Grafos (NetworkX)
* **Em Tela:** Jupyter Lab ou terminal executando `python src/analysis/graph_metrics.py`.
* **Acoes ao Vivo:**
  1. Mostrar o ranking de Betweenness Centrality e o Caminho Critico.
  2. Exibir brevemente as figuras salvas em `reports/figures/`.
* **Audio:**
  > "Para a analise implicita dos dados, integramos o Neo4j com o NetworkX em Python.
  > O algoritmo comprovou que o grafo e um DAG valido e identificou que Desenvolvimento Web I e Projeto Integrador I sao os maiores gargalos curriculares por terem a maior centralidade de intermediacao.
  > Alem disso, o caminho critico de formatura exige 5 periodos consecutivos sem retencao."

### 04:00 - 04:30 | Encerramento
* **Em Tela:** Pagina do repositorio no GitHub com os testes passando.
* **Audio:**
  > "O repositorio completo com codigo modular, testes unitarios e notebooks esta disponivel no GitHub. Concluimos assim a validacao tecnologica com sucesso. Muito obrigado."

---

## 3. Checklist Tecnico
* [ ] Conexao com Neo4j testada antes de iniciar a gravacao.
* [ ] Fonte do terminal aumentada para permitir boa leitura no video.
* [ ] Terminal limpo (`cls` ou `clear`) antes de rodar os comandos.
