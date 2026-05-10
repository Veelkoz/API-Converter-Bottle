from .base import convert as base_convert

factor = {
    "meter_per_second":             1.0,
    "meter_per_minute":             1.0 / 60.0,
    "meter_per_hour":               1.0 / 3600.0,

    "kilometer_per_second":         1000.0,
    "kilometer_per_minute":         1000.0 / 60.0,
    "kilometer_per_hour":           1000.0 / 3600.0,

    "mile_per_second":              1609.344,
    "mile_per_minute":              1609.344 / 60.0,
    "mile_per_hour":                1609.344 / 3600.0,

    "foot_per_second":              0.3048,
    "foot_per_minute":              0.3048 / 60.0,
    "foot_per_hour":                0.3048 / 3600.0,

    "yard_per_second":              0.9144,
    "yard_per_minute":              0.9144 / 60.0,
    "yard_per_hour":                0.9144 / 3600.0,

    "knot":                         0.5144444444444445,

    "speed_of_light":               299792458.0,
    "earth_orbital_velocity":       29780,
    "mach_air_20c":                 343.6,
}

aliases = {
    "m/s": "meter_per_second",
    "mps": "meter_per_second",
    "m/min": "meter_per_minute",
    "m/h": "meter_per_hour",

    "km/s": "kilometer_per_second",
    "km/min": "kilometer_per_minute",
    "km/h": "kilometer_per_hour",
    "kph": "kilometer_per_hour",

    "mi/s": "mile_per_second",
    "mi/min": "mile_per_minute",
    "mi/h": "mile_per_hour",
    "mph": "mile_per_hour",

    "ft/s": "foot_per_second",
    "fps": "foot_per_second",
    "ft/min": "foot_per_minute",
    "ft/h": "foot_per_hour",

    "yd/s": "yard_per_second",
    "yd/min": "yard_per_minute",
    "yd/h": "yard_per_hour",

    "kt": "knot",
    "kn": "knot",
    "sol": "speed_of_light",

    "mach": "mach_air_20c",
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