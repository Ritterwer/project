from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(nums: str) -> str | None:
    """Фикция общей маскировки карты и счёта"""
    if 'счет' in nums:
        return get_mask_account(nums)
    else:
        cards = get_mask_card_number(nums[-16:])
        new_card = nums. replace(nums[-16:], cards)
        return new_card


print(mask_account_card('Счет 73654108430135874305'))
print(mask_account_card('Visa Platinun 7008792289606361'))
print(mask_account_card('Maestro 7000792289606361'))


def get_date(date: str) -> str | None:
    """Финкция преобразования даты"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]})"


print(get_date('2024-03-11T02:26:18.671407'))
