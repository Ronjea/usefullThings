import pytest

from calculate_progress import calculate_progress


def test_half_progress():
    assert calculate_progress([0, 1, 2, 3], 2) == 50.0


def test_full_progress():
    assert calculate_progress([1, 2], 2) == 100.0


def test_zero_progress():
    assert calculate_progress([1, 2, 3], 0) == 0.0
