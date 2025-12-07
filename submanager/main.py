from __future__ import annotations

from .manager import SubscriptionManager
from rich.console import Console

console = Console()
manager = SubscriptionManager()


def mostrar_menu() -> str:
    """Muestra el menú principal y devuelve la opción elegida.

    Returns
    -------
    str
        Opción ingresada por el usuario.
    """
    console.print("\n[bold cyan]SUBMANAGER — Administrador de Suscripciones[/bold cyan]")
    console.print("1) Listar suscripciones")
    console.print("2) Agregar suscripción")
    console.print("3) Eliminar suscripción")
    console.print("4) Mostrar gasto mensual total")
    console.print("5) Salir")
    opcion = console.input("Elija opción: ")
    return opcion


def main() -> None:
    """Función principal que controla el flujo del programa."""
    while True:
        opcion = mostrar_menu()
        if opcion == "1":
            suscripciones = manager.listar_suscripciones()
            if not suscripciones:
                console.print("No hay suscripciones registradas.")
            else:
                for s in suscripciones:
                    console.print(
                        f"[green]{s['nombre']}[/green] - ${s['precio']} - Renovación: {s['fecha_renovacion']}"
                    )
        elif opcion == "2":
            try:
                nombre = console.input("Nombre de la suscripción: ").strip()
                precio = float(console.input("Precio: "))
                fecha = console.input("Fecha de renovación (YYYY-MM-DD): ").strip()
            except ValueError:
                console.print("[red]Precio inválido. Intente nuevamente.[/red]")
                continue

            manager.agregar_suscripcion(nombre, precio, fecha)
            console.print("Suscripción agregada correctamente.")
        elif opcion == "3":
            nombre = console.input("Nombre de la suscripción a eliminar: ").strip()
            manager.eliminar_suscripcion(nombre)
            console.print("Suscripción eliminada si existía.")
        elif opcion == "4":
            total = manager.gasto_mensual_total()
            console.print(f"Gasto mensual total: ${total}")
        elif opcion == "5":
            console.print("¡Hasta luego!")
            break
        else:
            console.print("Opción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()
