"""
models.py — Clase Subscription como dataclass.
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Subscription:
    """
    Representa una suscripción.
    Attributes:
        name: nombre del servicio.
        price: precio mensual (float).
        renew_date: datetime de la próxima renovación (o fecha de cobro).
    """
    name: str
    price: float
    renew_date: datetime

    def to_serializable(self) -> dict:
        """Convierte a dict serializable (para CSV/JSON)."""
        return {
            "name": self.name,
            "price": float(self.price),
            "renew_date": self.renew_date.strftime("%Y-%m-%d"),
        }

    @classmethod
    def from_dict(cls, d: dict) -> "Subscription":
        """Crea Subscription a partir de un diccionario (lee renew_date en formato YYYY-MM-DD)."""
        rd = d.get("renew_date")
        if isinstance(rd, str):
            rd_dt = datetime.strptime(rd, "%Y-%m-%d")
        else:
            rd_dt = rd  # si ya es datetime
        return cls(
            name=d.get("name", ""),
            price=float(d.get("price", 0.0)),
            renew_date=rd_dt,
        )
