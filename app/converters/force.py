from .base import convert as base_convert

factor = {
    "newton":          1.0,
    "kilonewton":      1e3,
    "meganewton":      1e6,
    "millinewton":     1e-3,
    "micronewton":     1e-6,
    "nanonewton":      1e-9,
    "gram_force":      0.00980665,
    "kilogram_force":  9.80665,
    "metric_ton_force": 9806.65,
    "pound_force":     4.4482216153,
    "ounce_force":     0.278013851,
    "kip_force":       4448.2216152548,
    "dyne":            1e-5,
}

aliases = {
    "n": "newton",
    "kn": "kilonewton",
    "mn": "meganewton",
    "un": "micronewton",
    "μn": "micronewton",
    "nn": "nanonewton",
    "gf": "gram_force",
    "kgf": "kilogram_force",
    "tf": "metric_ton_force",
    "lbf": "pound_force",
    "ozf": "ounce_force",
    "kip": "kip_force",
    "kipf": "kip_force",
    "dyn": "dyne",
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