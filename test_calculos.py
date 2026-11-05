
import unittest

from calculos import (
    calcular_area,
    calcular_preco,
    aplicar_desconto,
    aplicar_valor_minimo
)


class TestCalculadora(unittest.TestCase):

    def test_area(self):
        resultado = calcular_area(263, 23)
        self.assertAlmostEqual(resultado, 0.6049)

    def test_preco(self):
        resultado = calcular_preco(0.6049, 56, 3)
        self.assertAlmostEqual(resultado, 101.6232)

    def test_desconto_abaixo_200(self):
        self.assertEqual(aplicar_desconto(150), 150)

    def test_desconto_igual_200(self):
        self.assertEqual(aplicar_desconto(200), 200)

    def test_desconto_acima_200(self):
        self.assertEqual(aplicar_desconto(250), 237.50)

    def test_valor_minimo_abaixo(self):
        self.assertEqual(aplicar_valor_minimo(5), 30)

    def test_valor_minimo_igual(self):
        self.assertEqual(aplicar_valor_minimo(30), 30)

    def test_valor_minimo_acima(self):
        self.assertEqual(aplicar_valor_minimo(75), 75)

    def test_fluxo_completo(self):
        area = calcular_area(100, 100)
        subtotal = calcular_preco(area, 100, 3)
        desconto = aplicar_desconto(subtotal)
        total = aplicar_valor_minimo(desconto)

        self.assertAlmostEqual(total, 285)


if __name__ == "__main__":
    unittest.main()
