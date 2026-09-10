from __future__ import annotations

from dataclasses import dataclass
from decimal import ROUND_DOWN, Decimal

DAYS_PER_YEAR = Decimal("365")
DEFAULT_ANNUAL_RATE = Decimal("0.05")


@dataclass(frozen=True)
class InterestResult:
    principal: Decimal
    annual_rate: Decimal
    days: int
    daily_rate: Decimal
    daily_interest: Decimal
    total_interest: Decimal
    new_balance: Decimal


def _truncate(value: Decimal, places: int) -> Decimal:
    quantizer = Decimal(10) ** -places
    return value.quantize(quantizer, rounding=ROUND_DOWN)


def calc_daily(principal: Decimal, annual_rate: Decimal) -> tuple[Decimal, Decimal]:
    daily_rate = _truncate(annual_rate / DAYS_PER_YEAR, 4)
    daily_interest = _truncate(principal * daily_rate, 2)
    return daily_rate, daily_interest


def accumulate(daily_interest: Decimal, days: int) -> Decimal:
    interest = Decimal("0")
    for day in range(1, days + 1):
        interest += daily_interest
        print(f"DAY={day} RUNNING={interest}")
    return interest


def apply_to_bal(principal: Decimal, interest: Decimal) -> Decimal:
    return principal + interest


def calculate_interest(
    principal: Decimal,
    annual_rate: Decimal = DEFAULT_ANNUAL_RATE,
    days: int = 31,
) -> InterestResult:
    daily_rate, daily_interest = calc_daily(principal, annual_rate)
    total_interest = accumulate(daily_interest, days)
    new_balance = apply_to_bal(principal, total_interest)
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
    principal = Decimal("12500.50")
    annual_rate = DEFAULT_ANNUAL_RATE
    days = 31

    print("INTCALC START")
    print(f"PRINCIPAL={principal}")
    print(f"RATE={annual_rate}")
    print(f"DAYS={days}")

    daily_rate, daily_interest = calc_daily(principal, annual_rate)
    print(f"DAILY RATE (TRUNC)={daily_rate}")
    print(f"DAILY INT (TRUNC)={daily_interest}")

    total_interest = accumulate(daily_interest, days)
    new_balance = apply_to_bal(principal, total_interest)
    print(f"INTEREST={total_interest}")
    print(f"NEW BALANCE={format_currency(new_balance)}")
    print("INTCALC END")

    return InterestResult(
        principal=principal,
        annual_rate=annual_rate,
        days=days,
        daily_rate=daily_rate,
        daily_interest=daily_interest,
        total_interest=total_interest,
        new_balance=new_balance,
    )


if __name__ == "__main__":
    main()
