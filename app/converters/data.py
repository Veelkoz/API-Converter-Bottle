from .base import convert as base_convert

factor = {
    # basic
    "bit":             1.0,
    "nibble":          4.0,
    "byte":            8.0,
    "character":       8.0,
    "word":            16.0,
    "mapm_word":       32.0,
    "quadruple_word":  64.0,
    "block":           4096.0,

    # binary units
    "kilobit":         1024.0,
    "kilobyte":        8192.0,

    "megabit":         1048576.0,
    "megabyte":        8388608.0,

    "gigabit":         1073741824.0,
    "gigabyte":        8589934592.0,

    "terabit":         1099511627776.0,
    "terabyte":        8796093022208.0,

    "petabit":         1125899906842624.0,
    "petabyte":        9007199254740992.0,

    "exabit":          1152921504606846976.0,
    "exabyte":         9223372036854775808.0,

    # decimal SI units
    "kilobyte_decimal": 8000.0,
    "megabyte_decimal": 8000000.0,
    "gigabyte_decimal": 8000000000.0,
    "terabyte_decimal": 8000000000000.0,
    "petabyte_decimal": 8000000000000000.0,
    "exabyte_decimal": 8000000000000000000.0,
}

aliases = {
    # basic
    "b": "bit",
    "B": "byte",

    # binary
    "kb": "kilobit",
    "kib": "kilobit",

    "kB": "kilobyte",

    "mb": "megabit",
    "mib": "megabit",

    "MB": "megabyte",

    "gb": "gigabit",
    "gib": "gigabit",

    "GB": "gigabyte",

    "tb": "terabit",
    "tib": "terabit",

    "TB": "terabyte",

    "pb": "petabit",
    "pib": "petabit",

    "PB": "petabyte",

    "eb": "exabit",
    "eib": "exabit",

    "EB": "exabyte",

    # decimal byte units
    "kb_decimal": "kilobyte_decimal",
    "mb_decimal": "megabyte_decimal",
    "gb_decimal": "gigabyte_decimal",
    "tb_decimal": "terabyte_decimal",
    "pb_decimal": "petabyte_decimal",
    "eb_decimal": "exabyte_decimal",
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