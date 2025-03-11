import unittest
from conversions import convertCelsiusToKelvin, convertCelsiusToFahrenheit

class TestTemperatureConversions(unittest.TestCase):
    def test_convertCelsiusToKelvin(self):
        self.assertAlmostEqual(convertCelsiusToKelvin(0), 273.15)
        self.assertAlmostEqual(convertCelsiusToKelvin(100), 373.15)
        self.assertAlmostEqual(convertCelsiusToKelvin(-273.15), 0.0)
        self.assertAlmostEqual(convertCelsiusToKelvin(300), 573.15)
        self.assertAlmostEqual(convertCelsiusToKelvin(25), 298.15)

    def test_convertCelsiusToFahrenheit(self):
        self.assertAlmostEqual(convertCelsiusToFahrenheit(0), 32.0)
        self.assertAlmostEqual(convertCelsiusToFahrenheit(100), 212.0)
        self.assertAlmostEqual(convertCelsiusToFahrenheit(-40), -40.0)
        self.assertAlmostEqual(convertCelsiusToFahrenheit(300), 572.0)
        self.assertAlmostEqual(convertCelsiusToFahrenheit(25), 77.0)

if __name__ == '__main__':
    unittest.main()
from conversions import convertFahrenheitToCelsius, convertFahrenheitToKelvin, convertKelvinToFahrenheit, convertKelvinToCelsius

class TestTemperatureConversions(unittest.TestCase):
    # (Previous test functions here...)

    def test_convertFahrenheitToCelsius(self):
        self.assertAlmostEqual(convertFahrenheitToCelsius(32), 0.0)
        self.assertAlmostEqual(convertFahrenheitToCelsius(212), 100.0)
        self.assertAlmostEqual(convertFahrenheitToCelsius(-40), -40.0)
        self.assertAlmostEqual(convertFahrenheitToCelsius(572), 300.0)
        self.assertAlmostEqual(convertFahrenheitToCelsius(77), 25.0)

    def test_convertFahrenheitToKelvin(self):
        self.assertAlmostEqual(convertFahrenheitToKelvin(32), 273.15)
        self.assertAlmostEqual(convertFahrenheitToKelvin(212), 373.15)
        self.assertAlmostEqual(convertFahrenheitToKelvin(-40), 233.15)
        self.assertAlmostEqual(convertFahrenheitToKelvin(572), 573.15)
        self.assertAlmostEqual(convertFahrenheitToKelvin(77), 298.15)

    def test_convertKelvinToFahrenheit(self):
        self.assertAlmostEqual(convertKelvinToFahrenheit(273.15), 32.0)
        self.assertAlmostEqual(convertKelvinToFahrenheit(373.15), 212.0)
        self.assertAlmostEqual(convertKelvinToFahrenheit(233.15), -40.0)
        self.assertAlmostEqual(convertKelvinToFahrenheit(573.15), 572.0)
        self.assertAlmostEqual(convertKelvinToFahrenheit(298.15), 77.0)

    def test_convertKelvinToCelsius(self):
        self.assertAlmostEqual(convertKelvinToCelsius(273.15), 0.0)
        self.assertAlmostEqual(convertKelvinToCelsius(373.15), 100.0)
        self.assertAlmostEqual(convertKelvinToCelsius(233.15), -40.0)
        self.assertAlmostEqual(convertKelvinToCelsius(573.15), 300.0)
        self.assertAlmostEqual(convertKelvinToCelsius(298.15), 25.0)