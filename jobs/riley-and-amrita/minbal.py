# Copyright 2026 SpaceXAi

"""Reject withdrawals that breach minimum balance (modernized from MINBAL.cbl)."""

from __future__ import annotations

from dataclasses import dataclass
from enum import IntEnum

import numpy as np


class StatusCode(IntEnum):
    OK = 0
    BELOW_MINIMUM = 9


@dataclass(frozen=True)
class WithdrawalStatus:
    code: StatusCode
    text: str


@dataclass(frozen=True)
class WithdrawalResult:
    balance: np.float64
    withdraw: np.float64
    remaining: np.float64
    min_remaining: np.float64
    status: WithdrawalStatus


def evaluate_withdrawal(
    balance: np.float64,
    withdraw: np.float64,
    min_remaining: np.float64 = np.float64(500.00),
) -> WithdrawalResult:
    remaining = np.subtract(balance, withdraw)
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
        balance=np.float64(1200.00),
        withdraw=np.float64(950.00),
    )
    print("MINBAL START")
    print(f"BALANCE={result.balance:.2f}")
    print(f"WITHDRAW={result.withdraw:.2f}")
    print(f"REMAIN={result.remaining:.2f}")
    if result.status.code == StatusCode.BELOW_MINIMUM:
        print(f"REJECTED={result.status.text}")
    else:
        print(f"APPROVED={result.status.text}")
    print("MINBAL END")
    return result


if __name__ == "__main__":
    main()
