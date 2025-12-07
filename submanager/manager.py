from __future__ import annotations

import os
from typing import List, Dict, Any

import pandas as pd

ARCHIVO = os.path.join("data", "subscriptions.csv")


class SubscriptionManager:
    """Clase para manejar suscripciones: agregar, eliminar, listar y calcular gasto mensual."""

    def __init__(self) -> None:
        """Inicializa el manager cargando las suscripciones desde disco."""
        self.suscripciones: List[Dict[str, Any]] = self.cargar_suscripciones()

    def cargar_suscripciones(self) -> List[Dict[str, Any]]:
        """Carga las suscripciones desde el archivo CSV.

        Si el archivo no existe, devuelve una lista vacía.

        Returns
        -------
        list[dict]
            Lista de suscripciones con claves: 'nombre', 'precio', 'fecha_renovacion'.
        """
        try:
            df = pd.read_csv(ARCHIVO)
            return df.to_dict(orient="records")
        except FileNotFoundError:
            return []

    def guardar_suscripciones(self) -> None:
        """Guarda las suscripciones actuales en el archivo CSV.

        Crea la carpeta `data/` si no existe.
        """
        df = pd.DataFrame(self.suscripciones)
        os.makedirs("data", exist_ok=True)
        df.to_csv(ARCHIVO, index=False)

    def agregar_suscripcion(self, nombre: str, precio: float, fecha_renovacion: str) -> None:
        """Agrega una nueva suscripción.

        Parameters
        ----------
        nombre : str
            Nombre de la suscripción (por ejemplo, 'Netflix').
        precio : float
            Precio mensual en números (no negativo).
        fecha_renovacion : str
            Fecha de renovación en formato YYYY-MM-DD.

        Notes
        -----
        No se realiza validación estricta sobre el formato de fecha aquí para mantener
        la simplicidad (principio "Simple es mejor que complejo"). Se asume entrada razonable.
        """
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.suscripciones.append(
            {"nombre": nombre, "precio": precio, "fecha_renovacion": fecha_renovacion}
        )
        self.guardar_suscripciones()

    def eliminar_suscripcion(self, nombre: str) -> None:
        """Elimina una suscripción por nombre.

        Parameters
        ----------
        nombre : str
            Nombre de la suscripción a eliminar.
        """
        self.suscripciones = [s for s in self.suscripciones if s["nombre"] != nombre]
        self.guardar_suscripciones()

    def listar_suscripciones(self) -> List[Dict[str, Any]]:
        """Devuelve la lista de suscripciones.

        Returns
        -------
        list[dict]
            Lista de diccionarios con las suscripciones actuales.
        """
        return self.suscripciones

    def gasto_mensual_total(self) -> float:
        """Calcula el gasto mensual total sumando el precio de cada suscripción.

        Returns
        -------
        float
            Suma de los precios mensuales.
        """
        return sum(s["precio"] for s in self.suscripciones)
