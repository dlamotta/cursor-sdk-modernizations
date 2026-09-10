from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class FeeResult:
    balance: Decimal
    min_balance: Decimal
    fee: Decimal
    new_balance: Decimal
    fee_applied: bool


def calculate_fee(
    balance: Decimal,
    min_balance: Decimal = Decimal("500.00"),
    fee: Decimal = Decimal("12.50"),
) -> FeeResult:
    if balance < min_balance:
        new_balance = balance - fee
        return FeeResult(balance, min_balance, fee, new_balance, True)
    return FeeResult(balance, min_balance, fee, balance, False)


def format_currency(amount: Decimal) -> str:
    return f"${amount:,.2f}"


def main() -> FeeResult:
    result = calculate_fee(Decimal("450.75"))
    print("FEECALC START")
    print(f"BALANCE={result.balance}")
    print(f"MIN={result.min_balance}")
    if result.fee_applied:
        print(f"FEE APPLIED={result.fee}")
        print(f"NEW BALANCE={format_currency(result.new_balance)}")
    else:
        print("NO FEE")
    print("FEECALC END")
    return result


if __name__ == "__main__":
    main()
