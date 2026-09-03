"""Reject withdrawals that breach minimum balance (modernized from MINBAL.cbl)."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from enum import IntEnum


class StatusCode(IntEnum):
    OK = 0
    BELOW_MINIMUM = 9


@dataclass(frozen=True)
class WithdrawalStatus:
    code: StatusCode
    text: str


@dataclass(frozen=True)
class WithdrawalResult:
    balance: Decimal
    withdraw: Decimal
    remaining: Decimal
    min_remaining: Decimal
    status: WithdrawalStatus


def evaluate_withdrawal(
    balance: Decimal,
    withdraw: Decimal,
    min_remaining: Decimal = Decimal("500.00"),
) -> WithdrawalResult:
    remaining = balance - withdraw
    if remaining < min_remaining:
        status = WithdrawalStatus(StatusCode.BELOW_MINIMUM, "BELOW MINIMUM")
    else:
        status = WithdrawalStatus(StatusCode.OK, "OK")
    return WithdrawalResult(
        balance=balance,
        withdraw=withdraw,
        remaining=remaining,
        min_remaining=min_remaining,
        status=status,
    )


def main() -> WithdrawalResult:
    result = evaluate_withdrawal(
        balance=Decimal("1200.00"),
        withdraw=Decimal("950.00"),
    )
    print("MINBAL START")
    print(f"BALANCE={result.balance}")
    print(f"WITHDRAW={result.withdraw}")
    print(f"REMAIN={result.remaining}")
    if result.status.code == StatusCode.BELOW_MINIMUM:
        print(f"REJECTED={result.status.text}")
    else:
        print(f"APPROVED={result.status.text}")
    print("MINBAL END")
    return result


if __name__ == "__main__":
    main()
