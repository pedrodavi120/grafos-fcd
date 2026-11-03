# Atribuicoes da Equipe e Guia para a Apresentacao

**Disciplina:** Fundamentos e Tecnicas em Ciencia de Dados  
**Docente:** Prof. Josenalde Oliveira  
**Data da Apresentacao:** 04/11/2026 (Amanha)  
**Tempo Limite da Apresentacao:** 15 minutos (tempo de fala planejado: 14 minutos)

---

## 1. Divisao de Tarefas Operacionais do Trabalho

* **Pedro Davi:** Responsavel pelo desenvolvimento e estruturacao do repositorio de codigo, organizacao do padrao Cookiecutter Data Science, scripts de processamento de dados e testes.
* **Cleiton Mizael:** Responsavel pela elaboracao visual dos slides da apresentacao (com base no roteiro em `docs/slides_roteiro.md`) e organizacao dos topicos teoricos de grafos.
* **Natanael Lucas:** Responsavel pela gravacao e edicao do video demonstrativo curto (3 a 5 minutos, conforme guiao em `docs/roteiro_video.md`) evidenciando o codigo, o Neo4j Browser e as metricas.

---

## 2. Divisao de Fala na Apresentacao de Amanha (14 Minutos)

Para atender a exigencia de participacao equitativa de todos os membros no limite maximo de 15 minutos, a fala foi distribuida da seguinte forma (com Pedro falando um pouco menos na abertura e contextualizacao):

### Bloco 1: Pedro Davi (00:00 - 03:45 | ~3 min e 45 s)
* **Slides 01, 02 e 03:**
  1. **Abertura e Contextualizacao (00:00 - 01:15):** Apresentar a equipe (TADS/EAJ/UFRN) e o objetivo do trabalho: validar o uso de bases de dados orientadas a grafos (Neo4j & Cypher) para modelar dependencias curriculares reais sem dados ficticios.
  2. **O Problema Relacional e NoSQL Documental (01:15 - 02:30):** Explicar as limitacoes vistas em aula:
     - No modelo relacional, multiplos `JOINs` recursivos causam lentidao severa quando a profundidade aumenta.
     - No MongoDB (exercicio da `grade_curricular` feito na lista), guardar pre-requisitos em arrays funciona para 1 salto, mas nao para travessias encadeadas.
  3. **Data Product Canvas (02:30 - 03:45):** Apresentar sinteticamente os 8 blocos do canvas (framework do Leandro Carvalho): problema, usuarios (coordenacao e alunos), proposta de valor (consultas em tempo constante por salto) e metricas de sucesso. Fazer a passagem de fala para Cleiton.

---

### Bloco 2: Cleiton Mizael (03:45 - 09:00 | ~5 min e 15 s)
* **Slides 04, 05 e 06:**
  4. **Fundamentacao em Grafos e Neo4j (03:45 - 05:15):**
     - O modelo Labeled Property Graph (LPG): nos, rotulos, relacionamentos direcionados e propriedades.
     - O conceito de Adjacencia Livre de Indices (*Index-Free Adjacency*): cada vertice possui ponteiros diretos em memoria para seus vizinhos, garantindo tempo O(1) por salto percorrido.
  5. **A Linguagem Cypher e Modelagem Curricular (05:15 - 07:00):**
     - Sintaxe declarativa e visual em padrao ASCII: `(c:Componente)-[:E_PRE_REQUISITO_DE]->(d:Componente)`.
     - Carga idempotente via `UNWIND` e `MERGE` com restricoes de unicidade (`CREATE CONSTRAINT`).
     - Consultas com travessia de tamanho variavel `[:E_PRE_REQUISITO_DE*1..3]`.
  6. **Arquitetura Cookiecutter Data Science (07:00 - 09:00):**
     - Explicar a organizacao do projeto: dados brutos imutaveis em `data/raw`, codigo modular em `src/`, configuracao limpa com `.env.example`, `Makefile` e testes automatizados. Fazer a passagem de fala para Natanael.

---

### Bloco 3: Natanael Lucas (09:00 - 14:00 | ~5 min e 00 s)
* **Slides 07, 08 e 09:**
  7. **Pipeline Analitico: Explicita vs Implicita (09:00 - 10:45):**
     - Conectar com o slide `ds06.pdf` do professor Josenalde:
       - **Analise Exploratoria (AED):** Distribuicao de carga horaria e disciplinas por periodo (Pandas/Seaborn).
       - **Analise Explicita:** Consulta direta em Cypher respondendo a questao analoga a lista de exercicios (disciplinas que dependem de Algoritmos).
       - **Analise Implicita:** Integracao Neo4j com Python e NetworkX para minerar padroes de rede nao evidentes a olho nu.
  8. **Resultados e Metricas de Rede (10:45 - 12:45):**
     - Apresentar as metricas calculadas:
       - **Grau de Saida (Out-Degree):** Algoritmos (TADS01) e Banco de Dados (TADS08) sao as materias que mais destravam o curso.
       - **Betweenness Centrality (Gargalos):** Desenvolvimento Web I e Projeto Integrador I atuam como pontes criticas que, se travadas, interrompem o fluxo ate o TCC.
       - **Caminho Critico de Formatura:** Sequencia obrigatoria de 5 semestres encadeados sem margem de reprovacao.
  9. **Conclusao e Entregaveis (12:45 - 14:00):**
     - Sintese de viabilidade do produto de dados.
     - Apresentacao do link do repositorio no GitHub (`https://github.com/pedrodavi120/grafos-fcd`), mencao ao video demonstrativo e fechamento para perguntas da banca.

---

## 3. Checklist para Amanha
* [ ] Slides prontos em formato PDF ou PPTX (Cleiton)
* [ ] Video gravado de 3 a 5 minutos e link disponivel no README / entrega (Natanael)
* [ ] Repositorio GitHub atualizado e publico (Pedro)
* [ ] Cronometro sincronizado na apresentacao presencial (iniciar no slide 1)
