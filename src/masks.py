import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("..//logs/masks.log", "w", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Функция, которая маскирует номер карты"""
    try:
        masked_number = f"{card_number[:4]} {card_number[4:6]}** **** {card_number[12:]}"
        logger.info(f"Маскировка номера карты успешна: {masked_number}")
        return masked_number
    except Exception as e:
        logger.error(f"Ошибка при маскировке номера карты: {e}")
        raise


def get_mask_account(account_number: str) -> str:
    """Функция, которая маскирует номер счета"""
    try:
        masked_account = f"**{account_number[-4:]}"
        logger.info(f"Маскировка номера счета успешна: {masked_account}")
        return masked_account
    except Exception as e:
        logger.error(f"Ошибка при маскировке номера счета: {e}")
        raise


if __name__ == "__main__":
    card_number_example = "7000792289606361"
    account_number_example = "73654108430135874305"

    masked_card_number = get_mask_card_number(card_number_example)
    masked_account_number = get_mask_account(account_number_example)

    print(masked_card_number)
    print(masked_account_number)
