# Validacao Tecnologica: Bases de Dados em Grafos (Neo4j & Cypher)

Projeto desenvolvido para a unidade curricular de **Fundamentos e Tecnicas em Ciencia de Dados**  
**Curso:** Analise e Desenvolvimento de Sistemas (TADS)  
**Instituicao:** Universidade Federal do Rio Grande do Norte (UFRN) - Campus de Ciencias Agrarias / Escola Agricola de Jundiai (EAJ)  
**Docente:** Prof. Dr. Josenalde Oliveira  
**Repositorio Oficial:** https://github.com/pedrodavi120/grafos-fcd  

---

## 1. Integrantes da Equipe e Papeis

| Integrante | Atribuicao no Projeto | Papel na Apresentacao (Amanha) | Tempo Estimado |
|---|---|---|---|
| **Pedro Davi** | Desenvolvimento da base de codigo e arquitetura do repositorio | Abertura, Contexto NoSQL, O Problema e Data Product Canvas | 00:00 - 03:45 (~3m45s) |
| **Cleiton Mizael** | Elaboracao dos slides e documentacao formal da apresentacao | Teoria de Grafos, SGBD Neo4j, Cypher e Estrutura Cookiecutter | 03:45 - 09:00 (~5m15s) |
| **Natanael Lucas** | Gravacao e edicao do video demonstrativo (3 a 5 minutos) | Pipeline Pratico (Explicita vs Implicita), NetworkX e Conclusao | 09:00 - 14:00 (~5m00s) |

---

## 2. Contextualizacao e Escopo do Trabalho

Na disciplina de Fundamentos e Tecnicas em Ciencia de Dados, foram estudados diferentes modelos de armazenamento NoSQL (chave-valor, documentos, colunas e grafos nos slides `ds04.pdf` e `ds05.pdf`), bem como o ciclo de vida dos dados e os niveis de analise de dados no contexto de Big Data (`ds06.pdf`).

Nas listas de exercicios praticas com MongoDB (`listastorage.pdf`, questao 7), foi proposta a modelagem da colecao `grade_curricular` do curso de TADS, armazenando os pre-requisitos em arrays de strings (`pre_requisito: ["Algoritmos"]`). 

Embora esse modelo documental funcione bem para consultas de leitura direta em 1 salto (questao 7.1), ele apresenta serias limitacoes quando se deseja consultar percursos encadeados de multiplos saltos (quais disciplinas uma matéria destrava indiretamente) ou identificar o caminho critico de formatura. Em bancos relacionais, esse tipo de consulta exige multiplos `JOINs` custosos ou CTEs recursivas (`WITH RECURSIVE`).

O objetivo desta validacao tecnologica e demonstrar, de forma simples e empirica, como os **Bancos de Dados Orientados a Grafos** (com o **Neo4j** e a linguagem declarativa **Cypher**) resolvem nativamente o armazenamento e a consulta de redes de dependencias atraves do conceito de **Adjacencia Livre de Indices** (*Index-Free Adjacency*).

---

## 3. Alinhamento com as Aulas do Professor

O projeto foi desenhado respeitando estritamente a sequencia didatica ministrada:
* **Analise Exploratoria de Dados (AED):** Aplicacao dos conceitos de John Tukey (1977) apresentados em aula (`ds06.pdf`), utilizando Pandas, describe(), histogramas e graficos de dispersao para conhecer o dataset curricular.
* **Analise Explicita:** Execucao de consultas declarativas em Cypher para responder diretamente as perguntas de pre-requisitos (equivalente a questao 7.1 da lista).
* **Analise Implicita:** Uso da biblioteca `NetworkX` para extracao de conhecimento nao obvio da rede: grau de entrada/saida, identificacao de disciplinas gargalo (centralidade de intermediacao / *betweenness*) e calculo do caminho critico de formatura em DAG.
* **Data Product Canvas:** Planejamento segundo a metodologia de Leandro S. Carvalho indicada no SIGAA (`references/data_product_canvas.md`).
* **Estrutura Cookiecutter Data Science:** Organizacao reprodutivel recomendada pela DrivenData.

---

## 4. Estrutura de Diretorios (Cookiecutter Data Science)

```text
grafos-fcd/
|-- LICENSE                      <- Licenca MIT
|-- Makefile                     <- Comandos uteis de execucao
|-- README.md                    <- Este documento
|-- pyproject.toml               <- Configuracao de empacotamento
|-- requirements.txt             <- Dependencias do projeto
|-- setup.py                     <- Instalacao do modulo src
|
|-- data/
|   |-- raw/                     <- Dados brutos (tads_disciplinas.csv e tads_prerequisitos.csv)
|   |-- interim/                 <- Dados intermediarios
|   `-- processed/               <- Dados saneados (nodes_componentes.csv e edges_prerequisitos.csv)
|
|-- docs/
|   |-- atribuicoes_equipe.md    <- Resumo de atribuicoes e orientacoes individuais
|   |-- slides_roteiro.md        <- Roteiro dos 9 slides calibrado para 15 minutos
|   |-- roteiro_video.md         <- Guiao para o video de demonstracao (3 a 5 min)
|   `-- topologia_grafo.md       <- Definicao do Labeled Property Graph (LPG)
|
|-- notebooks/
|   |-- 0.1-analise-exploratoria-inicial.ipynb
|   |-- 0.2-modelacao-e-ingestao-neo4j.ipynb
|   `-- 0.3-analise-avancada-e-metricas-grafo.ipynb
|
|-- references/
|   |-- data_product_canvas.md   <- Data Product Canvas nos 8 blocos
|   `-- cypher_reference.md      <- Guia de consultas Cypher utilizadas
|
|-- reports/
|   `-- figures/                 <- Graficos gerados pelo pipeline
|       |-- grau_centralidade_distribuicao.png
|       |-- ranking_betweenness_gargalos.png
|       `-- topologia_dag_curricular.png
|
|-- src/
|   |-- __init__.py
|   |-- config.py                <- Leitura do .env e caminhos
|   |-- data/make_dataset.py     <- Tratamento de dados brutos
|   |-- graph/connection.py      <- Conexao com Neo4j (local ou AuraDB)
|   |-- graph/schema.py          <- Constraints e indices Cypher
|   |-- graph/loader.py          <- Carga em lote com UNWIND e MERGE
|   |-- analysis/graph_metrics.py<- Calculo de metricas com NetworkX
|   `-- visualization/plot_graph.py <- Gerador de graficos
|
`-- tests/
    |-- test_dataset.py          <- Teste de integridade dos dados
    |-- test_graph_queries.py    <- Teste de sintaxe das queries Cypher
    `-- test_metrics.py          <- Teste dos algoritmos de grafos
```

---

## 5. Como Executar o Projeto

### Pre-requisitos
* Python 3.10 ou superior instalado
* Instancia do Neo4j ativa localmente (`bolt://localhost:7687`) ou Neo4j AuraDB (nuvem gratuita)

Caso utilize Docker para o Neo4j local:
```bash
docker run -d --name neo4j-fcd -p 7474:7474 -p 7687:7687 -e NEO4J_AUTH=neo4j/senha_teste neo4j:5-community
```

### Configuracao do Ambiente
```bash
# 1. Clonar o repositorio
git clone https://github.com/pedrodavi120/grafos-fcd.git
cd grafos-fcd

# 2. Criar ambiente virtual
python -m venv .venv

# Ativar ambiente virtual:
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Linux / macOS:
source .venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt
pip install -e .

# 4. Configurar variaveis de conexao
cp .env.example .env
```

---

## 6. Execucao dos Scripts

Os comandos podem ser executados via terminal ou atraves do `Makefile`:

```bash
# 1. Processar dados brutos e validar integridade referencial
python src/data/make_dataset.py

# 2. Executar testes automatizados da aplicacao
python -m unittest discover -s tests -p "test_*.py" -v

# 3. Fazer a carga idempotente dos dados no Neo4j
python src/graph/loader.py

# 4. Calcular as metricas de rede e caminho critico (NetworkX)
python src/analysis/graph_metrics.py

# 5. Gerar os graficos analiticos em reports/figures/
python src/visualization/plot_graph.py
```

---

## 7. Resultados Analiticos Obtidos

1. **Analise Explicita (Cypher):**
   - Consulta direta de pre-requisitos de *Algoritmos e Logica de Programacao* (TADS01) executada em tempo inferior a 3ms.
   - Percursos de 3 saltos recuperam instantaneamente as disciplinas de programacao avancada sem necessidade de joins recursivos.
2. **Analise Implicita (NetworkX):**
   - **Betweenness Centrality (Gargalos):** *Desenvolvimento Web I* (TADS11) e *Projeto Integrador I* (TADS22) apresentaram a maior centralidade de intermediacao, configurando pontos de estrangulamento que conectam o ciclo basico ao conclusivo.
   - **Out-Degree (Maiores Provedores):** *Algoritmos e Logica de Programacao* (TADS01) e *Bancos de Dados* (TADS08) destravam diretamente 4 componentes cada.
   - **Caminho Critico:** Cadeia de 5 periodos letivos ininterruptos partindo de Algoritmos ate Dispositivos Moveis.

---

## 8. Documentos de Suporte a Apresentacao

* **Roteiro dos Slides (15 Minutos):** [`docs/slides_roteiro.md`](docs/slides_roteiro.md)
* **Atribuicoes dos Integrantes:** [`docs/atribuicoes_equipe.md`](docs/atribuicoes_equipe.md)
* **Guiao do Video Demonstrativo (3 a 5 Min):** [`docs/roteiro_video.md`](docs/roteiro_video.md)
* **Data Product Canvas:** [`references/data_product_canvas.md`](references/data_product_canvas.md)
* **Dicionario Cypher:** [`references/cypher_reference.md`](references/cypher_reference.md)
