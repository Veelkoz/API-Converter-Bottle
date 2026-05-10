from converters.base import convert as base_convert

factor = {
}

def convert(value, from_unit, to_unit, round_to=10):
    return base_convert(factor, value, from_unit, to_unit, round_to)
