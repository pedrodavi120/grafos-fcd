.PHONY: help setup data ingest metrics figures app test clean

help:
	@echo "Comandos disponíveis:"
	@echo "  make setup     - Instala as dependências do requirements.txt e pacote em modo editável"
	@echo "  make data      - Processa os dados brutos de data/raw para data/processed"
	@echo "  make ingest    - Executa a carga no Neo4j com UNWIND e MERGE"
	@echo "  make metrics   - Calcula as centralidades e caminho crítico com NetworkX"
	@echo "  make figures   - Gera e salva os gráficos analíticos em reports/figures"
	@echo "  make app       - Inicia o dashboard interativo em Streamlit"
	@echo "  make test      - Executa a suíte de testes automatizados"
	@echo "  make clean     - Remove caches e arquivos temporários de compilação"

setup:
	pip install -r requirements.txt
	pip install -e .

data:
	python src/data/make_dataset.py

ingest:
	python src/graph/loader.py

metrics:
	python src/analysis/graph_metrics.py

figures:
	python src/visualization/plot_graph.py

app:
	streamlit run app.py

test:
	python -m unittest discover -s tests -p "test_*.py" -v

clean:
	python -c "import shutil, pathlib; [shutil.rmtree(p) for p in pathlib.Path('.').rglob('__pycache__')]"
	python -c "import shutil, pathlib; [shutil.rmtree(p) for p in pathlib.Path('.').rglob('*.egg-info')]"

