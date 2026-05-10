from decimal import Decimal, getcontext

getcontext().prec = 100

factor = {
    # SI
    "meter":        Decimal("1"),
    "kilometer":    Decimal("1000"),
    "decimeter":    Decimal("0.1"),
    "centimeter":   Decimal("0.01"),
    "millimeter":   Decimal("0.001"),
    "micrometer":   Decimal("1e-6"),
    "nanometer":    Decimal("1e-9"),
    "picometer":    Decimal("1e-12"),

    # Imperial
    "mile":         Decimal("1609.344"),
    "yard":         Decimal("0.9144"),
    "foot":         Decimal("0.3048"),
    "inch":         Decimal("0.0254"),
    "thou":         Decimal("0.0000254"),

    # Nautical
    "nautical_mile": Decimal("1852"),

    # Astronomy
    "au":           Decimal("149597870700"),
    "light_second": Decimal("299792458"),
    "light_minute": Decimal("17987547480"),
    "light_hour":   Decimal("1079252848800"),
    "light_year":   Decimal("9460730472580800"),

    # Scientific
    "angstrom":     Decimal("1e-10"),

    # Typography
    "point":        Decimal("0.0003527777777777777777777778"),
    "pica":         Decimal("0.004233333333333333333333333"),
}

def convert(value, from_unit, to_unit, round_to=10):

    if from_unit not in factor:
        raise ValueError(f"unknown from_unit: {from_unit}")

    if to_unit not in factor:
        raise ValueError(f"unknown to_unit: {to_unit}")

    if round_to < 0:
        raise ValueError("round_to can't be smaller than 0")

    if round_to > 40:
        raise ValueError("round_to exceeds 40")

    value = Decimal(str(value))

    result = value * factor[from_unit] / factor[to_unit]
    return round(float(result), round_to)