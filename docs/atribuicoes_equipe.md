# Atribuições da Equipe e Guia Estratégico da Apresentação Oral

**Unidade Curricular:** Fundamentos e Técnicas em Ciência de Dados  
**Docente:** Prof. Dr. Josenalde Oliveira  
**Curso:** Análise e Desenvolvimento de Sistemas (TADS) — EAJ / UFRN  
**Grupo:** G1 — T7: Banco de Dados Baseado em Grafos (Neo4j & Cypher)  
**Data da Apresentação:** Quarta-feira, 04/11/2026, às 07h50 (Abertura dos Seminários)  
**Tempo Limite:** Estritamente 15 minutos (tempo de fala planejado: 13m45s a 14m00s)

---

## 1. Diretrizes Estratégicas do Docente (Atualização 27/10)

1. **Estrutura Obrigatória da Apresentação:**
   - **Teoria Envolvida:** Grafos direcionados $G = (V, E)$, taxonomia NoSQL (`ds05.pdf`), modelo Labeled Property Graph (LPG) e Adjacência Livre de Índices (*Index-Free Adjacency*).
   - **Descrição da Ferramenta:** SGBD Neo4j (armazenamento nativo, transações ACID) e a linguagem declarativa Cypher.
   - **Prova de Conceito (PoC como Diferencial):** Validação prática com a matriz curricular real do TADS (UFRN/EAJ), integração com NetworkX e dashboard PoC em Streamlit (`app.py`).
2. **Recomendação Estrita Anti-Falha:**
   - **Evitar demonstração ao vivo** via terminal para não perder tempo com conexão ou "efeito demonstração".
   - **Exibir o vídeo curto demonstrativo (ou capturas de tela em alta definição já salvas)** focado na funcionalidade durante a fala do Natanael.
3. **Logística de Sala:**
   - Início pontual às 07h50 (a equipe abre a sessão como G1).
   - Conexão via cabo HDMI (levar adaptador caso necessário).

---

## 2. Divisão Operacional de Entregas

* **Pedro Davi:** Responsável pela arquitetura do repositório de código no padrão Cookiecutter Data Science, scripts de processamento de dados, modelo relacional de grafos e suíte de testes automatizados.
* **Cleiton Mizael:** Responsável pela montagem e consolidação visual dos diapositivos da apresentação (conforme `docs/slides_roteiro.md`), com foco na teoria e na ferramenta.
* **Natanael Lucas:** Responsável pela gravação e edição do vídeo demonstrativo curto (3 a 5 minutos, conforme `docs/roteiro_video.md`) para ser projetado na apresentação e anexado à entrega do SIGAA.

---

## 3. Divisão de Fala no Seminário (14 Minutos)

### Bloco 1: Pedro Davi (00:00 - 03:45 | Duração: 03 min e 45 s)
* **Diapositivos 01 a 03:**
  1. **Abertura e Contextualização:** Apresentação da equipe G1 (TADS/EAJ/UFRN). Enquadramento na taxonomia NoSQL (`ds04.pdf`/`ds05.pdf`) e justificativa da escolha do problema: a matriz curricular real do TADS/EAJ.
  2. **O Problema Relacional e NoSQL Documental:** Gargalos de `JOINs` múltiplos em SQL clássico e limitações do modelo de documentos com vetores (exercício prático do MongoDB com a coleção `grade_curricular`).
  3. **Data Product Canvas:** Síntese dos 8 blocos (Leandro S. Carvalho), demonstrando a proposta de valor e as métricas de sucesso técnico e educacional. Transição para Cleiton Mizael.

### Bloco 2: Cleiton Mizael (03:45 - 09:00 | Duração: 05 min e 15 s)
* **Diapositivos 04 a 06:**
  4. **Teoria Envolvida e o Modelo LPG:** Grafos direcionados $G = (V, E)$, modelo Labeled Property Graph (nós, rótulos, arestas tipadas e propriedades) e a Adjacência Livre de Índices (*Index-Free Adjacency*, tempo $O(1)$ por salto).
  5. **A Ferramenta Neo4j e a Linguagem Cypher:** SGBD nativo em grafos, sintaxe declarativa em ASCII-art, integridade referencial com `CREATE CONSTRAINT` e carga atômica idempotente via `UNWIND` + `MERGE`.
  6. **Engenharia de Dados (Cookiecutter Data Science):** Organização profissional do projeto (dados imutáveis `raw`, dados higienizados `processed`, código modular `src/`, automação com `Makefile` e ausência de credenciais hardcoded). Transição para Natanael Lucas.

### Bloco 3: Natanael Lucas (09:00 - 14:00 | Duração: 05 min e 00 s)
* **Diapositivos 07 a 09:**
  7. **Pipeline Analítico (Explícita vs. Implícita):** Conexão com o slide `ds06.pdf`: AED inicial (Pandas), Análise Explícita em Cypher (travessia até 3 saltos a partir de Algoritmos) e Análise Implícita em NetworkX.
  8. **A PoC e Resultados da Validação (Exibição do Vídeo / Telas):**
     - Em vez de rodar ao vivo, projetar o vídeo curto ou as telas do Neo4j Browser e as figuras analíticas já exportadas (`reports/figures/`).
     - Explicar as métricas: gargalos de fluxo (*Betweenness Centrality*: Fundamentos e Técnicas em Ciência de Dados - TAD0204, Estruturas de Dados - TAD0020 e Projetos Aplicados I - TAD0156), provedores de pré-requisitos (*Out-Degree*: Algoritmos - TAD0102 e Banco de Dados - TAD0103) e o Caminho Crítico de 5 semestres.
     - Mencionar a interface PoC construída em Streamlit (`app.py`) como diferencial prático abordado nas aulas.
  9. **Conclusões e Encerramento:** Resumo dos aprendizados, link do repositório no GitHub (`https://github.com/pedrodavi120/grafos-fcd`) e abertura para a banca.

---

## 4. Checklist para a Manhã de Quarta-feira (04/11)
* [ ] Chegar às 07h35 na sala de aula para testar a conexão do cabo HDMI do projetor.
* [ ] Slides em formato PDF no pendrive e também salvos localmente no notebook de apresentação.
* [ ] Arquivo de vídeo MP4 salvo localmente (sem depender de conexão de internet no momento da apresentação).
* [ ] Cronômetro do celular posicionado no púlpito para início simultâneo com a fala de Pedro Davi.
