"""
Módulo para el análisis de datos de población municipal de Colombia.
"""

from __future__ import annotations

import pandas as pd


class AnalizadorPoblacion:
    """
    Encapsula la carga, limpieza y análisis de datos de población.

    Args:
        ruta_csv (str): Ruta del archivo CSV con los datos de población.

    Attributes:
        dataframe (pd.DataFrame): DataFrame con los datos limpios.
    """

    def __init__(self, ruta_csv: str) -> None:
        self.dataframe = self._cargar_datos(ruta_csv)
        self._limpiar_datos()

    def _cargar_datos(self, ruta_csv: str) -> pd.DataFrame:
        """Carga el archivo CSV y devuelve un DataFrame."""
        try:
            return pd.read_csv(ruta_csv)
        except FileNotFoundError:
            return pd.DataFrame()

    def _limpiar_datos(self) -> None:
        """
        Limpia la columna de población:
        - Elimina separadores de miles.
        - Convierte a tipo entero.
        - Elimina filas con valores nulos.
        """
        if "Poblacion" not in self.dataframe.columns:
            return

        poblacion_limpia = pd.to_numeric(
            self.dataframe["Poblacion"]
            .astype(str)
            .str.replace(".", "", regex=False),
            errors="coerce",
        )

        self.dataframe["Poblacion"] = poblacion_limpia
        self.dataframe.dropna(subset=["Poblacion"], inplace=True)
        self.dataframe["Poblacion"] = \
            self.dataframe["Poblacion"].astype(int)

    def calcular_poblacion_total(self) -> int:
        """
        Calcula la suma total de la población.

        Returns:
            int: Población total.
        """
        if "Poblacion" not in self.dataframe.columns:
            return 0
        return int(self.dataframe["Poblacion"].sum())

    def obtener_dpto_mas_poblado(self) -> tuple[str | None, int]:
        """
        Obtiene el departamento con mayor población acumulada.

        Returns:
            tuple: (nombre_departamento, poblacion_total).
        """
        columnas_necesarias = {"Departamento", "Poblacion"}

        if not columnas_necesarias.issubset(self.dataframe.columns):
            return None, 0

        agrupado = (
            self.dataframe
            .groupby("Departamento")["Poblacion"]
            .sum()
        )

        if agrupado.empty:
            return None, 0

        departamento = agrupado.idxmax()
        poblacion = int(agrupado.max())
        return departamento, poblacion
