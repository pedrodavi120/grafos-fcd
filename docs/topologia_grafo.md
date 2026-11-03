# Especificação da Topologia do Grafo: Labeled Property Graph (LPG)

Especificação técnica do modelo de dados em grafos utilizado no projeto **GraphCurriculum-FCD**.

---

## 1. Nós (Nodes / Vértices)

### Rótulo (*Label*): `:Componente`

Representa uma unidade curricular ofertada na matriz pedagógica de TADS / EAJ - UFRN.

| Propriedade | Tipo Neo4j | Restrição / Índice | Descrição | Exemplo |
|---|---|---|---|---|
| `codigo` | String | **UNIQUE CONSTRAINT** | Código identificador único do componente | `"TADS01"` |
| `nome` | String | Indexado | Nome oficial da disciplina | `"Algoritmos e Logica de Programacao"` |
| `ch` | Integer | - | Carga horária total em horas | `90` |
| `semestre` | Integer | **INDEX** | Período letivo sugerido (1 a 6) | `1` |
| `natureza` | String | - | `"Obrigatoria"` ou `"Optativa"` | `"Obrigatoria"` |
| `area` | String | - | Área do conhecimento | `"Programacao"`, `"Dados"`, `"Engenharia"` |

---

## 2. Arestas (Relationships / Arestas Direcionadas)

### Tipo: `[:E_PRE_REQUISITO_DE]`

Estabelece a dependência pedagógica direta entre dois componentes curriculares.

* **Direção:** `(origem:Componente)-[:E_PRE_REQUISITO_DE]->(destino:Componente)`
* **Semântica:** O componente `origem` deve ser cursado e aprovado com sucesso antes de o aluno matricular-se no componente `destino`.
* **Propriedades:**
  - `tipo`: String (padrão `"E_PRE_REQUISITO_DE"`).

---

## 3. Propriedades Estruturais da Topologia

* **Natureza da Rede:** Grafo Direcionado Acíclico (DAG - *Directed Acyclic Graph*).
* **Ausência de Ciclos:** Rigorosamente comprovada matematicamente via `nx.is_directed_acyclic_graph(G) == True`.
* **Densidade de Arestas:** Proporção moderada, refletindo a estrutura de dependências do curso superior.
* **Componentes Conexos:** O grafo é conexo na sua grande maioria através de Algoritmos (TADS01), com pequenos subgrafos isolados para disciplinas instrumentais (ex.: Metodologia e Governança).

