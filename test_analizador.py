import unittest
import pandas as pd

from analizador_poblacion import AnalizadorPoblacion


class TestAnalizadorPoblacion(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        datos = pd.DataFrame({
            "Departamento": ["A", "A", "B", "B"],
            "Poblacion": ["1.000", "2.000", "3.000", None],
        })
        datos.to_csv("test_data.csv", index=False)

        vacio = pd.DataFrame(columns=["Departamento", "Poblacion"])
        vacio.to_csv("test_empty.csv", index=False)

    def test_carga_y_limpieza(self):
        analizador = AnalizadorPoblacion("test_data.csv")

        self.assertEqual(len(analizador.dataframe), 3)
        self.assertTrue(
            pd.api.types.is_integer_dtype(
                analizador.dataframe["Poblacion"]
            )
        )

    def test_calculo_poblacion_total(self):
        analizador = AnalizadorPoblacion("test_data.csv")

        total = analizador.calcular_poblacion_total()
        self.assertEqual(total, 6000)

    def test_archivo_vacio(self):
        analizador = AnalizadorPoblacion("test_empty.csv")

        total = analizador.calcular_poblacion_total()
        self.assertEqual(total, 0)


if __name__ == "__main__":
    unittest.main()