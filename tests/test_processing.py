import pytest

from src.processing import filter_by_state, sort_by_date
from tests.conftest import (my_list_dict_all_canceled, my_list_dict_executed, my_list_dict_canceled,
                            my_list_dict_no_state, my_list_dict_sorted_1, my_list_dict_sorted_2,
                            my_list_dict_sorted_date)


@pytest.fixture
def my_list_dict_fixture() -> list:
    return [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def my_list_dict_sorted_date_fixture() -> list:
    return [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    {"id": 156272841, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]


"""Тесты для filter_by_state"""

