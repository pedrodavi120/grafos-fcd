# script de limpeza e preparacao dos dados das disciplinas e pre-requisitos
import sys
from pathlib import Path
import pandas as pd

sys.path.append(str(Path(__file__).resolve().parent.parent.parent))
from src.config import RAW_DATA_DIR, PROCESSED_DATA_DIR


def process_disciplinas(input_path: Path) -> pd.DataFrame:
    # le os dados das disciplinas e valida tipos basicos
    if not input_path.exists():
        raise FileNotFoundError(f"arquivo nao encontrado: {input_path}")

    df = pd.read_csv(input_path, encoding="utf-8")

    # remove espacos soltos nas strings
    for col in ["codigo", "nome", "natureza", "area"]:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()

    # converte valores numericos
    df["ch"] = pd.to_numeric(df["ch"], errors="raise").astype(int)
    df["semestre"] = pd.to_numeric(df["semestre"], errors="raise").astype(int)

    # garante que nao tem codigo repetido
    if df["codigo"].duplicated().any():
        dups = df[df["codigo"].duplicated()]["codigo"].tolist()
        raise ValueError(f"codigos duplicados detectados: {dups}")

    return df


def process_prerequisitos(input_path: Path, codigos_validos: set) -> pd.DataFrame:
    # le os pre-requisitos e checa integridade referencial
    if not input_path.exists():
        raise FileNotFoundError(f"arquivo nao encontrado: {input_path}")

    df = pd.read_csv(input_path, encoding="utf-8")

    for col in ["codigo_origem", "codigo_destino", "tipo_relacao"]:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()

    # tira linhas duplicadas se houver
    df = df.drop_duplicates(subset=["codigo_origem", "codigo_destino"])

    # checa se alguma disciplina nao existe na tabela de disciplinas
    origens_invalidas = set(df["codigo_origem"]) - codigos_validos
    destinos_invalidos = set(df["codigo_destino"]) - codigos_validos

    if origens_invalidas:
        raise ValueError(f"disciplinas de origem inexistentes: {origens_invalidas}")
    if destinos_invalidos:
        raise ValueError(f"disciplinas de destino inexistentes: {destinos_invalidos}")

    # evita que uma disciplina seja pre-requisito dela mesma
    auto_rel = df[df["codigo_origem"] == df["codigo_destino"]]
    if not auto_rel.empty:
        raise ValueError("disciplina nao pode ser pre-requisito de si mesma")

    return df


def main():
    # cria pasta processed e roda o pipeline de dados
    print("processando dados brutos da matriz curricular...")
    PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)

    raw_disc = RAW_DATA_DIR / "tads_disciplinas.csv"
    raw_pre = RAW_DATA_DIR / "tads_prerequisitos.csv"

    # processa disciplinas
    df_disc = process_disciplinas(raw_disc)
    codigos_validos = set(df_disc["codigo"])
    out_disc = PROCESSED_DATA_DIR / "nodes_componentes.csv"
    df_disc.to_csv(out_disc, index=False, encoding="utf-8")
    print(f"disciplinas salvas: {len(df_disc)} em {out_disc}")

    # processa pre-requisitos
    df_pre = process_prerequisitos(raw_pre, codigos_validos)
    out_pre = PROCESSED_DATA_DIR / "edges_prerequisitos.csv"
    df_pre.to_csv(out_pre, index=False, encoding="utf-8")
    print(f"arestas de pre-requisitos salvas: {len(df_pre)} em {out_pre}")
    print("dados processados com sucesso.")


if __name__ == "__main__":
    main()
