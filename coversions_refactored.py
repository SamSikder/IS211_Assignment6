class ConversionNotPossible(Exception):
    pass

conversion_factors = {
    ("Celsius", "Kelvin"): lambda c: c + 273.15,
    ("Celsius", "Fahrenheit"): lambda c: (c * 9/5) + 32,
    ("Kelvin", "Celsius"): lambda k: k - 273.15,
    ("Kelvin", "Fahrenheit"): lambda k: (k - 273.15) * 9/5 + 32,
    ("Fahrenheit", "Celsius"): lambda f: (f - 32) * 5/9,
    ("Fahrenheit", "Kelvin"): lambda f: (f - 32) * 5/9 + 273.15,
    ("Miles", "Yards"): lambda m: m * 1760,
    ("Miles", "Meters"): lambda m: m * 1609.34,
    ("Yards", "Miles"): lambda y: y / 1760,
    ("Yards", "Meters"): lambda y: y * 0.9144,
    ("Meters", "Miles"): lambda m: m / 1609.34,
    ("Meters", "Yards"): lambda m: m / 0.9144,
}

def convert(fromUnit, toUnit, value):
    if fromUnit == toUnit:
        return value
    try:
        return conversion_factors[(fromUnit, toUnit)](value)
    except KeyError:
        raise ConversionNotPossible(f"Cannot convert {fromUnit} to {toUnit}")