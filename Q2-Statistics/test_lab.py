import pytest
from main import calculate_statistics


def test_basic_statistics():
    """Test with sample input"""
    result = calculate_statistics([12, 5, 8, 19, 3])
    assert result['sum'] == 47
    assert result['average'] == 9.4
    assert result['max'] == 19
    assert result['min'] == 3


def test_single_element():
    """Test with single element"""
    result = calculate_statistics([10])
    assert result['sum'] == 10
    assert result['average'] == 10.0
    assert result['max'] == 10
    assert result['min'] == 10


def test_negative_numbers():
    """Test with negative numbers"""
    result = calculate_statistics([-5, -10, -3])
    assert result['sum'] == -18
    assert result['average'] == -6.0
    assert result['max'] == -3
    assert result['min'] == -10


def test_mixed_numbers():
    """Test with mixed positive and negative"""
    result = calculate_statistics([10, -5, 3, -2, 4])
    assert result['sum'] == 10
    assert result['average'] == 2.0
    assert result['max'] == 10
    assert result['min'] == -5


def test_all_same():
    """Test with all same numbers"""
    result = calculate_statistics([5, 5, 5, 5])
    assert result['sum'] == 20
    assert result['average'] == 5.0
    assert result['max'] == 5
    assert result['min'] == 5