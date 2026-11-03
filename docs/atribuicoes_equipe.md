# Atribuições da Equipe e Guia da Apresentação Oral

**Unidade Curricular:** Fundamentos e Técnicas em Ciência de Dados  
**Docente:** Prof. Dr. Josenalde Oliveira  
**Curso:** Análise e Desenvolvimento de Sistemas (TADS) — EAJ / UFRN  
**Data da Apresentação:** 04/11/2026  
**Tempo Limite da Apresentação:** 15 minutos (tempo de fala planejado: 14 minutos)

---

## 1. Atribuições Operacionais do Trabalho

* **Pedro Davi:** Responsável pelo desenvolvimento da base de código, estruturação do repositório segundo o padrão Cookiecutter Data Science, scripts de processamento de dados e testes automatizados.
* **Cleiton Mizael:** Responsável pela elaboração formal dos diapositivos da apresentação (baseado no roteiro consolidado em `docs/slides_roteiro.md`) e pela estruturação dos tópicos teóricos de bases em grafos.
* **Natanael Lucas:** Responsável pela gravação e edição técnica do vídeo demonstrativo (duração de 3 a 5 minutos, conforme o guião em `docs/roteiro_video.md`), evidenciando a execução do código, o Neo4j Browser e as análises em Python.

---

## 2. Divisão de Fala na Apresentação Oral (14 Minutos)

Para assegurar a participação equilibrada de todos os integrantes no limite estrito de 15 minutos estabelecido pela disciplina, a distribuição dos temas e tempos foi definida da seguinte forma:

### Bloco 1: Pedro Davi (00:00 - 03:45 | Duração: 03 min e 45 s)
* **Diapositivos 01 a 03:**
  1. **Abertura e Contextualização (00:00 - 01:15):**
     - Apresentação da equipe de discentes (TADS/EAJ/UFRN) e do objetivo central: validação empírica de bases de dados orientadas a grafos (Neo4j & Cypher) para resolução de problemas de redes densamente conectadas sem uso de dados sintéticos.
  2. **O Problema Relacional e NoSQL Documental (01:15 - 02:30):**
     - Demonstração dos gargalos discutidos em aula:
       - Em bancos relacionais, a resolução de dependências recursivas exige múltiplos `JOIN`s sucessivos ou expressões de tabela comuns (`WITH RECURSIVE`), com degradação exponencial de desempenho computacional à medida que a profundidade da busca aumenta.
       - Em bancos NoSQL orientados a documentos, a exemplo do MongoDB trabalhado na lista de exercícios (coleção `grade_curricular`), o uso de vetores de strings para pré-requisitos atende a buscas de um único salto, porém inviabiliza travessias recursivas eficientes sem agregações custosas.
  3. **Data Product Canvas (02:30 - 03:45):**
     - Apresentação sintética dos 8 blocos do canvas (framework conceitual de Leandro S. Carvalho): explicitação do problema, usuários-alvo (coordenação e corpo discente), proposta de valor (consultas de percursos em tempo constante por salto) e métricas de sucesso. Transição formal da palavra para Cleiton Mizael.

---

### Bloco 2: Cleiton Mizael (03:45 - 09:00 | Duração: 05 min e 15 s)
* **Diapositivos 04 a 06:**
  4. **Fundamentação em Grafos e Tecnologia Neo4j (03:45 - 05:15):**
     - Definição matemática de um grafo direcionado $G = (V, E)$ e do modelo *Labeled Property Graph* (LPG): nós, rótulos, arestas direcionadas tipadas e propriedades em pares chave-valor.
     - Explicação da propriedade arquitetural fundamental: **Adjacência Livre de Índices** (*Index-Free Adjacency*), em que cada nó mantém ponteiros diretos em memória física para os nós vizinhos, garantindo que o custo de percurso de cada salto seja de complexidade $O(1)$, independentemente do volume total de dados da base.
  5. **A Linguagem Cypher e a Modelagem Curricular (05:15 - 07:00):**
     - Sintaxe declarativa e visual inspirada em caracteres ASCII: `(c:Componente)-[:E_PRE_REQUISITO_DE]->(d:Componente)`.
     - Ingestão atômica e idempotente por meio de `UNWIND` e `MERGE` combinados com restrições de unicidade (`CREATE CONSTRAINT`).
     - Consultas com travessias de profundidade arbitrária (`[:E_PRE_REQUISITO_DE*1..3]`).
  6. **Arquitetura de Engenharia com Cookiecutter Data Science (07:00 - 09:00):**
     - Descrição da organização do repositório: imutabilidade dos dados brutos em `data/raw`, modularização do código em `src/`, isolamento de credenciais via `.env.example`, automação com `Makefile` e verificação por testes automatizados. Transição formal da palavra para Natanael Lucas.

---

### Bloco 3: Natanael Lucas (09:00 - 14:00 | Duração: 05 min e 00 s)
* **Diapositivos 07 a 09:**
  7. **Pipeline Analítico: Análise Explícita vs. Implícita (09:00 - 10:45):**
     - Enquadramento nas categorias analíticas ministradas pelo docente no material `ds06.pdf`:
       - **Análise Exploratória (AED):** Distribuição da carga horária e concentração de disciplinas por semestre e área temática (Pandas e Seaborn).
       - **Análise Explícita:** Consultas diretas em Cypher correspondendo à questão prática de pré-requisitos da lista da disciplina.
       - **Análise Implícita:** Integração do Neo4j com Python e a biblioteca `NetworkX` para a descoberta de padrões estruturais ocultos na rede.
  8. **Resultados Empíricos e Métricas de Rede (10:45 - 12:45):**
     - Apresentação quantitativa das métricas calculadas:
       - **Grau de Saída (*Out-Degree*):** Confirmação de *Algoritmos e Lógica de Programação* (TADS01) e *Bancos de Dados* (TADS08) como as maiores provedoras curriculares.
       - **Centralidade de Intermediação (*Betweenness*):** Identificação de *Desenvolvimento Web I* e *Projeto Integrador I* como as principais disciplinas-ponte da matriz, cujo eventual trancamento gera retenção em cadeia.
       - **Caminho Crítico de Formatura:** Determinação do caminho mais longo em grafo acíclico, evidenciando uma sequência obrigatória de 5 períodos letivos ininterruptos.
  9. **Conclusão e Entregas (12:45 - 14:00):**
     - Síntese da validação: viabilidade técnica e superioridade da modelagem em grafos para problemas altamente interconectados.
     - Disponibilização do endereço do repositório no GitHub (`https://github.com/pedrodavi120/grafos-fcd`), menção ao vídeo demonstrativo gravado e abertura para arguição da banca.

---

## 3. Recomendações de Execução para a Apresentação
* Manter o cronômetro visível para a equipe desde o início da fala do primeiro integrante.
* Realizar transições de fala objetivas e sem interrupções de fluxo de tela.
* Assegurar que os diapositivos estejam centralizados no formato PDF para evitar problemas de compatibilidade no equipamento de projeção da sala.
