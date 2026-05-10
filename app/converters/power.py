from .base import convert as base_convert

factor = {
    # SI
    "watt":        1.0,

    "kilowatt":    1e3,
    "megawatt":    1e6,
    "gigawatt":    1e9,
    "terawatt":    1e12,
    "petawatt":    1e15,
    "exawatt":     1e18,

    "milliwatt":   1e-3,
    "microwatt":   1e-6,
    "nanowatt":    1e-9,

    # horsepower
    "horsepower":          745.6998715823,
    "metric_horsepower":   735.49875,
    "electric_horsepower": 746.0,
    "boiler_horsepower":   9809.5,

    # thermal / HVAC
    "btu_per_hour":        0.2930710702,
    "ton_refrigeration":   3516.8528420667,

    # calories
    "kilocalorie_per_hour":   1.163,
    "kilocalorie_per_second": 4186.8,

    # mechanics
    "foot_pound_per_second": 1.3558179483,

    # electrical
    "volt_ampere":        1.0,
    "kilovolt_ampere":    1000.0,

    # energy over time
    "joule_per_second":   1.0,
    "kilojoule_per_second": 1000.0,
    "megajoule_per_second": 1e6,

    "joule_per_minute":   1.0 / 60.0,
    "joule_per_hour":     1.0 / 3600.0,

    "kilojoule_per_minute": 1000.0 / 60.0,
    "kilojoule_per_hour":   1000.0 / 3600.0,
}

aliases = {
    # SI
    "w": "watt",

    "kw": "kilowatt",
    "mw": "megawatt",
    "gw": "gigawatt",
    "tw": "terawatt",
    "pw": "petawatt",
    "ew": "exawatt",

    "mw_small": "milliwatt",

    "uw": "microwatt",
    "μw": "microwatt",

    "nw": "nanowatt",

    # horsepower
    "hp": "horsepower",
    "ps": "metric_horsepower",

    # HVAC
    "btu/h": "btu_per_hour",
    "tr": "ton_refrigeration",

    # calories
    "kcal/h": "kilocalorie_per_hour",
    "kcal/s": "kilocalorie_per_second",

    # mechanics
    "ftlb/s": "foot_pound_per_second",

    # electrical
    "va": "volt_ampere",
    "kva": "kilovolt_ampere",

    # energy/time
    "j/s": "joule_per_second",
    "kj/s": "kilojoule_per_second",
    "mj/s": "megajoule_per_second",

    "j/min": "joule_per_minute",
    "j/h": "joule_per_hour",

    "kj/min": "kilojoule_per_minute",
    "kj/h": "kilojoule_per_hour",
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