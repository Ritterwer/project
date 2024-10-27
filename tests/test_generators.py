from typing import Any

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize("currency, expected_count", [("USD", 2), ("EUR", 1), ("GBP", 0)])
def test_filter_by_currency(transactions: list[dict[str, Any]], currency: str, expected_count: int) -> None:
    result = list(filter_by_currency(transactions, currency))
    assert len(result) == expected_count


def test_filter_by_currency_empty() -> None:
    result = list(filter_by_currency([], "USD"))
    assert result == []


def test_transaction_descriptions(transactions: list[dict[str, Any]]) -> None:
    result = list(transaction_descriptions(transactions))
    assert result == ["Перевод организации", "Перевод со счета на счет", "Перевод отменен"]


def test_transaction_descriptions_empty() -> None:
    result = list(transaction_descriptions([]))
    assert result == []


@pytest.mark.parametrize(
    "start, stop, expected_numbers",
    [
        (1, 3, ["0000000000000001", "0000000000000002", "0000000000000003"]),
        (10, 10, ["0000000000000010"]),
        (100, 102, ["0000000000000100", "0000000000000101"]),
    ],
)
def test_card_number_generator(start: int, stop: int, expected_numbers: list[str]) -> None:
    generated_numbers = list(card_number_generator(start, stop))
    assert generated_numbers == expected_numbers


def test_card_number_generator_format() -> None:
    generated_numbers = list(card_number_generator(1, 5))
    assert all(len(num.replace(" ", "")) == 16 for num in generated_numbers)


def test_card_number_generator_empty() -> None:
    generated_numbers = list(card_number_generator(5, 1))
    assert generated_numbers == []
