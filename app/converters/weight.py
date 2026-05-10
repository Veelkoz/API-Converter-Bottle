from app.converters.base import convert as base_convert

factor = {
    "kilogram":         1,
    "gram":             0.001,
    "milligram":        0.000001,
    "microgram":        1e-9,
    "nanogram":         1e-12,
    "metric_ton":       1000,
    "long_ton":         1016.04608,
    "short_ton":        907.18474,
    "pound":            0.45359237,
    "ounce":            0.028349523125,
    "carrat":           0.0002,
    "atomic_mass_unit": 1.66053906660e-27,
    "stone":         6.35029318,
    "grain":            6.479891E-5	
}

def convert(value, from_unit, to_unit, round_to=10):
    return base_convert(factor, value, from_unit, to_unit, round_to)
