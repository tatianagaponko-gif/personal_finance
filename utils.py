import re
from datetime import datetime

def validate_amount(amount_str):
    try:
        amount = float(amount_str)
        return amount
    except ValueError:
        raise ValueError("Некорректная сумма.")

def validate_date(date_str):
    pattern = r"\d{4}-\d{2}-\d{2}"
    if re.match(pattern, date_str):
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            raise ValueError("Некорректная дата.")
    else:
        raise ValueError("Дата должна быть в формате ГГГГ-ММ-ДД")