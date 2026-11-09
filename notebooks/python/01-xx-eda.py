# %% [markdown]
# # EDA — run cells with Shift+Enter in VS Code
# %%
import pandas as pd
from src.config import CLEAN_PATH
from src.visualization.plot_settings import set_style
set_style()

df = pd.read_parquet(CLEAN_PATH)   # run `make fake-data` first if this fails
df.describe()
# %%
df["target"].value_counts()
