# Copyright (c) 2026. All rights reserved.

from decimal import Decimal

from minbal import StatusCode, evaluate_withdrawal


def test_default_withdrawal_rejected():
    result = evaluate_withdrawal(Decimal("1200.00"), Decimal("950.00"))
    assert result.remaining == Decimal("250.00")
    assert result.status.code == StatusCode.BELOW_MINIMUM
    assert result.status.text == "BELOW MINIMUM"


def test_withdrawal_approved_when_remaining_at_minimum():
    result = evaluate_withdrawal(Decimal("1500.00"), Decimal("1000.00"))
    assert result.remaining == Decimal("500.00")
    assert result.status.code == StatusCode.OK
    assert result.status.text == "OK"


def test_withdrawal_approved_when_remaining_above_minimum():
    result = evaluate_withdrawal(Decimal("2000.00"), Decimal("500.00"))
    assert result.remaining == Decimal("1500.00")
    assert result.status.code == StatusCode.OK
