from .base import convert as base_convert

factor = {
    # SI
    "newton":          1.0,

    "kilonewton":      1e3,
    "meganewton":      1e6,
    "giganewton":      1e9,
    "teranewton":      1e12,
    "petanewton":      1e15,
    "exanewton":       1e18,

    "hectonewton":     1e2,
    "dekanewton":      1e1,
    "decinewton":      1e-1,
    "centinewton":     1e-2,
    "millinewton":     1e-3,

    "micronewton":     1e-6,
    "nanonewton":      1e-9,
    "piconewton":      1e-12,
    "femtonewton":     1e-15,
    "attonewton":      1e-18,

    # force from mass
    "gram_force":      0.00980665,
    "kilogram_force":  9.80665,
    "metric_ton_force": 9806.65,

    # imperial
    "pound_force":     4.4482216153,
    "ounce_force":     0.278013851,

    "kip_force":       4448.2216152548,

    "short_ton_force": 8896.443230521,
    "long_ton_force":  9964.0164181707,

    # scientific
    "dyne":            1e-5,
}

aliases = {
    # SI
    "n": "newton",

    "kn": "kilonewton",
    "mn": "meganewton",
    "gn": "giganewton",
    "tn": "teranewton",
    "pn": "petanewton",
    "en": "exanewton",

    "hn": "hectonewton",
    "dan": "dekanewton",

    "dn": "decinewton",
    "cn": "centinewton",
    "mn_small": "millinewton",

    "un": "micronewton",
    "μn": "micronewton",

    "nn": "nanonewton",
    "pn_small": "piconewton",
    "fn": "femtonewton",
    "an": "attonewton",

    # mass force
    "gf": "gram_force",
    "kgf": "kilogram_force",
    "tf": "metric_ton_force",

    # imperial
    "lbf": "pound_force",
    "ozf": "ounce_force",

    "kip": "kip_force",
    "kipf": "kip_force",

    # tons
    "stonf": "short_ton_force",
    "ltonf": "long_ton_force",

    # scientific
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