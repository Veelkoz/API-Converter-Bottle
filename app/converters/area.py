from .base import convert as base_convert

factor = {
    "square_meter":         1,
    "square_kilometer":     1000000,
    "square_centimeter":    0.0001,
    "square_millimeter":    0.000001,
    "square_micrometer":    1.E-12,
    "hectare":              10000,
    "square_mile":          2589990,
    "square_yard":          0.83612736,
    "square_foot":          0.09290304,
    "square_inch":          0.00064516,
    "acre":                 4046.8564224,
    "square_nautical_mile": 3429904

}

aliases = {
    "m2": "square_meter",
    "sqm": "square_meter",

    "km2": "square_kilometer",

    "cm2": "square_centimeter",

    "mm2": "square_millimeter",

    "um2": "square_micrometer",
    "μm2": "square_micrometer",

    "ha": "hectare",

    "mi2": "square_mile",

    "yd2": "square_yard",

    "ft2": "square_foot",
    "sqft": "square_foot",

    "in2": "square_inch",

    "ac": "acre",

    "nmi2": "square_nautical_mile",
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