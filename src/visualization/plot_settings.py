"""Shared matplotlib/seaborn style so every figure in reports/ looks the same."""
import matplotlib.pyplot as plt
import seaborn as sns


def set_style() -> None:
    sns.set_theme(style="whitegrid", context="notebook")
    plt.rcParams.update({"figure.figsize": (8, 5), "figure.dpi": 110, "savefig.bbox": "tight"})
