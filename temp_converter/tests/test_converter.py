import unittest
from temp_converter.converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    kelvin_to_celsius,
    fahrenheit_to_kelvin,
    kelvin_to_fahrenheit
)

class TestTemperatureConversions(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32)
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0)
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100)

    def test_celsius_to_kelvin(self):
        self.assertAlmostEqual(celsius_to_kelvin(0), 273.15)
        self.assertAlmostEqual(celsius_to_kelvin(100), 373.15)

    def test_kelvin_to_celsius(self):
        self.assertAlmostEqual(kelvin_to_celsius(273.15), 0)
        self.assertAlmostEqual(kelvin_to_celsius(373.15), 100)

    def test_fahrenheit_to_kelvin(self):
        self.assertAlmostEqual(fahrenheit_to_kelvin(32), 273.15)
        self.assertAlmostEqual(fahrenheit_to_kelvin(212), 373.15)

    def test_kelvin_to_fahrenheit(self):
        self.assertAlmostEqual(kelvin_to_fahrenheit(273.15), 32)
        self.assertAlmostEqual(kelvin_to_fahrenheit(373.15), 212)

if __name__ == "__main__":
    unittest.main()
