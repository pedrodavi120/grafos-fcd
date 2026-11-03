# Validação Tecnológica: Bases de Dados em Grafos (Neo4j & Cypher)

Projeto desenvolvido para a unidade curricular de **Fundamentos e Técnicas em Ciência de Dados**  
**Curso:** Análise e Desenvolvimento de Sistemas (TADS)  
**Instituição:** Universidade Federal do Rio Grande do Norte (UFRN) — Campus de Ciências Agrárias / Escola Agrícola de Jundiaí (EAJ)  
**Docente:** Prof. Dr. Josenalde Oliveira  
**Repositório Oficial:** [https://github.com/pedrodavi120/grafos-fcd](https://github.com/pedrodavi120/grafos-fcd)  

---

## 1. Integrantes da Equipe e Atribuições

| Integrante | Atribuição no Projeto | Papel na Apresentação | Tempo Estimado |
|---|---|---|---|
| **Pedro Davi** | Desenvolvimento da base de código e arquitetura do repositório | Abertura, Contexto NoSQL, O Problema e Data Product Canvas | 00:00 - 03:45 (~3m45s) |
| **Cleiton Mizael** | Elaboração dos diapositivos e documentação visual da apresentação | Teoria de Grafos, SGBD Neo4j, Cypher e Estrutura Cookiecutter | 03:45 - 09:00 (~5m15s) |
| **Natanael Lucas** | Gravação e edição do vídeo demonstrativo (3 a 5 minutos) | Pipeline Prático (Explícita vs. Implícita), NetworkX e Conclusão | 09:00 - 14:00 (~5m00s) |

---

## 2. Contextualização e Escopo do Trabalho

Na unidade curricular de Fundamentos e Técnicas em Ciência de Dados, foram examinados diversos modelos de armazenamento não relacional (NoSQL: chave-valor, documentos, colunas e grafos, conforme os materiais didáticos `ds04.pdf` e `ds05.pdf`), bem como o ciclo de vida dos dados e os níveis analíticos aplicados ao contexto de Big Data (`ds06.pdf`).

Nas atividades práticas com MongoDB (`listastorage.pdf`, Questão 7), foi proposta a modelagem da coleção `grade_curricular` do curso de TADS, armazenando os pré-requisitos em vetores de cadeias de caracteres (`pre_requisito: ["Algoritmos"]`). 

Embora o modelo documental responda adequadamente a consultas diretas de um único salto (Questão 7.1), surgem gargalos expressivos quando se pretende consultar travessias recursivas de múltiplos saltos (identificar todas as disciplinas destravadas direta ou indiretamente por uma matéria inicial) ou quando se deseja calcular caminhos críticos de formatura. Em sistemas gerenciadores de banco de dados relacionais (SGBD-R), tais consultas exigem junções sucessivas (`JOIN`) com explosão de custos computacionais ou expressões de tabela comuns recursivas (`WITH RECURSIVE`).

O propósito desta validação tecnológica consiste em demonstrar, de forma empírica e reprodutível, como as **Bases de Dados Baseadas em Grafos** (representadas pelo **Neo4j** com a linguagem declarativa **Cypher**) tratam relacionamentos como elementos de primeira ordem, viabilizando percursos analíticos com custo computacional praticamente constante por salto mediante o princípio de **Adjacência Livre de Índices** (*Index-Free Adjacency*).

---

## 3. Alinhamento com o Conteúdo Programático

O projeto foi construído respeitando rigorosamente a fundamentação apresentada pelo docente:
* **Análise Exploratória de Dados (AED):** Aplicação das diretrizes de John Tukey (1977) descritas em aula (`ds06.pdf`), utilizando Pandas, `describe()`, histogramas e gráficos de dispersão para o reconhecimento dos dados da matriz curricular.
* **Análise Explícita:** Formulação de consultas declarativas em Cypher para responder diretamente às restrições de pré-requisitos curriculares (equivalente analítico da Questão 7.1 da lista).
* **Análise Implícita:** Emprego da biblioteca `NetworkX` para a extração de conhecimento não aparente na rede: métricas de grau (entrada e saída), identificação de nós estranguladores do fluxo pedagógico (centralidade de intermediação / *betweenness*) e identificação do caminho crítico em grafo direcionado acíclico (DAG).
* **Data Product Canvas:** Planejamento estratégico segundo o modelo metodológico de Leandro S. Carvalho referenciado no SIGAA (`references/data_product_canvas.md`).
* **Estrutura Cookiecutter Data Science:** Organização modular e reprodutível segundo as boas práticas mantidas pela DrivenData.

---

## 4. Estrutura de Diretórios (Cookiecutter Data Science)

```text
grafos-fcd/
├── LICENSE                      <- Licença de código aberto MIT
├── Makefile                     <- Automação de tarefas (setup, data, ingest, metrics, figures, test)
├── README.md                    <- Documentação formal e instruções de reprodução
├── pyproject.toml               <- Configuração de empacotamento e ferramentas
├── requirements.txt             <- Dependências para replicação do ambiente
├── setup.py                     <- Script de instalação do módulo src em modo editável
│
├── data/
│   ├── raw/                     <- Dados brutos imutáveis (tads_disciplinas.csv e tads_prerequisitos.csv)
│   ├── interim/                 <- Dados intermediários de transformação
│   └── processed/               <- Dados processados (nodes_componentes.csv e edges_prerequisitos.csv)
│
├── docs/
│   ├── atribuicoes_equipe.md    <- Especificação de atribuições operacionais e divisão de apresentação
│   ├── slides_roteiro.md        <- Roteiro detalhado dos diapositivos (14 minutos de apresentação)
│   ├── roteiro_video.md         <- Roteiro estruturado para o vídeo demonstrativo (3 a 5 minutos)
│   └── topologia_grafo.md       <- Especificação formal do Labeled Property Graph (LPG)
│
├── notebooks/
│   ├── 0.1-analise-exploratoria-inicial.ipynb
│   ├── 0.2-modelacao-e-ingestao-neo4j.ipynb
│   └── 0.3-analise-avancada-e-metricas-grafo.ipynb
│
├── references/
│   ├── data_product_canvas.md   <- Especificação do produto de dados nos 8 blocos formais
│   └── cypher_reference.md      <- Catálogo de consultas Cypher utilizadas na validação
│
├── reports/
│   └── figures/                 <- Figuras analíticas exportadas pelo pipeline:
│       ├── grau_centralidade_distribuicao.png
│       ├── ranking_betweenness_gargalos.png
│       └── topologia_dag_curricular.png
│
├── src/
│   ├── __init__.py
│   ├── config.py                <- Gestor de caminhos globais e parâmetros de ambiente
│   ├── data/make_dataset.py     <- Tratamento de dados brutos e validação de integridade
│   ├── graph/connection.py      <- Gestor de conexão com Neo4j (local ou Neo4j AuraDB)
│   ├── graph/schema.py          <- Criação de restrições de unicidade e índices em Cypher
│   ├── graph/loader.py          <- Ingestão em lote idempotente via UNWIND e MERGE
│   ├── analysis/graph_metrics.py<- Algoritmos de grafos em NetworkX (centralidades e caminho crítico)
│   └── visualization/plot_graph.py <- Geração automatizada das figuras do relatório
│
└── tests/
    ├── test_dataset.py          <- Testes de unicidade e integridade referencial dos dados
    ├── test_graph_queries.py    <- Testes de validação da sintaxe das consultas Cypher
    └── test_metrics.py          <- Testes matemáticos das propriedades do DAG e métricas
```

---

## 5. Instruções de Instalação e Configuração

### Pré-requisitos
* Python 3.10 ou superior instalado no sistema operacional.
* Instância do Neo4j ativa localmente (`bolt://localhost:7687`) ou serviço em nuvem (**Neo4j AuraDB**).

#### Inicialização local do Neo4j via Docker (Opcional)
```bash
docker run -d --name neo4j-fcd \
  -p 7474:7474 -p 7687:7687 \
  -e NEO4J_AUTH=neo4j/senha_teste \
  neo4j:5-community
```
> O painel do Neo4j Browser estará acessível em: `http://localhost:7474`

#### Configuração do Ambiente Virtual
```bash
# 1. Clonar o repositório
git clone https://github.com/pedrodavi120/grafos-fcd.git
cd grafos-fcd

# 2. Criar o ambiente virtual
python -m venv .venv

# 3. Ativar o ambiente virtual
# No Windows (PowerShell):
.venv\Scripts\Activate.ps1
# No Linux / macOS:
source .venv/bin/activate

# 4. Instalar as dependências do projeto
pip install -r requirements.txt
pip install -e .

# 5. Configurar as variáveis de ambiente
cp .env.example .env
```

---

## 6. Execução do Pipeline

A execução de cada etapa pode ser realizada sequencialmente pelo terminal ou por meio dos alvos do `Makefile`:

```bash
# 1. Processamento e validação dos dados curriculares
python src/data/make_dataset.py

# 2. Execução da suíte de testes automatizados
python -m unittest discover -s tests -p "test_*.py" -v

# 3. Carga idempotente dos nós e arestas no Neo4j
python src/graph/loader.py

# 4. Cálculo das métricas de redes complexas com NetworkX
python src/analysis/graph_metrics.py

# 5. Geração e exportação das figuras analíticas em reports/figures/
python src/visualization/plot_graph.py
```

---

## 7. Resultados Analíticos da Validação

1. **Análise Explícita (Cypher):**
   - A consulta direta de pré-requisitos para *Algoritmos e Programação* (TAD0102) foi processada em latência inferior a 3 milissegundos.
   - A travessia de múltiplos saltos (`*1..3`) recuperou com precisão todas as disciplinas da cadeia formativa de desenvolvimento e dados sem a necessidade de recursão manual.
2. **Análise Implícita (NetworkX):**
   - **Centralidade de Intermediação (*Betweenness Centrality*):** A própria disciplina ministrada pelo docente, *Fundamentos e Técnicas em Ciência de Dados* (TAD0204), desponta como o principal nó estruturante e gargalo de intermediação da rede ($0.0128$), seguida por *Estruturas de Dados* (TAD0020) e *Projetos Aplicados I* (TAD0156).
   - **Grau de Saída (*Out-Degree*):** *Algoritmos e Programação* (TAD0102) lidera como a maior provedora de pré-requisitos do curso (4 dependências diretas), seguida por *Processo de Desenvolvimento de Software* (TAD0012) e *Fundamentos e Técnicas em Ciência de Dados* (TAD0204).
   - **Caminho Crítico de Formatura:** O caminho de maior extensão em saltos no DAG curricular abrange uma sequência obrigatória de 5 períodos letivos:
     $$\text{Algoritmos} \rightarrow \text{POO} \rightarrow \text{Análise e Projeto OO} \rightarrow \text{Arquitetura de Software} \rightarrow \text{Projetos Aplicados I} \rightarrow \text{Projetos Aplicados II}$$

---

## 8. Documentos de Apoio à Apresentação

* **Roteiro dos Diapositivos:** [`docs/slides_roteiro.md`](docs/slides_roteiro.md)
* **Atribuições dos Integrantes:** [`docs/atribuicoes_equipe.md`](docs/atribuicoes_equipe.md)
* **Guião do Vídeo Demonstrativo:** [`docs/roteiro_video.md`](docs/roteiro_video.md)
* **Data Product Canvas:** [`references/data_product_canvas.md`](references/data_product_canvas.md)
* **Catálogo de Consultas Cypher:** [`references/cypher_reference.md`](references/cypher_reference.md)
