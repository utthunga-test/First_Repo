import math


def net_income(revenues: float, expenses: float, decimals=2) -> float:
    multiplier = 10 ** decimals
    net_income = revenues - expenses
    return math.floor(net_income * multiplier + 0.5) / multiplier