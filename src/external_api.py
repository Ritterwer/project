import os
from typing import Any, Dict

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("BASE_URL")


def currency_conversion(transaction: Dict[str, Any]) -> float:
    """Конвертация суммы транзакции в рубли на основе текущего курса валют."""
    amount = transaction.get("operationAmount", {}).get("amount")
    code = transaction.get("operationAmount", {}).get("currency", {}).get("code")

    if amount is None or code is None:
        raise ValueError("Недостаточно информации для конвертации валюты")

    to = "RUB"
    url = f"https://api.apilayer.com/exchangerates_data/convert?to={to}&from={code}&amount={amount}"

    headers = {"apikey": API_KEY}
    payload = {}
    response = requests.get(url, headers=headers, data=payload)
    result = response.json()
    return result["result"]
