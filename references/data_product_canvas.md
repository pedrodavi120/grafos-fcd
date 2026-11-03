# Data Product Canvas: Otimizador de Fluxos Curriculares e Gargalos com Grafos (GraphCurriculum-FCD)

Baseado no framework conceitual de Leandro S. Carvalho (*Data Product Canvas*, Medium) e adaptado para a disciplina de **Fundamentos e Tecnicas em Ciencia de Dados** (TADS / UFRN - Prof. Josenalde Oliveira).

---

## Matriz Estrategica do Produto de Dados

```
+---------------------------------------------------------------------------------------------------------------------+
|                                              DATA PRODUCT CANVAS                                                    |
|                                         (GraphCurriculum TADS/EAJ - UFRN)                                           |
+----------------------------------------------------------+----------------------------------------------------------+
| 1. PROBLEMA & OPORTUNIDADE                               | 2. USUARIOS & STAKEHOLDERS                               |
| * Dificuldade de modelar e analisar cadeias de depen-     | * Coordenacao de Curso e Colegiado de TADS/EAJ:          |
|   dencias curriculares com SQL classico (JOINs recursi-  |   Identificar disciplinas "rolha" causadoras de evasao   |
|   vos custosos e CTEs complexas).                         |   e retencao de estudantes.                              |
| * NoSQL documental (ex.: MongoDB) exige arrays aninhados | * Alunos de Graduacao:                                   |
|   e consultas manuais com $in e pipelines pesados para   |   Visualizacao do caminho critico para formatura e simu-  |
|   descobrir pre-requisitos indiretos.                    |   lacao de impacto de trancamento/reprovacao.             |
| * Oportunidade: Utilizar bases em grafos (Neo4j) para    | * Analistas de Dados Educacionais:                       |
|   travessias instantaneas de k-saltos e analise de rede. |   Extracao de metricas de centralidade e modularidade.    |
+----------------------------------------------------------+----------------------------------------------------------+
| 3. PROPOSTA DE VALOR DO PRODUTO DE DADOS                 | 4. INTERFACES DE CONSUMO & SAIDAS (OUTPUTS)              |
| * Resolucao de travessias de profundidade arbitraria      | * Neo4j Browser / Neo4j Bloom: Exploracao visual intera- |
|   (Index-Free Adjacency) com tempo O(1) por salto.       |   tiva da topologia de dependencias com coloracao por    |
| * Identificacao cientifica de componentes gargalo via    |   periodo e area tematica.                               |
|   algoritmos de centralidade de rede (NetworkX + Cypher).| * Relatorios e Figuras Analiticas (PNG/PDF):             |
| * Pipeline 100% reprodutivel sob padrao Cookiecutter     |   Histogramas de carga horaria, rankings de betweenness  |
|   Data Science, integrando dados reais do curso.         |   e visualizacao do DAG do curso.                         |
|                                                          | * Notebooks Jupyter com consultas analiticas prontas.    |
+----------------------------------------------------------+----------------------------------------------------------+
| 5. FONTES DE DADOS (DATA SOURCES)                        | 6. PROCESSAMENTO & MODELAGEM ANALITICA                   |
| * Matriz Curricular Oficial de TADS/EAJ - UFRN:          | * Ingestao Idempotente: Scripts Python com UNWIND e      |
|   - tads_disciplinas.csv (codigo, nome, carga horaria,   |   MERGE garantindo atomicidade e constraints unicas.     |
|     semestre, natureza, area de conhecimento).           | * Analise Explicita: Consultas Cypher declarativas para  |
|   - tads_prerequisitos.csv (pares direcionados           |   cadeias de pre-requisitos (*1..k).                     |
|     codigo_origem -> codigo_destino).                    | * Analise Implicita: Teoria dos Grafos via NetworkX      |
|                                                          |   (Grau de entrada/saida, Betweenness, Caminho Critico).  |
+----------------------------------------------------------+----------------------------------------------------------+
| 7. CRITERIOS DE SUCESSO & KPIS                           | 8. ARQUITETURA, RISCOS & GOVERNANCA                      |
| * Tecnico: Execucao de consultas de ate 4 saltos em      | * SGBD: Neo4j 5.x (Community / AuraDB) via protocolo     |
|   tempo < 10ms localmente e < 50ms em nuvem (AuraDB).     |   Bolt oficial com autenticacao segura.                  |
| * Dados: 100% de integridade referencial nas arestas     | * Isolamento: Cookiecutter Data Science com segregacao   |
|   (zero nos orfaos ou arestas desconexas).               |   estrita de raw, processed, src e reports.              |
| * Negocio: Ranqueamento inequivoco das 3 disciplinas com | * Risco: Dependencia de disponibilidade de porta local   |
|   maior potencial de travamento curricular.              |   (7687) contornada por suporte nativo a nuvem (AuraDB). |
+----------------------------------------------------------+----------------------------------------------------------+
```

---

## Detalhamento dos 8 Blocos

### 1. Problema & Oportunidade
Em sistemas academicos tradicionais (RDBMS), responder a pergunta "Quais sao todos os pre-requisitos diretos e indiretos para cursar Projeto Integrador II?" exige a escrita de CTEs recursivas (`WITH RECURSIVE`) ou multiplos `JOINs`, cuja complexidade de execucao cresce exponencialmente com o numero de niveis. Em bancos NoSQL orientados a documentos (ex.: MongoDB, conforme a Questao 7 da lista de exercicios do professor), o armazenamento de pre-requisitos como listas de strings (`pre_requisito: ["Algoritmos"]`) resolve buscas diretas simples, mas inviabiliza travessias recursivas e calculo de topologias globais sem desnormalizacao extrema ou pos-processamento pesado na aplicacao.

### 2. Usuarios & Stakeholders
* **Gestores Educacionais (UFRN):** Tomada de decisao fundamentada em dados sobre flexibilizacao de pre-requisitos e alocacao de docentes em disciplinas-chave.
* **Discentes:** Autonomia no planejamento de matricula, compreendendo o custo de oportunidade e atraso gerado por trancamentos.
* **Comunidade de Ciencia de Dados:** Demonstracao pratica do uso de grafos como ferramenta analitica superior para dados relacionais densos.

### 3. Proposta de Valor
Entregar um pipeline que consolida, valida e analisa a topologia do curso, oferecendo respostas instantaneas para navegacao de rede e metricas matematicas de vulnerabilidade curricular (teoria de redes complexas aplicada a educacao).

### 4. Interfaces de Consumo
* Consultas parametrizadas no console Cypher / Neo4j Browser para exploracao interativa.
* Graficos estaticos gerados por Seaborn/Matplotlib para o relatorio executivo.
* Modulos Python reusaveis (`src.analysis.graph_metrics`) integraveis a qualquer aplicacao web academica.

### 5. Fontes de Dados
Dados tabulares fidedignos extraidos da estrutura pedagogica de TADS (UFRN/EAJ), tratados contra inconsistencias de codificacao, espacos em branco e duplicatas.

### 6. Processamento & Modelagem Analitica
Aplicacao do ciclo de dados de Big Data apresentado em aula:
* **Exploratoria:** Estatisticas descritivas das disciplinas (distribuicao de carga horaria, densidade de pre-requisitos).
* **Explicita:** Consultas diretas em Cypher (`MATCH ... RETURN ...`).
* **Implicita:** Algoritmos de rede para descobrir nos estruturantes ocultos (disciplinas que, embora tenham carga horaria padrao, controlam o fluxo de graduacao de quase todo o curso).

### 7. Criterios de Sucesso
* Idempotencia total do pipeline (multiplas execucoes do loader produzem o mesmo estado final no grafo sem duplicatas).
* Resposta de latencia minima sem locks de tabela.
* Suite de testes automatizados com 100% de aprovacao.

### 8. Arquitetura, Riscos & Governanca
* Repositorio versionado no GitHub com estrutura DrivenData Cookiecutter.
* Zero credenciais em codigo; credenciais gerenciadas por `.env`.
* Tratamento de excecoes no driver de banco de dados para falhas de rede.
