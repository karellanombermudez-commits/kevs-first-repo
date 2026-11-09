"""Deep-learning variant of train_model.py. Same inputs, same output location.

Run:  python -m src.models.deep_learning.train_torch
Requires:  pip install -e ".[dl]"
"""
import json
import numpy as np
import pandas as pd
import torch
from torch import nn
from sklearn.model_selection import train_test_split

from src.config import CLEAN_PATH, MODEL_DIR, SEED
from src.features.build_features import split_xy

torch.manual_seed(SEED)


class MLP(nn.Module):
    def __init__(self, d_in: int):
        super().__init__()
        self.net = nn.Sequential(nn.Linear(d_in, 64), nn.ReLU(), nn.Linear(64, 1))

    def forward(self, x):
        return self.net(x).squeeze(-1)


def main(epochs: int = 20) -> None:
    X, y = split_xy(pd.read_parquet(CLEAN_PATH))
    Xtr, Xte, ytr, yte = train_test_split(X, y, test_size=0.2, random_state=SEED)
    to_t = lambda a: torch.tensor(np.asarray(a, dtype=np.float32))
    Xtr_t, ytr_t, Xte_t, yte_t = map(to_t, (Xtr, ytr, Xte, yte))

    model = MLP(Xtr.shape[1])
    opt = torch.optim.Adam(model.parameters(), lr=1e-3)
    loss_fn = nn.BCEWithLogitsLoss()
    for _ in range(epochs):
        opt.zero_grad()
        loss_fn(model(Xtr_t), ytr_t).backward()
        opt.step()

    with torch.no_grad():
        acc = ((model(Xte_t) > 0).float() == yte_t).float().mean().item()
    torch.save(model.state_dict(), MODEL_DIR / "model.pt")
    (MODEL_DIR / "columns.json").write_text(json.dumps(list(X.columns)))
    (MODEL_DIR / "metrics.json").write_text(json.dumps({"accuracy": acc}, indent=2))
    print(f"saved to {MODEL_DIR}  accuracy={acc:.3f}")
    # NOTE: to serve this, extend predict_model._load() to build MLP and load model.pt


if __name__ == "__main__":
    main()
