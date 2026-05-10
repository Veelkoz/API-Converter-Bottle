
units = {
    "kelvin":     {"to": lambda x: x,              "from": lambda x: x},
    "celsius":    {"to": lambda x: x + 273.15,     "from": lambda x: x - 273.15},
    "fahrenheit": {"to": lambda x: (x + 459.67) * 5/9, "from": lambda x: x * 9/5 - 459.67},
}

aliases = {
    "k":    "kelvin",
    "c":    "celsius",
    "f":    "fahrenheit",
    "°c":   "celsius",
    "°f":   "fahrenheit",
    "°k":   "kelvin",
}

def convert(value, from_unit, to_unit, round_to=10):

    from_unit = aliases.get(from_unit.lower(), from_unit.lower())
    to_unit = aliases.get(to_unit.lower(), to_unit.lower())

    if from_unit not in units:
        raise ValueError(f"unknown from_unit: {from_unit}")
    if to_unit not in units:
        raise ValueError(f"unknown to_unit: {to_unit}")
    if round_to < 0:
        raise ValueError("round_to can't be smaller than 0")
    if round_to > 25:
        raise ValueError("round_to exceeds 25")

    in_kelvin = units[from_unit]["to"](value)
    result = units[to_unit]["from"](in_kelvin)
    return round(result, round_to)