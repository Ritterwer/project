from typing import Any

import pytest


@pytest.fixture
def card_data() -> list:
    return [("7000792289606361", "7000 79** **** 6361"), ("7634562893564253", "7634 56** **** 4253")]


@pytest.fixture
def account_data() -> list:
    return [("73654108430135874305", "**4305"), ("73654108430135871856", "**1856")]


@pytest.fixture
def sample_data() -> list[dict[str, Any]]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def unsorted_dates() -> list[dict[str, Any]]:
    return [
        {"id": 1, "date": "2018-10-14T08:21:33.419441"},
        {"id": 2, "date": "2018-06-30T02:08:58.425572"},
        {"id": 3, "date": "2019-07-03T18:35:29.512364"},
        {"id": 4, "date": "2018-09-12T21:27:25.241689"},
    ]


@pytest.fixture
def unsorted_invalid_dates() -> list[dict[str, Any]]:
    return [
        {"id": 1, "date": "Invalid date"},
        {"id": 2, "date": "Another invalid date"},
        {"id": 3, "date": "2019-07-03T18:35:29.512364"},
    ]


@pytest.fixture
def transactions() -> list[dict[str, Any]]:
    """Фикстура для создания тестовых данных транзакций."""
    return [
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
        },
        {
            "id": 142264268,
            "state": "EXECUTED",
            "date": "2019-04-04T23:20:05.206878",
            "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод со счета на счет",
            "from": "Счет 19708645243227258542",
            "to": "Счет 75651667383060284188",
        },
        {
            "id": 100000003,
            "state": "CANCELLED",
            "date": "2020-01-01T12:00:00.000000",
            "operationAmount": {"amount": "500.00", "currency": {"name": "EUR", "code": "EUR"}},
            "description": "Перевод отменен",
            "from": "Счет 12345678901234567890",
            "to": "Счет 09876543210987654321",
        },
    ]
