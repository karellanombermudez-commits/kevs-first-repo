.PHONY: data fake-data features train app api report test lint clean

PY := python

data:
	$(PY) -m src.data.make_dataset

fake-data:
	$(PY) -m src.data.make_dataset --fake

features:
	$(PY) -m src.features.build_features

train:
	$(PY) -m src.models.train_model

app:
	streamlit run app/streamlit/app.py

api:
	uvicorn app.api.main:app --reload --port 8000

report:
	quarto render

test:
	pytest -q

lint:
	ruff check . && ruff format --check .

clean:
	rm -rf data/interim/* data/processed/* reports/*.html .quarto
