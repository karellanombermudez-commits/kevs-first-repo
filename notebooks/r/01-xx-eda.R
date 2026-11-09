# EDA in R. Reads the same Parquet the Python side writes.
library(arrow)
library(dplyr)
library(ggplot2)
source("R/utils.R")

df <- read_parquet("data/processed/clean.parquet")
glimpse(df)

df |>
  ggplot(aes(feature_1, feature_2, colour = factor(target))) +
  geom_point(alpha = .5) +
  theme_minimal()

# Hand results back to Python as Parquet, never CSV:
# write_parquet(df_summary, "data/interim/r_summary.parquet")
