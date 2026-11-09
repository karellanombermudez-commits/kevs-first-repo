import pandas as pd
import matplotlib.pyplot as plt
from src.config import FIGURES
from src.visualization.plot_settings import set_style


def save_fig(name: str) -> None:
    plt.savefig(FIGURES / f"{name}.png")
    plt.close()


def target_balance(df: pd.DataFrame) -> None:
    set_style()
    df["target"].value_counts().plot.bar()
    plt.title("Target balance")
    save_fig("target_balance")
