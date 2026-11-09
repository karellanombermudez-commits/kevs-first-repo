# Setup by tool

## VS Code (Python + R + Quarto in one editor)
Extensions: Python, Jupyter, R (REditorSupport), Quarto, GitLens.
Select the `.venv` interpreter. For R: `install.packages("languageserver")`.

## RStudio
Open `project.Rproj`. Quarto and git panel are built in. `renv::restore()`.

## JupyterLab
`jupyter lab` from the repo root. R kernel: `install.packages("IRkernel"); IRkernel::installspec()`.

## Google Colab (GPU training)
Clone the repo in a cell, `pip install -e .`, pull data from Drive, run
`python -m src.models.deep_learning.train_torch`, then copy `models/latest/` back.
