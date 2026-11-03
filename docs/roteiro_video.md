# Guião Técnico para Gravação do Vídeo Demonstrativo (3 a 5 Minutos)

**Projeto:** Validação Tecnológica de Bases de Dados em Grafos (Neo4j & Cypher)  
**Unidade Curricular:** Fundamentos e Técnicas em Ciência de Dados  
**Docente:** Prof. Dr. Josenalde Oliveira  
**Curso:** Análise e Desenvolvimento de Sistemas (TADS) — EAJ / UFRN  
**Responsável Técnico pela Gravação e Edição:** Natanael Lucas  
**Equipe:** Pedro Davi, Cleiton Mizael e Natanael Lucas  

---

## 1. Parâmetros de Produção Audiovisual
* **Duração Recomendada:** Entre 3 minutos e 30 segundos e 4 minutos e 15 segundos (limite regulamentar máximo: 5 minutos).
* **Software de Captura:** OBS Studio ou Gravador de Tela integrado do Windows (`Win + Alt + R`).
* **Resolução:** 1080p (Full HD), áudio equalizado e sem ruídos ambientes.
* **Ambientes de Gravação:** VS Code (código-fonte e terminal) e Navegador Web (Neo4j Browser e Jupyter Lab).

---

## 2. Roteiro Cronometrado Passo a Passo

### 00:00 - 00:45 | Contextualização e Data Product Canvas
* **Ambiente Visual:** Diapositivo inicial com os dados de identificação da equipe e exibição integral do *Data Product Canvas*.
* **Locução (Natanael Lucas):**
  > "Olá, professor Josenalde. Este é o vídeo demonstrativo da nossa validação tecnológica referente à Etapa 2 da disciplina de Fundamentos e Técnicas em Ciência de Dados, cujo tema é Bancos de Dados Baseados em Grafos, com foco no Neo4j e na linguagem Cypher.
  > Nosso objetivo prático foi modelar a matriz curricular e as dependências de pré-requisitos do curso de TADS da EAJ/UFRN para comprovar o ganho de eficiência em percursos relacionais densos frente aos modelos relacionais tradicionais e documentais.
  > Todo o planejamento técnico seguiu a estrutura formal do Data Product Canvas, que define claramente as fontes, os usuários, a proposta de valor e as métricas de sucesso."

### 00:45 - 01:45 | Arquitetura Cookiecutter e Ingestão de Dados
* **Ambiente Visual:** VS Code evidenciando a hierarquia de diretórios do padrão *Cookiecutter Data Science* (`data/`, `src/`, `notebooks/`, `Makefile`).
* **Execução em Terminal:**
  1. Apresentação do arquivo `data/raw/tads_disciplinas.csv`.
  2. Execução do script de carga:
     ```bash
     python src/graph/loader.py
     ```
* **Locução (Natanael Lucas):**
  > "A arquitetura do projeto segue rigorosamente o padrão Cookiecutter Data Science.
  > Os dados brutos das disciplinas e pré-requisitos residem em data/raw e são tratados e validados para a pasta data/processed.
  > No módulo loader.py, utilizamos o driver oficial do Neo4j com parâmetros de conexão parametrizados por variáveis de ambiente.
  > Ao executar o script, são aplicadas as restrições de unicidade no banco e realizada a carga em lote idempotente através das cláusulas UNWIND e MERGE do Cypher, impedindo a inserção de nós ou arestas duplicadas.
  > Conforme exibido no terminal, 26 componentes e 27 relacionamentos foram consolidados com sucesso."

### 01:45 - 03:00 | Validação Prática no Neo4j Browser
* **Ambiente Visual:** Painel do Neo4j Browser conectado à instância ativa.
* **Execução ao Vivo:**
  1. Consulta geral da topologia:
     ```cypher
     MATCH (n:Componente) RETURN n LIMIT 25;
     ```
     (Demonstração da visualização gráfica com nós coloridos e arestas direcionadas).
  2. Consulta de múltiplos saltos a partir da disciplina de Algoritmos (análoga à questão da lista prática):
     ```cypher
     MATCH path = (alg:Componente {codigo: 'TADS01'})-[:E_PRE_REQUISITO_DE*1..3]->(alvo)
     RETURN path;
     ```
* **Locução (Natanael Lucas):**
  > "No ambiente do Neo4j Browser, observamos a topologia do grafo. Cada nó representa um componente curricular e cada aresta direcionada expressa a relação E_PRE_REQUISITO_DE.
  > Ao executarmos a consulta de travessia profunda partindo de Algoritmos e Lógica de Programação, recuperamos instantaneamente todas as disciplinas destravadas em até 3 saltos de dependência.
  > Graças à Adjacência Livre de Índices do Neo4j, o custo dessa busca é resolvido diretamente por ponteiros de memória em milissegundos, sem requerer múltiplos JOINs sucessivos ou recursão analítica pesada."

### 03:00 - 04:00 | Análise com NetworkX e Métricas Topológicas
* **Ambiente Visual:** Terminal ou Jupyter Lab executando o módulo `src/analysis/graph_metrics.py`.
* **Execução ao Vivo:**
  1. Exibição da validação de DAG e da tabela de *Betweenness Centrality*.
  2. Apresentação visual rápida das figuras geradas em `reports/figures/`.
* **Locução (Natanael Lucas):**
  > "Para a análise implícita dos dados, integramos o banco Neo4j à biblioteca NetworkX em Python.
  > O algoritmo confirmou matematicamente que a estrutura é um grafo direcionado acíclico, livre de ciclos temporais.
  > O cálculo da centralidade de intermediação revelou que disciplinas como Desenvolvimento Web I e Projeto Integrador I são os maiores gargalos estruturais da formação, pois concentram o fluxo curricular até o TCC.
  > Além disso, o algoritmo de caminho mais longo em DAG estabeleceu que a cadeia crítica mínima de formatura exige 5 períodos letivos ininterruptos."

### 04:00 - 04:30 | Encerramento e Apresentação do Repositório
* **Ambiente Visual:** Página inicial do repositório no GitHub (`https://github.com/pedrodavi120/grafos-fcd`), com destaque para a suíte de testes passando com 100% de sucesso.
* **Locução (Natanael Lucas):**
  > "O repositório completo com a documentação do projeto, cadernos Jupyter e a suíte de testes automatizados está acessível publicamente no GitHub.
  > Concluímos, portanto, que a validação comprovou a eficiência e a expressividade do modelo de grafos para dados pedagógicos e relacionais complexos. Muito obrigado."

---

## 3. Lista de Verificação Prévia à Gravação
* [ ] Instância local do Neo4j ou conexão com o Neo4j AuraDB testada e operacional.
* [ ] Resolução e escala do terminal configuradas com fonte legível (tamanho 16 ou superior).
* [ ] Janela do navegador com o Neo4j Browser configurada com contraste adequado e zoom em 110%.
* [ ] Limpeza prévia do histórico do terminal para uma apresentação nítida.
