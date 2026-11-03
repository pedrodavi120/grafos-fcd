# Guia de Referência: Cypher Query Language (Neo4j)

Este documento compila as consultas declarativas em Cypher empregadas na validação tecnológica do **GraphCurriculum-FCD**, correlacionando a sintaxe de grafos com os paradigmas relacional (SQL) e documental (MongoDB MQL).

---

## 1. Fundamentos da Sintaxe Declarativa Cypher

A linguagem Cypher adota uma notação visual inspirada em caracteres ASCII para expressar nós e relacionamentos:
* `(n)`: Representa um **Nó** (*Node* / Vértice).
* `(c:Componente)`: Representa um nó portador do rótulo (*Label*) `Componente`.
* `(c:Componente {codigo: 'TADS01'})`: Nó com propriedades (*Properties*) específicas.
* `-->` ou `<--`: Representa um **Relacionamento Direcionado** (*Relationship* / Aresta).
* `-[r:E_PRE_REQUISITO_DE]->`: Relacionamento tipado com identificador `r`.
* `(origem)-[:E_PRE_REQUISITO_DE]->(destino)`: Padrão completo de travessia direcionada.

---

## 2. DDL: Criação de Restrições e Índices

### Restrição de Unicidade (Garante integridade referencial)
```cypher
CREATE CONSTRAINT unique_componente_codigo IF NOT EXISTS
FOR (c:Componente)
REQUIRE c.codigo IS UNIQUE;
```

### Índice Secundário (Otimiza filtros por período letivo)
```cypher
CREATE INDEX idx_componente_semestre IF NOT EXISTS
FOR (c:Componente)
ON (c.semestre);
```

---

## 3. DML: Ingestão em Lote Idempotente

### Inserção Atômica de Nós com `UNWIND` + `MERGE`
```cypher
UNWIND $batch AS comp
MERGE (c:Componente {codigo: comp.codigo})
SET c.nome = comp.nome,
    c.ch = toInteger(comp.ch),
    c.semestre = toInteger(comp.semestre),
    c.natureza = comp.natureza,
    c.area = comp.area;
```

### Inserção Atômica de Arestas com `UNWIND` + `MERGE`
```cypher
UNWIND $relacoes AS rel
MATCH (origem:Componente {codigo: rel.codigo_origem})
MATCH (destino:Componente {codigo: rel.codigo_destino})
MERGE (origem)-[r:E_PRE_REQUISITO_DE]->(destino)
RETURN count(r) AS total_relacoes;
```

---

## 4. DQL: Consultas Analíticas (Explícitas e Múltiplos Saltos)

### 4.1 Consulta Direta (Equivalente à Questão 7.1 da Lista de Exercícios)
*"Quais disciplinas possuem Algoritmos (TADS01) como pré-requisito direto?"*
```cypher
MATCH (alg:Componente {codigo: 'TADS01'})-[:E_PRE_REQUISITO_DE]->(dep:Componente)
RETURN dep.codigo AS Codigo, dep.nome AS Nome, dep.semestre AS Semestre
ORDER BY dep.semestre;
```

### 4.2 Travessia de Profundidade Arbitrária (*k-hop*)
*"Quais são todas as disciplinas destravadas na cadeia de dependência até o 3º nível a partir de Algoritmos?"*
```cypher
MATCH path = (alg:Componente {codigo: 'TADS01'})-[:E_PRE_REQUISITO_DE*1..3]->(alvo:Componente)
RETURN alvo.codigo AS Codigo, alvo.nome AS Componente, length(path) AS DistanciaSaltos
ORDER BY DistanciaSaltos, alvo.semestre;
```

### 4.3 Rastreabilidade Reversa (Ancestrais de Conclusão de Curso)
*"Quais são todos os pré-requisitos diretos e indiretos para cursar o Projeto Integrador II (TADS25)?"*
```cypher
MATCH path = (origem:Componente)-[:E_PRE_REQUISITO_DE*1..5]->(fim:Componente {codigo: 'TADS25'})
RETURN origem.codigo AS CodigoPreRequisito, origem.nome AS Disciplina, length(path) AS Nivel
ORDER BY Nivel DESC;
```

### 4.4 Cálculo de Grau de Conectividade (In-Degree & Out-Degree)
```cypher
MATCH (c:Componente)
OPTIONAL MATCH (c)<-[in_rel:E_PRE_REQUISITO_DE]-()
OPTIONAL MATCH (c)-[out_rel:E_PRE_REQUISITO_DE]->()
RETURN c.codigo AS Codigo,
       c.nome AS Nome,
       count(DISTINCT in_rel) AS PreRequisitosExigidos,
       count(DISTINCT out_rel) AS DisciplinasQueDestrava
ORDER BY DisciplinasQueDestrava DESC;
```

---

## 5. Comparativo Arquitetural: Cypher vs. SQL vs. MongoDB

| Critério Analítico | SQL Relacional (SGBD-R) | MongoDB (MQL Documental) | Neo4j (Cypher em Grafos) |
|---|---|---|---|
| **Busca em 1 salto** | Junção `JOIN` com chaves estrangeiras | Operadores `$lookup` ou `$in` em vetores | `(a)-[:REL]->(b)` |
| **Busca em N saltos** | `WITH RECURSIVE` (complexa e onerosa) | Inviável em escala sem ETL prévio | `(a)-[:REL*1..N]->(b)` |
| **Index-Free Adjacency** | Inexistente (varreduras em índices a cada junção) | Inexistente (varreduras em índices de coleção) | Nativa (ponteiros diretos de memória física) |
| **Complexidade Temporal** | $O(N \log M)$ por nível de junção | $O(N)$ em coleções não normalizadas | $O(1)$ por salto percorrido |
