# %% [markdown]
# # Interactive Python in VS Code
# Run a cell with **Shift+Enter**. Variables stay available in the Interactive
# Window, so you can run later cells independently and inspect values inline.

# %%
import numpy as np
import pandas as pd

# %% [markdown]
# ## Create data and inspect it

# %%
days = np.arange(1, 8)
temperatures = np.array([18, 20, 19, 23, 25, 22, 21])

weather = pd.DataFrame({"day": days, "temperature_c": temperatures})
weather

# %% [markdown]
# ## Reuse variables and filter interactively

# %%
warm_days = weather[weather["temperature_c"] >= 22]
warm_days

# %% [markdown]
# ## Define a function, then call it in another cell

# %%
def celsius_to_fahrenheit(celsius):
    """Convert a temperature from Celsius to Fahrenheit."""
    return celsius * 9 / 5 + 32

# %%
weather["temperature_f"] = celsius_to_fahrenheit(weather["temperature_c"])
weather

# %% [markdown]
# Change a value above and rerun just the cell to see the results update.
