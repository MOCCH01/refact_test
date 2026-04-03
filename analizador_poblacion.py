"""
Módulo para el análisis de datos de población municipal de Colombia.
"""
import pandas as pd
import os

# Contenido correcto para 'analizador_poblacion.py'
analizador_poblacion_content = """import pandas as pd
import os


class AnalizadorPoblacion:
    \"\"\"
    Clase para analizar datos de población desde un archivo CSV.

    Esta clase carga datos de población desde un archivo CSV, los limpia
    y permite realizar cálculos como la población total y encontrar
    el departamento más poblado.
    \"\"\"

    def __init__(self, ruta_archivo_csv: str):
        \"\"\"
        Inicializa la clase AnalizadorPoblacion.

        Args:
            ruta_archivo_csv (str): La ruta al archivo CSV que contiene
                                     los datos de población.
        \"\"\"
        if not os.path.exists(ruta_archivo_csv):
            raise FileNotFoundError(f"El archivo no se encontró en: {ruta_archivo_csv}")

        try:
            self.dataframe = pd.read_csv(ruta_archivo_csv)
            self._limpiar_datos()
        except Exception as e:
            raise ValueError(f"Error al cargar o limpiar los datos: {e}")

    def _limpiar_datos(self):
        \"\"\"
        Método privado para limpiar y preprocesar los datos del DataFrame.

        Este método renombra columnas, convierte la columna 'Poblacion'
        a tipo numérico manejando separadores de miles y valores nulos.
        \"\"\"
        # Renombrar columnas para mayor claridad y consistencia
        self.dataframe.columns = [
            col.strip().replace(' ', '_') for col in self.dataframe.columns
        ]
        self.dataframe.rename(columns={'Departamento': 'departamento', 'Poblacion': 'poblacion'},
                               inplace=True)

        # Convertir la columna 'poblacion' a numérico, manejando errores
        if 'poblacion' in self.dataframe.columns:
            # Eliminar puntos (separadores de miles) y convertir a numérico
            self.dataframe['poblacion'] = (
                self.dataframe['poblacion']
                .astype(str)
                .str.replace('.', '', regex=False)
                .str.replace(',', '', regex=False) # En caso de coma como separador de miles
                .replace('', '0') # Reemplazar cadenas vacías con '0' antes de convertir
                .astype(float)
                .fillna(0) # Rellenar NaN después de la conversión a float
                .astype(int)
            )
        else:
            self.dataframe['poblacion'] = 0

    def calcular_poblacion_total(self) -> int:
        \"\"\"
        Calcula la población total de todos los departamentos.

        Returns:
            int: La suma total de la población.
        \"\"\"
        if self.dataframe.empty or 'poblacion' not in self.dataframe.columns:
            return 0
        return self.dataframe['poblacion'].sum()

    def obtener_departamento_mas_poblado(self) -> tuple[str, int]:
        \"\"\"
        Identifica el departamento con la mayor población.

        Returns:
            tuple[str, int]: Una tupla que contiene el nombre del departamento
                             y su población. Si el DataFrame está vacío o
                             no tiene datos de población, retorna ('None', 0).
        \"\"\"
        if self.dataframe.empty or 'poblacion' not in self.dataframe.columns or self.dataframe['poblacion'].sum() == 0:
            return 'None', 0

        departamento_mas_poblado_fila = self.dataframe.loc[self.dataframe['poblacion'].idxmax()]
        return (
            departamento_mas_poblado_fila['departamento'],
            departamento_mas_poblado_fila['poblacion']
        )
"""

with open('analizador_poblacion.py', 'w') as f:
    f.write(analizador_poblacion_content)
