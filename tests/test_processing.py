import pytest
from typing import Any
from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize(
    "my_list_dict, state,",
    [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ],
)
def test_filter_by_state(my_list_dict: list[dict[str, Any]], state: str = "EXECUTED") -> None:
    assert filter_by_state(my_list_dict) == state


@pytest.mark.parametrize(
    "my_list_dict, reverse_list",
    [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ],
)
def test_sort_by_date(my_list_dict: list[dict[str, Any]], reverse_list: bool = True) -> None:
    assert sort_by_date(my_list_dict) == reverse_list
