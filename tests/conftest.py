from typing import Any
import pytest


@pytest.fixture
def mask_card() -> Any:
    return "7000792289606361", "7365410843013587", "7000F922896S6361", "7000792289606361627911", ""


@pytest.fixture
def mask_account() -> Any:
    return "73654108430135874305", "7000792289606361627911", "73654108430135874305DXK", "135"


@pytest.fixture
def mask_account_card_change() -> Any:
    return "Счет 63829169283549154926", "Visa Platinun 7008792289606361", "Счет 82739465720374638254"


@pytest.fixture
def mask_account_card_change_type() -> Any:
    return "Счет 63829169283549154926", "Maestro 7008792289606361", "Счет 82739465720374638254"


@pytest.fixture
def mask_account_card_change_error() -> Any:
    return "Счет 638291", "Maero 700879228", "", "Visa Platinun 700879606361", "xhch5478293", "827394657203746382"


@pytest.fixture
def get_date_change() -> Any:
    return "2024-03-11T02:26:18.671407", "2024-03-11T02:2.671407", "2024-03-11T05332:26:18.671407", "", "fxtew1324"
