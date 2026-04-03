from analizador_poblacion import AnalizadorPoblacion
import os

if __name__ == "__main__":
    ruta_csv = 'test_data.csv'

    # Asegurarse de que el archivo test_data.csv exista. Si no, se puede usar el original o crear uno.
    if not os.path.exists(ruta_csv):
        print(f"El archivo {ruta_csv} no se encontró. Usando el archivo por defecto 'test_data.csv'.")
        # Aquí podrías poner lógica para crear un archivo de prueba si no existe, o usar otro por defecto.
        # Para este ejemplo, asumiremos que 'test_data.csv' ya fue creado o existe.
        # Si el usuario quiere usar el original, podría cambiar ruta_csv a 'data.csv' o similar.

    try:
        analizador = AnalizadorPoblacion(ruta_csv)

        poblacion_total = analizador.calcular_poblacion_total()
        departamento_mas_poblado, poblacion_dpto = analizador.obtener_departamento_mas_poblado()

        print(f"Población total: {poblacion_total}")
        print(f"Departamento más poblado: {departamento_mas_poblado} ({poblacion_dpto})")

    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Error al procesar los datos: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")