import unittest
from src.Pricing import Pricing

class TestPricing(unittest.TestCase):
    def test_calculate_datosDefinirPrecio_RetornaPrecio(self):
        # Arrange
        pricing = Pricing()
        price = 100
        tax = 0.1
        discount = 10
        precioEsperado = 99.0

        # Do
        precioactual = pricing.calculate(price, tax, discount)

        # Assert
        self.assertEqual(precioEsperado,precioactual)

    def test_calculate_datosDefinirPrecio_RetornaPrecio_subtest(self):
        items = (
            {'case': 'No tax, no discount', 'price': 10, 'tax': 0, 'discount': 0, 'net_price': 10},
            {'case': 'Has tax, no discount', 'price': 10, 'tax': 0.1, 'discount': 0, 'net_price': 11},
            {'case': 'No tax, has discount', 'price': 10, 'tax': 0, 'discount': 1, 'net_price': 9},
            {'case': 'Has tax, has discount', 'price': 10, 'tax': 0.1, 'discount': 1, 'net_price': 9.9},
        )

        pricing=Pricing()

        for item in items:
            with self.subTest(item['case']):
                net_price = pricing.calculate(
                    item['price'],
                    item['tax'],
                    item['discount']
                )

            self.assertEqual(
                net_price,
                item['net_price']
            )





