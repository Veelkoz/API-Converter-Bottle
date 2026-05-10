from .base import convert as base_convert

factor = {
    "cubic_meter":              1,
    "cubic_kilometer":          1000000000,
    "cubic_centimeter":         0.000001,
    "cubic_millimeter":         1.E-9,
    "liter":                    0.001,
    "milliliter":               0.000001,
    "gallon_us":                0.00378541,
    "quart_us":                 0.0009463525,
    "pint_us":                  0.0004731763,
    "cup_us":                   0.0002365881,
    "fluid_ounce_us":           0.0000295735,
    "table_spoon_us":           0.0000147868,
    "tea_spoon_us":             0.0000049289,
    "gallon_imperial":          0.00454609,
    "quart_imperial":           0.0011365225,
    "pint_imperial":            0.0005682613,
    "fluid_ounce_imperial":     0.0000284131,
    "table_spoon_imperial":     0.0000177582,
    "tea_spoon_imperial":       0.0000059194,
    "cubic_mile":               4168180000,
    "cubic_yard":               0.764554858,
    "cubic_foot":               0.0283168466,
    "cubic_inch":               0.0000163871
}

aliases = {
    "m3": "cubic_meter",
    "km3": "cubic_kilometer",
    "cm3": "cubic_centimeter",
    "mm3": "cubic_millimeter",
    "l": "liter",
    "ml": "milliliter",
    "gal": "gallon_us",
    "qt": "quart_us",
    "pt": "pint_us",
    "cup": "cup_us",
    "floz": "fluid_ounce_us",
    "tbsp": "table_spoon_us",
    "tsp": "tea_spoon_us",
    "igal": "gallon_imperial",
    "iqt": "quart_imperial",
    "ipt": "pint_imperial",
    "ifloz": "fluid_ounce_imperial",
    "mi3": "cubic_mile",
    "yd3": "cubic_yard",
    "ft3": "cubic_foot",
    "in3": "cubic_inch",
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