from .base import convert as base_convert

factor = {
    "joule":           1.0,
    "kilojoule":       1e3,
    "megajoule":       1e6,
    "gigajoule":       1e9,

    "watt_hour":       3600.0,
    "kilowatt_hour":   3.6e6,
    "megawatt_hour":   3.6e9,
    "gigawatt_hour":   3.6e12,

    "calorie":         4.184,
    "kilocalorie":     4184.0,

    "btu":             1055.05585262,
    "therm":           105505600.0,

    "electronvolt":    1.602176634e-19,
    "kiloelectronvolt": 1.602176634e-16,
    "megaelectronvolt": 1.602176634e-13,

    "foot_pound":      1.3558179483,

    "ton_tnt":         4.184e9,
    "kiloton_tnt":     4.184e12,
    "megaton_tnt":     4.184e15,
}

aliases = {
    "j": "joule",
    "kj": "kilojoule",
    "mj": "megajoule",
    "gj": "gigajoule",

    "wh": "watt_hour",
    "kwh": "kilowatt_hour",
    "mwh": "megawatt_hour",

    "cal": "calorie",
    "kcal": "kilocalorie",

    "ev": "electronvolt",
    "kev": "kiloelectronvolt",
    "mev": "megaelectronvolt",

    "btu": "btu",
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
