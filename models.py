from datetime import datetime

class Transaction:
    """
    Класс для описания финансовой операции.
    """
    def __init__(self, amount: float, category: str, date: str, comment: str = ""):
        self.amount = amount
        self.category = category
        self.date = datetime.strptime(date, "%Y-%m-%d")
        self.comment = comment

    def __repr__(self):
        return f"<Transaction {self.amount} {self.category} {self.date.strftime('%Y-%m-%d')}>"