def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты"""
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер счета"""
    return f"**{account_number[-4:]}"


card_number_example = "7000792289606361"
account_number_example = "73654108430135874305"


masked_card_number = get_mask_card_number(card_number_example)
masked_account_number = get_mask_account(account_number_example)


print(masked_card_number)
print(masked_account_number)
