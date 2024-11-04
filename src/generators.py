from typing import Iterator


def filter_by_currency(transactions: list, currency: str) -> Iterator:
    """Фильтрует транзакции по валюте и возвращает итератор для результатов."""
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction


def transaction_descriptions(transactions: list) -> Iterator:
    """Генератор, возвращающий описания транзакций по очереди."""
    for transaction in transactions:
        yield transaction.get("description", "Нет описания")


def card_number_generator(start: int, stop: int) -> Iterator:
    """Генератор, выдающий номера банковских карт в формате 'XXXX XXXX XXXX XXXX'."""

    if start == 0 and stop > 0:
        start += 1
    for number in range(start, stop):
        card_number = str(number)
        while len(card_number) < 16:
            if start < 1000000000000000:
                card_number = "0" + card_number
        formatted_card_number = f"{card_number[0:4]}{card_number[4:8]}{card_number[8:12]}{card_number[12:16]}"
        yield formatted_card_number
