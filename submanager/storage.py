"""
storage.py — carga y guarda Subscription en CSV usando pandas.
"""

from pathlib import Path
from typing import List
import pandas as pd
from datetime import datetime

from .models import Subscription

DATA_DIR = Path.cwd() / "data"
DATA_DIR.mkdir(exist_ok=True)
DATA_FILE = DATA_DIR / "subscriptions.csv"


def load_subscriptions() -> List[Subscription]:
    """Carga suscripciones desde CSV y devuelve lista de Subscription."""
    if not DATA_FILE.exists():
        return []

    df = pd.read_csv(DATA_FILE, dtype=str)
    subs: List[Subscription] = []

    for _, row in df.iterrows():
        try:
            d = {
                "name": row.get("name", ""),
                "price": float(row.get("price", 0.0)),
                "renew_date": row.get("renew_date", ""),
            }
            # if renew_date is empty, set today
            if not d["renew_date"]:
                d["renew_date"] = datetime.today().strftime("%Y-%m-%d")
            subs.append(Subscription.from_dict(d))
        except Exception:
            # saltar filas corruptas
            continue

    return subs


def save_subscriptions(subs: List[Subscription]) -> None:
    """Guarda lista de Subscription en CSV (sobrescribe)."""
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    if not subs:
        # crear archivo con cabeceras vacías
        df = pd.DataFrame(columns=["name", "price", "renew_date"])
        df.to_csv(DATA_FILE, index=False)
        return

    rows = [s.to_serializable() for s in subs]
    df = pd.DataFrame(rows)
    df.to_csv(DATA_FILE, index=False)
