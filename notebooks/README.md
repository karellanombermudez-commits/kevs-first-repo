Notebooks are for exploration. Nothing in `src/` or `app/` imports from here.

- `python/` — `.ipynb`, or `.py` files with `# %%` cells for the VS Code interactive window
- `r/` — `.R` / `.Rmd`; open the repo as an RStudio project (`project.Rproj`)
- `quarto/` — `.qmd` mixing R and Python chunks; `quarto render` writes to `reports/`

Naming: `NN-initials-topic` e.g. `01-lr-eda.ipynb`, `02-cm-baseline.py`.

Outputs are stripped on commit by nbstripout. If a result matters, save the
figure to `reports/figures/` or the table to `data/interim/`.
