# Copyright (c) 2026. All rights reserved.

from decimal import Decimal

from feecalc import calculate_fee


def test_default_balance_below_minimum_applies_fee():
    result = calculate_fee(Decimal("450.75"))
    assert result.fee_applied is True
    assert result.new_balance == Decimal("438.25")
    assert result.fee == Decimal("12.50")
    assert result.min_balance == Decimal("500.00")


def test_balance_at_minimum_no_fee():
    result = calculate_fee(Decimal("500.00"))
    assert result.fee_applied is False
    assert result.new_balance == Decimal("500.00")


def test_balance_above_minimum_no_fee():
    result = calculate_fee(Decimal("750.00"))
    assert result.fee_applied is False
    assert result.new_balance == Decimal("750.00")
