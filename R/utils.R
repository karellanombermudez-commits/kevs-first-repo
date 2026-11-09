# Reusable R helpers. Source from notebooks/r or Quarto with source("R/utils.R").

read_clean <- function(path = "data/processed/clean.parquet") {
  arrow::read_parquet(path)
}

theme_project <- function() {
  ggplot2::theme_minimal(base_size = 13)
}
