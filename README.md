# Bottle – Unit Converter API

Fast, lightweight, and accurate unit conversion API for 100+ units across 10 categories. Built by **Bottle** for developers who need reliable conversions.

**Live on RapidAPI:** [Bottle – Unit Converter](LinkHier)

---

## Overview

Convert between units instantly:
- **10 categories** (Length, Weight, Area, Volume, Time, Temperature, Speed, Pressure, Energy, Data)
- **100+ units** with alias support
- **High precision** (configurable rounding)
- **Simple REST API** with clear JSON responses

Perfect for apps, scripts, workflows, and integrations that need reliable unit conversions.

---

## Quick Start

### Endpoint

```
GET /{category}/convert
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `value` | float | **required** | Value to convert |
| `from_unit` | string | **required** | Source unit (name or alias) |
| `to_unit` | string | **required** | Target unit (name or alias) |
| `round_to` | integer | `10` | Decimal places (0–25) |

### Example Request

```bash
curl "https://api-converter-bottle.onrender.com/length/convert?value=1&from_unit=mile&to_unit=kilometer"
```

**Response:**
```json
{
  "result": 1.609344,
  "from_unit": "mile",
  "to_unit": "kilometer",
  "input": 1
}
```

---

## Categories & Units

### 1. Length

Convert meters, kilometers, miles, feet, light-years, and more.

- meter (m)
- kilometer (km)
- decimeter (dm)
- centimeter (cm)
- millimeter (mm)
- micrometer (um, μm)
- nanometer (nm)
- picometer (pm)
- mile (mi)
- yard (yd)
- foot (ft)
- inch (in)
- thou (mil)
- nautical_mile (nmi)
- au (au)
- light_second (ls)
- light_minute (lm)
- light_hour (lh)
- light_year (ly)

**Example:**
```bash
# Convert 1 light-year to kilometers
curl "https://api-converter-bottle.onrender.com/length/convert?value=1&from_unit=light_year&to_unit=km"
```
```json
{
  "result": 9460730472580800.0,
  "from_unit": "light_year",
  "to_unit": "km",
  "input": 1.0
}
```

---

### 2. Weight

Convert kilograms, pounds, ounces, stones, tons, and atomic units.

- kilogram (kg)
- gram (g)
- milligram (mg)
- microgram (ug, μg, mcg)
- nanogram (ng)
- metric_ton (t)
- long_ton
- short_ton
- pound (lb, lbs)
- ounce (oz)
- carat (ct)
- atomic_mass_unit (amu, u, da)
- stone (st)
- grain (gr)

**Example:**
```bash
# Convert 150 pounds to kilograms
curl "https://api-converter-bottle.onrender.com/weight/convert?value=150&from_unit=lb&to_unit=kg&round_to=2"
```
```json
{
  "result": 68.04,
  "from_unit": "lb",
  "to_unit": "kg",
  "input": 150.0
}
```

---

### 3. Area

Convert square meters, acres, hectares, square miles, and more.

- square_meter (m2, sqm)
- square_kilometer (km2)
- square_centimeter (cm2)
- square_millimeter (mm2)
- square_micrometer (um2, μm2)
- hectare (ha)
- square_mile (mi2)
- square_yard (yd2)
- square_foot (ft2, sqft)
- square_inch (in2)
- acre (ac)
- square_nautical_mile (nmi2)

**Example:**
```bash
# Convert 100 acres to square kilometers
curl "https://api-converter-bottle.onrender.com/area/convert?value=100&from_unit=acre&to_unit=km2&round_to=3"
```
```json
{
  "result": 0.405,
  "from_unit": "acre",
  "to_unit": "km2",
  "input": 100.0
}
```

---

### 4. Volume

Convert liters, gallons, cubic meters, pints, fluid ounces, and more.

- cubic_meter (m3)
- cubic_kilometer (km3)
- cubic_centimeter (cm3)
- cubic_millimeter (mm3)
- liter (l)
- milliliter (ml)
- gallon_us (gal)
- quart_us (qt)
- pint_us (pt)
- cup_us (cup)
- fluid_ounce_us (floz)
- table_spoon_us (tbsp)
- tea_spoon_us (tsp)
- gallon_imperial (igal)
- quart_imperial (iqt)
- pint_imperial (ipt)
- fluid_ounce_imperial (ifloz)
- table_spoon_imperial
- tea_spoon_imperial
- cubic_mile (mi3)
- cubic_yard (yd3)
- cubic_foot (ft3)
- cubic_inch (in3)

**Example:**
```bash
# Convert 1 gallon (US) to liters
curl "https://api-converter-bottle.onrender.com/volume/convert?value=1&from_unit=gal&to_unit=l&round_to=3"
```
```json
{
  "result": 3.785,
  "from_unit": "gal",
  "to_unit": "l",
  "input": 1.0
}
```

---

### 5. Time

Convert seconds, minutes, hours, days, months, years, and sub-second units.

- second (s, sec)
- millisecond (ms)
- microsecond (us, μs)
- nanosecond (ns)
- picosecond (ps)
- minute (min)
- hour (h, hr)
- day (d)
- week (wk)
- month (mo)
- year (y, yr)

**Note:** `month` = 30.4375 days (average), `year` = 365.25 days (average)

**Example:**
```bash
# Convert 2 hours to seconds
curl "https://api-converter-bottle.onrender.com/time/convert?value=2&from_unit=h&to_unit=s"
```
```json
{
  "result": 7200.0,
  "from_unit": "h",
  "to_unit": "s",
  "input": 2.0
}
```

---

### 6. Temperature

Convert between Kelvin, Celsius, and Fahrenheit.

- kelvin (k, °k)
- celsius (c, °c)
- fahrenheit (f, °f)

**Note:** Temperature conversion uses absolute reference. Example: 0°C = 273.15K = 32°F

**Example:**
```bash
# Convert 100°C to Fahrenheit
curl "https://api-converter-bottle.onrender.com/temperature/convert?value=100&from_unit=celsius&to_unit=fahrenheit"
```
```json
{
  "result": 212.0,
  "from_unit": "celsius",
  "to_unit": "fahrenheit",
  "input": 100.0
}
```

---

### 7. Speed

Convert m/s, km/h, mph, knots, speed of light, and more.

- meter_per_second (m/s, mps)
- meter_per_minute (m/min)
- meter_per_hour (m/h)
- kilometer_per_second (km/s)
- kilometer_per_minute (km/min)
- kilometer_per_hour (km/h, kph)
- mile_per_second (mi/s)
- mile_per_minute (mi/min)
- mile_per_hour (mi/h, mph)
- foot_per_second (ft/s, fps)
- foot_per_minute (ft/min)
- foot_per_hour (ft/h)
- yard_per_second (yd/s)
- yard_per_minute (yd/min)
- yard_per_hour (yd/h)
- knot (kt, kn)
- speed_of_light (sol)
- earth_orbital_velocity
- mach_air_20c (mach)

**Note:** `mach` is at 20°C and 1 atm (sea level)

**Example:**
```bash
# Convert 100 km/h to mph
curl "https://api-converter-bottle.onrender.com/speed/convert?value=100&from_unit=km/h&to_unit=mph&round_to=2"
```
```json
{
  "result": 62.14,
  "from_unit": "km/h",
  "to_unit": "mph",
  "input": 100.0
}
```

---

### 8. Pressure

Convert pascals, bars, atmospheres, PSI, millimeters of mercury, and more.

- pascal (pa)
- kilopascal (kpa)
- megapascal (mpa)
- gigapascal (gpa)
- bar
- millibar (mbar)
- hectopascal (hpa)
- atmosphere (atm)
- torr
- psi
- ksi
- millimeter_mercury (mmhg)
- inch_mercury (inhg)
- millimeter_water (mmh2o)
- inch_water (inh2o)

**Example:**
```bash
# Convert 1 atmosphere to pascals
curl "https://api-converter-bottle.onrender.com/pressure/convert?value=1&from_unit=atm&to_unit=pa"
```
```json
{
  "result": 101325.0,
  "from_unit": "atm",
  "to_unit": "pa",
  "input": 1.0
}
```

---

### 9. Energy

Convert joules, kilowatt-hours, calories, BTU, TNT, and electron volts.

- joule (j)
- kilojoule (kj)
- megajoule (mj)
- gigajoule (gj)
- watt_hour (wh)
- kilowatt_hour (kwh)
- megawatt_hour (mwh)
- gigawatt_hour (gwh)
- calorie (cal)
- kilocalorie (kcal)
- btu
- therm
- electronvolt (ev)
- kiloelectronvolt (kev)
- megaelectronvolt (mev)
- foot_pound
- ton_tnt
- kiloton_tnt
- megaton_tnt

**Example:**
```bash
# Convert 1 kilowatt-hour to joules
curl "https://api-converter-bottle.onrender.com/energy/convert?value=1&from_unit=kwh&to_unit=j"
```
```json
{
  "result": 3600000.0,
  "from_unit": "kwh",
  "to_unit": "j",
  "input": 1.0
}
```

---

### 10. Data

Convert bits, bytes, kilobytes, megabytes, gigabytes, terabytes, and more.

- bit (b)
- nibble
- byte (B)
- character
- word
- double_word
- quadruple_word
- block
- kilobit (kb, kib)
- kilobyte (kB)
- megabit (mb, mib)
- megabyte (MB)
- gigabit (gb, gib)
- gigabyte (GB)
- terabit (tb, tib)
- terabyte (TB)
- petabit (pb, pib)
- petabyte (PB)
- exabit (eb, eib)
- exabyte (EB)

**Example:**
```bash
# Convert 1 gigabyte to megabytes
curl "https://api-converter-bottle.onrender.com/data/convert?value=1&from_unit=GB&to_unit=MB"
```
```json
{
  "result": 1024.0,
  "from_unit": "GB",
  "to_unit": "MB",
  "input": 1.0
}
```

---

## Error Handling

Invalid units return a **422 Unprocessable Entity** error:

```json
{
  "detail": "unknown from_unit: invalid_unit"
}
```

Always validate unit names against the category's unit list before calling the API.

---

## Health Check

```bash
curl "https://api-converter-bottle.onrender.com/health"
```

```json
{
  "status": "ok"
}
```

---

## Rate Limits & Pricing

Check your RapidAPI plan for rate limits and quotas.

---

## Support

For issues or questions, contact Bottle support or file an issue on GitHub.

---

**Made with ❤️ by Bottle**