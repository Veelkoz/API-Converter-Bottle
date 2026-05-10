from app.converters.base import convert as base_convert

factor = {
    "second":       1,
    "millisecond":  0.001,
    "microsecond":  0.000001,
    "nanosecond":   1.E-9,
    "picosecond":   1.E-12,
    "minute":       60,
    "hour":         3600,
    "day":          86400,
    "week":         604800,
    "month":        2629800,        #average month 30.4375 days
    "year":         31557600        #average year 365.25 days
}

def convert(value, from_unit, to_unit, round_to=10):
    return base_convert(factor, value, from_unit, to_unit, round_to)
