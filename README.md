# Data Science → ML → Deployment Project Template

Based on [daveebbelaar/data-science-template](https://github.com/daveebbelaar/data-science-template)
(itself based on [Cookiecutter Data Science](https://drivendata.github.io/cookiecutter-data-science/)),
extended for a team that:

1. explores and cleans data in **Python and R** (Jupyter / VS Code interactive cells / RStudio),
2. writes up findings with **Quarto**,
3. trains **ML / deep-learning** models,
4. ships them through a **Streamlit** app, a **FastAPI** service, and/or a static **website**.

## Folder map

```
├── data/                 ← git-ignored except .gitkeep and schema.md
│   ├── raw/              original, immutable
│   ├── external/         third-party sources
│   ├── interim/          intermediate transforms
│   ├── processed/        final clean data (Parquet) that models consume
│   └── schema.md         THE CONTRACT: columns + types of processed data
│
├── notebooks/            exploration only — nothing here is imported by code
│   ├── python/           .ipynb or .py with # %% cells
│   ├── r/                .R scripts / .Rmd
│   └── quarto/           .qmd (R + Python chunks), rendered to reports/
│
├── src/                  Python package: all reusable logic lives here
│   ├── config.py         paths and settings, read once everywhere
│   ├── data/             make_dataset.py    raw → processed
│   ├── features/         build_features.py  processed → model input
│   ├── models/           train_model.py, predict_model.py, deep_learning/
│   └── visualization/    plot_settings.py, visualize.py
│
├── R/                    reusable R functions (sourced by notebooks/r and quarto)
│
├── models/               saved weights / pickles — git-ignored, tracked by DVC or Drive
│
├── app/
│   ├── streamlit/        dashboard (app.py + pages/)
│   ├── api/              FastAPI service wrapping predict()
│   └── web/              static site / frontend
│
├── deploy/               Dockerfiles, docker-compose, Procfile, cloud configs
├── reports/figures/      rendered Quarto output and exported plots
├── tests/                pytest for src/ (the contracts are tested here)
├── docs/                 setup notes, decisions, data dictionary
├── references/           papers, manuals, folder_structure.txt
│
├── pyproject.toml        Python deps (pip install -e ".[dev,app]")
├── requirements.txt      pinned export for deployment
├── renv.lock             R deps (renv::restore())
├── _quarto.yml           Quarto project config
├── Makefile              make data / train / app / api / report
├── .env.example          secrets template — copy to .env (git-ignored)
└── .github/workflows/    CI: lint + tests on every PR
```

## Setup

```bash
git clone <repo> && cd <repo>
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -e ".[dev,app]"
cp .env.example .env
pre-commit install                                      # strips notebook outputs on commit
```

R users (optional):
```r
install.packages("renv"); renv::restore()
```

Quarto: install from https://quarto.org, then `quarto render`.

## Daily workflow

```bash
git checkout main && git pull
git checkout -b <yourname>/<short-task>
# ... work ...
git add -A && git commit -m "..." && git push -u origin HEAD
# open a Pull Request on GitHub; one teammate reviews, then merge
```

## The two contracts

Everything parallel in this project depends on two agreed interfaces. Change them only by PR.

**1. Data → Model**: `data/processed/clean.parquet` with the columns in `data/schema.md`.
Modelers code against `make fake-data` until the real file exists.

**2. Model → App**: `src/models/predict_model.py::predict(df) -> df`
and a saved artifact at `models/latest/`. The app imports only this function.
`src/models/predict_model.py` ships with a stub that returns random predictions so
the app can be built before the model exists.

## Make targets

| command            | what it does                                      |
|--------------------|---------------------------------------------------|
| `make data`        | raw → `data/processed/clean.parquet`              |
| `make fake-data`   | writes a schema-correct dummy parquet for dev     |
| `make train`       | trains and saves to `models/latest/`              |
| `make app`         | runs the Streamlit dashboard                      |
| `make api`         | runs the FastAPI server                           |
| `make report`      | `quarto render` → `reports/`                      |
| `make test`        | pytest                                            |
| `make lint`        | ruff                                              |

## Team ownership (edit for your project)

| area                  | owner | folders                             |
|-----------------------|-------|-------------------------------------|
| data cleaning & EDA   |       | `notebooks/`, `src/data`, `R/`, `data/schema.md` |
| model                 |       | `src/features`, `src/models`, `models/` |
| app & deployment      |       | `app/`, `deploy/`, `.github/`       |
| docs & integration    |       | `docs/`, `README`, PR reviews       |

## Notebook rules

- Notebooks are scratch. Once logic is stable, move it into `src/` or `R/` and import it.
- Outputs are stripped on commit (`nbstripout` via pre-commit) so notebooks don't cause merge conflicts.
- Python ↔ R handoff is always Parquet, never CSV: `arrow::write_parquet()` / `pd.read_parquet()`.

## Deployment options

- **Streamlit Community Cloud** — point it at `app/streamlit/app.py`. Easiest.
- **Docker** — `deploy/Dockerfile.api` and `Dockerfile.streamlit`; `docker compose up` runs both.
- **Static website** — `app/web/` deploys to GitHub Pages / Netlify; it calls the API for predictions.
- **Quarto site** — `quarto publish gh-pages` turns `notebooks/quarto/` into a project website.
