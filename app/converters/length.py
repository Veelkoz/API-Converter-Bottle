from .base import convert as base_convert

factor = {
    "meter":        1,
    "kilometer":    1000,
    "decimeter":    0.1,
    "centimeter":   0.01,
    "millimeter":   0.001,
    "micrometer":   1e-6,
    "nanometer":    1e-9,
    "picometer":    1e-12,

    "mile":         1609.344,
    "yard":         0.9144,
    "foot":         0.3048,
    "inch":         0.0254,
    "thou":         0.0000254,

    "nautical_mile": 1852,

    "au":           149597870700,
    "light_second": 299792458,
    "light_minute": 17987547480,
    "light_hour":   1079252848800,
    "light_year":   9460730472580800,
}
aliases = {
    "m": "meter",
    "km": "kilometer",
    "dm": "decimeter",
    "cm": "centimeter",
    "mm": "millimeter",

    "um": "micrometer",
    "μm": "micrometer",

    "nm": "nanometer",
    "pm": "picometer",

    "mi": "mile",
    "yd": "yard",
    "ft": "foot",
    "in": "inch",

    "mil": "thou",

    "nmi": "nautical_mile",

    "ls": "light_second",
    "lm": "light_minute",
    "lh": "light_hour",
    "ly": "light_year",
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