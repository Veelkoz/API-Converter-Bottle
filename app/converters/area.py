from app.converters.base import convert as base_convert

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

def convert(value, from_unit, to_unit, round_to=10):
    return base_convert(factor, value, from_unit, to_unit, round_to)
