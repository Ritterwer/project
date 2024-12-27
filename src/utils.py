import json
import logging
from json import JSONDecodeError
from typing import Any, Dict, List

from src.external_api import currency_conversion

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("..//logs/utils.log", "w", encoding="utf-8")
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def financial_transactions(path: str) -> List[Dict[str, Any]]:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях."""
    try:
        with open(path, encoding="utf-8") as financial_file:
            try:
                transactions = json.load(financial_file)
                logger.info(f"Успешно загружены транзакции из файла: {path}")
            except JSONDecodeError:
                logger.error(f"Ошибка при декодировании JSON из файла: {path}")
                return []

            if not isinstance(transactions, list):
                logger.error(f"Загруженные данные не являются списком: {transactions}")
                return []

            return transactions
    except FileNotFoundError:
        logger.error(f"Файл не найден: {path}")
        return []


def transaction_amount(trans: Dict[str, Any], currency: str = "RUB") -> float:
    """Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях."""
    try:
        if trans["operationAmount"]["currency"]["code"] == currency:
            amount = trans["operationAmount"]["amount"]
            logger.info(f"Сумма транзакции в рублях: {amount}")
        else:
            amount = currency_conversion(trans)
            logger.info(f"Сумма прошла конвертацию, итоговая сумма: {amount}")

        return amount
    except KeyError as e:
        logger.error(f"Ошибка доступа к ключу в транзакции: {e}")
        raise
