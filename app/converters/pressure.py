from .base import convert as base_convert

factor = {
    # SI
    "pascal":          1.0,
    "kilopascal":      1e3,
    "megapascal":      1e6,
    "gigapascal":      1e9,

    # common metric
    "bar":             1e5,
    "millibar":        100.0,
    "hectopascal":     100.0,

    # atmospheric
    "atmosphere":      101325.0,
    "torr":            133.3223684211,

    # imperial
    "psi":             6894.7572931783,
    "ksi":             6894757.2931783,

    # scientific
    "newton_per_square_meter": 1.0,

    # liquids / weather
    "millimeter_mercury": 133.322,
    "inch_mercury":       3386.389,

    # water pressure
    "millimeter_water": 9.80638,
    "inch_water":      249.082,
}

def convert(value, from_unit, to_unit, round_to=10):
    return base_convert(factor, value, from_unit, to_unit, round_to)
