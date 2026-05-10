from .base import convert as base_convert

factor = {
    "pascal":          1.0,
    "kilopascal":      1e3,
    "megapascal":      1e6,
    "gigapascal":      1e9,

    "bar":             1e5,
    "millibar":        100.0,
    "hectopascal":     100.0,

    "atmosphere":      101325.0,
    "torr":            133.3223684211,

    "psi":             6894.7572931783,
    "ksi":             6894757.2931783,

    "newton_per_square_meter": 1.0,

    "millimeter_mercury": 133.322,
    "inch_mercury":       3386.389,

    "millimeter_water": 9.80638,
    "inch_water":      249.082,
}
aliases = {
    "pa": "pascal",
    "kpa": "kilopascal",
    "mpa": "megapascal",
    "gpa": "gigapascal",

    "bar": "bar",
    "mbar": "millibar",
    "hpa": "hectopascal",

    "atm": "atmosphere",
    "torr": "torr",

    "psi": "psi",
    "ksi": "ksi",

    "n/m2": "newton_per_square_meter",

    "mmhg": "millimeter_mercury",
    "inhg": "inch_mercury",

    "mmh2o": "millimeter_water",
    "inh2o": "inch_water",
}

def convert(value, from_unit, to_unit, round_to=10):
    return base_convert(
        factor,
        aliases,
        value,
        from_unit,
        to_unit,
        round_to
    )