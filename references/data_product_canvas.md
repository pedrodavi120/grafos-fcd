# Data Product Canvas: Otimizador de Fluxos Curriculares e Gargalos com Grafos (GraphCurriculum-FCD)

Baseado no framework conceitual de Leandro S. Carvalho (*Data Product Canvas*, Medium) e adaptado para a disciplina de **Fundamentos e Técnicas em Ciência de Dados** (TADS / EAJ — UFRN, Docente: Prof. Dr. Josenalde Oliveira).

---

## Matriz Estratégica do Produto de Dados

```
+---------------------------------------------------------------------------------------------------------------------+
|                                              DATA PRODUCT CANVAS                                                    |
|                                         (GraphCurriculum TADS/EAJ - UFRN)                                           |
+----------------------------------------------------------+----------------------------------------------------------+
| 1. PROBLEMA & OPORTUNIDADE                               | 2. USUÁRIOS & STAKEHOLDERS                               |
| * Dificuldade de modelar e analisar cadeias de depen-     | * Coordenação de Curso e Colegiado de TADS/EAJ:          |
|   dências curriculares com SQL clássico (JOINs recursi-  |   Identificar disciplinas "rolha" causadoras de evasão   |
|   vos custosos e CTEs complexas).                         |   e retenção de estudantes.                              |
| * NoSQL documental (ex.: MongoDB) exige arrays aninhados | * Alunos de Graduação:                                   |
|   e consultas manuais com $in e pipelines pesados para   |   Visualização do caminho crítico para formatura e simu-  |
|   descobrir pré-requisitos indiretos.                    |   lação de impacto de trancamento/reprovação.             |
| * Oportunidade: Utilizar bases em grafos (Neo4j) para    | * Analistas de Dados Educacionais:                       |
|   travessias instantâneas de k-saltos e análise de rede. |   Extração de métricas de centralidade e modularidade.    |
+----------------------------------------------------------+----------------------------------------------------------+
| 3. PROPOSTA DE VALOR DO PRODUTO DE DADOS                 | 4. INTERFACES DE CONSUMO & SAÍDAS (OUTPUTS)              |
| * Resolução de travessias de profundidade arbitrária      | * Neo4j Browser / Neo4j Bloom: Exploração visual intera- |
|   (Index-Free Adjacency) com tempo O(1) por salto.       |   tiva da topologia de dependências com coloração por    |
| * Identificação científica de componentes gargalo via    |   período e área temática.                               |
|   algoritmos de centralidade de rede (NetworkX + Cypher).| * Relatórios e Figuras Analíticas (PNG/PDF):             |
| * Pipeline 100% reprodutível sob padrão Cookiecutter     |   Histogramas de carga horária, rankings de betweenness  |
|   Data Science, integrando dados reais do curso.         |   e visualização do DAG do curso.                         |
|                                                          | * Notebooks Jupyter com consultas analíticas prontas.    |
+----------------------------------------------------------+----------------------------------------------------------+
| 5. FONTES DE DADOS (DATA SOURCES)                        | 6. PROCESSAMENTO & MODELAGEM ANALÍTICA                   |
| * Matriz Curricular Oficial de TADS/EAJ - UFRN:          | * Ingestão Idempotente: Scripts Python com UNWIND e      |
|   - tads_disciplinas.csv (código, nome, carga horária,   |   MERGE garantindo atomicidade e restrições únicas.      |
|     semestre, natureza, área de conhecimento).           | * Análise Explícita: Consultas Cypher declarativas para  |
|   - tads_prerequisitos.csv (pares direcionados           |   cadeias de pré-requisitos (*1..k).                     |
|     codigo_origem -> codigo_destino).                    | * Análise Implícita: Teoria dos Grafos via NetworkX      |
|                                                          |   (Grau de entrada/saída, Betweenness, Caminho Crítico).  |
+----------------------------------------------------------+----------------------------------------------------------+
| 7. CRITÉRIOS DE SUCESSO & KPIS                           | 8. ARQUITETURA, RISCOS & GOVERNANÇA                      |
| * Técnico: Execução de consultas de até 4 saltos em      | * SGBD: Neo4j 5.x (Community / AuraDB) via protocolo     |
|   tempo < 10ms localmente e < 50ms em nuvem (AuraDB).     |   Bolt oficial com autenticação segura.                  |
| * Dados: 100% de integridade referencial nas arestas     | * Isolamento: Cookiecutter Data Science com segregação   |
|   (zero nós órfãos ou arestas desconexas).               |   estrita de raw, processed, src e reports.              |
| * Negócio: Ranqueamento inequívoco das 3 disciplinas com | * Risco: Dependência de disponibilidade de porta local   |
|   maior potencial de travamento curricular.              |   (7687) contornada por suporte nativo a nuvem (AuraDB). |
+----------------------------------------------------------+----------------------------------------------------------+
```

---

## Detalhamento Metodológico dos 8 Blocos

### 1. Problema & Oportunidade
Em sistemas acadêmicos tradicionais baseados em SGBD relacional, responder à pergunta *"Quais são todos os pré-requisitos diretos e indiretos para cursar Projetos Aplicados II?"* exige a escrita de expressões de tabela comuns recursivas (`WITH RECURSIVE`) ou múltiplos `JOIN`s, cuja complexidade de execução degrada exponencialmente com o aumento dos níveis de profundidade. Em bancos NoSQL orientados a documentos (a exemplo do MongoDB abordado na Questão 7 da lista da disciplina), o armazenamento de dependências como listas de cadeias de caracteres (`pre_requisito: ["Algoritmos"]`) soluciona consultas pontuais de 1 salto, mas inviabiliza travessias recursivas e cálculo de topologias globais sem desnormalização excessiva ou pós-processamento oneroso na camada da aplicação.

### 2. Usuários & Stakeholders
* **Gestores Educacionais (UFRN):** Tomada de decisão fundamentada em dados sobre flexibilização de pré-requisitos e alocação estratégica de docentes em disciplinas com alta taxa de retenção.
* **Corpo Discente:** Planejamento autônomo de matrícula semestral, compreendendo com antecedência o impacto temporal e o custo de atraso gerado por eventuais reprovações ou trancamentos.
* **Comunidade de Ciência de Dados:** Demonstração empírica do uso de bancos orientados a grafos como ferramenta analítica superior para estruturas de rede complexas.

### 3. Proposta de Valor
Disponibilização de um pipeline de engenharia e análise de dados que consolida, valida e analisa a topologia do curso, oferecendo respostas com latência constante por salto e métricas matemáticas formais de vulnerabilidade curricular baseadas na teoria de redes complexas.

### 4. Interfaces de Consumo
* Consultas parametrizadas no console Cypher e Neo4j Browser para exploração visual e interativa.
* Figuras analíticas em alta resolução geradas por Seaborn e Matplotlib para documentação técnica e relatórios executivos.
* Módulos Python reutilizáveis (`src.analysis.graph_metrics`) passíveis de integração em qualquer aplicação acadêmica.

### 5. Fontes de Dados
Dados tabulares extraídos da estrutura pedagógica de TADS (UFRN/EAJ), devidamente submetidos a controle de integridade de tipos, ausência de duplicatas e consistência de chaves primárias e estrangeiras.

### 6. Processamento & Modelagem Analítica
Aplicação estruturada do ciclo analítico de dados abordado nas aulas teóricas da disciplina (`ds06.pdf`):
* **Análise Exploratória:** Levantamento de estatísticas descritivas dos componentes (distribuição de carga horária e densidade de dependências por período).
* **Análise Explícita:** Execução de consultas declarativas em Cypher (`MATCH ... RETURN ...`) para respostas pontuais de requisitos.
* **Análise Implícita:** Aplicação de algoritmos de teoria dos grafos com NetworkX para identificação de nós estruturantes (disciplinas com elevado coeficiente de intermediação que controlam o fluxo de graduação).

### 7. Critérios de Sucesso
* Idempotência estrita do pipeline: múltiplas execuções do script de carga mantêm o mesmo estado final na base de dados, sem duplicatas.
* Resposta de latência mínima sem ocorrência de bloqueios globais de leitura.
* Suíte de testes automatizados com 100% de aprovação.

### 8. Arquitetura, Riscos & Governança
* Repositório público no GitHub formatado segundo o padrão Cookiecutter Data Science.
* Gestão segura de credenciais através de variáveis de ambiente isoladas em arquivo `.env`.
* Tratamento defensivo de exceções de rede e conectividade no driver do Neo4j.
