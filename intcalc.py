"""Savings interest for a statement period (modernized from INTCALC.cbl)."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import ROUND_HALF_UP, Decimal

TWO_PLACES = Decimal("0.01")
DAYS_PER_YEAR = Decimal("365")
DEFAULT_ANNUAL_RATE = Decimal("0.0525")  # 5.25%; legacy PIC 9V99 truncated to 0.05


@dataclass(frozen=True)
class InterestResult:
    principal: Decimal
    annual_rate: Decimal
    days: int
    daily_rate: Decimal
    daily_interest: Decimal
    total_interest: Decimal
    new_balance: Decimal


def _quantize(value: Decimal) -> Decimal:
    return value.quantize(TWO_PLACES, rounding=ROUND_HALF_UP)


def calc_daily_rate(annual_rate: Decimal) -> Decimal:
    return annual_rate / DAYS_PER_YEAR


def calc_daily_interest(principal: Decimal, daily_rate: Decimal) -> Decimal:
    return _quantize(principal * daily_rate)


def accumulate_interest(daily_interest: Decimal, days: int) -> Decimal:
    return _quantize(daily_interest * Decimal(days))


def calculate_interest(
    principal: Decimal,
    annual_rate: Decimal = DEFAULT_ANNUAL_RATE,
    days: int = 31,
) -> InterestResult:
    daily_rate = calc_daily_rate(annual_rate)
    daily_interest = calc_daily_interest(principal, daily_rate)
    total_interest = accumulate_interest(daily_interest, days)
    new_balance = _quantize(principal + total_interest)
    return InterestResult(
        principal=principal,
        annual_rate=annual_rate,
        days=days,
        daily_rate=daily_rate,
        daily_interest=daily_interest,
        total_interest=total_interest,
        new_balance=new_balance,
    )


def format_currency(amount: Decimal) -> str:
    return f"${amount:,.2f}"


def main() -> InterestResult:
    result = calculate_interest(Decimal("12500.50"))
    print("INTCALC START")
    print(f"PRINCIPAL={result.principal}")
    print(f"RATE={result.annual_rate}")
    print(f"DAYS={result.days}")
    print(f"DAILY RATE={result.daily_rate}")
    print(f"DAILY INT={result.daily_interest}")
    print(f"INTEREST={result.total_interest}")
    print(f"NEW BALANCE={format_currency(result.new_balance)}")
    print("INTCALC END")
    return result


if __name__ == "__main__":
    main()
