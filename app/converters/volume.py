from decimal import Decimal, getcontext

getcontext().prec = 100

factor = {}

def convert(value, from_unit, to_unit, round_to=10):
    raise NotImplementedError
