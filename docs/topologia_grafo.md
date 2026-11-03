# Especificação Formal da Topologia do Grafo: Labeled Property Graph (LPG)

Documento técnico que formaliza a modelagem de dados da validação tecnológica **GraphCurriculum-FCD**, em conformidade com as diretrizes da disciplina de **Fundamentos e Técnicas em Ciência de Dados** (TADS / EAJ — UFRN).

---

## 1. Nós (Nodes / Vértices)

### Rótulo (*Label*): `:Componente`

Representa uma unidade curricular formalmente ofertada na matriz pedagógica do curso de Tecnologia em Análise e Desenvolvimento de Sistemas (TADS / EAJ — UFRN).

| Propriedade | Tipo de Dado Neo4j | Restrição / Índice | Descrição Semântica | Exemplo de Instância |
|---|---|---|---|---|
| `codigo` | String | **UNIQUE CONSTRAINT** | Código identificador alfanumérico unívoco da disciplina | `"TAD0102"` |
| `nome` | String | Indexado | Nome oficial do componente curricular | `"ALGORITMOS E PROGRAMACAO"` |
| `ch` | Integer | - | Carga horária total do componente (horas) | `90` |
| `semestre` | Integer | **SECONDARY INDEX** | Período letivo sugerido para cursar (1 a 6) | `1` |
| `natureza` | String | - | Categoria formativa: `"Obrigatoria"` ou `"Optativa"` | `"Obrigatoria"` |
| `area` | String | - | Eixo formativo ou área temática de concentração | `"Programacao"`, `"Dados"`, `"Engenharia"` |

---

## 2. Relacionamentos (Relationships / Arestas Direcionadas)

### Rótulo do Tipo: `[:E_PRE_REQUISITO_DE]`

Formaliza a dependência pedagógica direta existente entre dois componentes curriculares.

* **Assinatura Direcionada:** `(origem:Componente)-[:E_PRE_REQUISITO_DE]->(destino:Componente)`
* **Semântica:** O componente `origem` deve ser obrigatoriamente cursado e concluído com aprovação antes que o estudante possa realizar matrícula no componente `destino`.
* **Propriedades da Aresta:**
  - `tipo`: String (armazenada com o valor constante `"E_PRE_REQUISITO_DE"` para consultas parametrizadas).

---

## 3. Propriedades Estruturais e Teoria de Grafos

* **Classificação Formal:** Grafo Direcionado Acíclico (DAG — *Directed Acyclic Graph*), denotado por $G = (V, E)$, no qual $V$ corresponde ao conjunto finito de disciplinas e $E \subseteq V \times V$ ao conjunto de pré-requisitos direcionados.
* **Verificação de Aciclicidade:** O grafo foi formalmente validado contra a presença de ciclos temporais ou inconsistências circulares mediante o algoritmo de ordenação topológica da biblioteca `NetworkX`:
  $$\text{nx.is\_directed\_acyclic\_graph}(G) = \text{True}$$
* **Adjacência Livre de Índices (*Index-Free Adjacency*):** Cada nó componente mantém referências diretas em memória física para seus vizinhos de entrada e de saída. O percurso de um salto arbitrário apresenta custo computacional de tempo constante $O(1)$, conferindo ao Neo4j superioridade teórica e prática frente a junções relacionais indexadas por árvores B-Tree ($O(N \log M)$ por nível de junção).
