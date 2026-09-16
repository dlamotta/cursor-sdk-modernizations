# Copyright (c) 2026. All rights reserved.

from decimal import Decimal

from intcalc import DEFAULT_ANNUAL_RATE, calc_daily, calculate_interest


def test_default_interest_calculation():
    result = calculate_interest(Decimal("12500.50"))
    assert result.annual_rate == DEFAULT_ANNUAL_RATE
    assert result.days == 31
    assert result.daily_rate == Decimal("0.0001")
    assert result.daily_interest == Decimal("1.25")
    assert result.total_interest == Decimal("38.75")
    assert result.new_balance == Decimal("12539.25")


def test_daily_rate_truncation():
    daily_rate, daily_interest = calc_daily(Decimal("12500.50"), Decimal("0.05"))
    assert daily_rate == Decimal("0.0001")
    assert daily_interest == Decimal("1.25")


def test_small_balance_loses_penny_dust():
    daily_rate, daily_interest = calc_daily(Decimal("10.00"), Decimal("0.05"))
    assert daily_rate == Decimal("0.0001")
    assert daily_interest == Decimal("0.00")

    result = calculate_interest(Decimal("10.00"), days=31)
    assert result.total_interest == Decimal("0.00")
    assert result.new_balance == Decimal("10.00")
