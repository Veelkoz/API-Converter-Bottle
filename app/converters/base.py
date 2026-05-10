
def convert(factor, aliases, value, from_unit, to_unit, round_to=10):

    from_unit = aliases.get(from_unit.lower(), from_unit.lower())
    to_unit = aliases.get(to_unit.lower(), to_unit.lower())

    if from_unit not in factor:
        raise ValueError(f"unknown from_unit: {from_unit}")
    if to_unit not in factor:
        raise ValueError(f"unknown to_unit: {to_unit}")
    if round_to < 0:
        raise ValueError("round_to can't be smaller than 0")
    if round_to > 25:
        raise ValueError("round_to exceeds 25")
    
    value = float(value)
    result = value * factor[from_unit] / factor[to_unit]
    
    return round(result, round_to)